import { CommandBus } from 'node-cqrs';
import { EntityManager, getManager } from 'typeorm';
import { User } from '../../../auth_management/domain/models/users.model';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import BaseException from '../../../common/exceptions/BaseException';
import { RunInTransaction } from '../../../common/repos/transaction';
import container from '../../../container';
import { MessageEntity } from '../../domain/entities/message.entity';
import { RoomEntity } from '../../domain/entities/rooms.entity';
import { MediaType } from '../../domain/enums/mediaType.enum';
import { RoomType } from '../../domain/enums/roomType.enum';
import { Message } from '../../domain/models/message.model';
import { Room } from '../../domain/models/rooms.model';
import { UserRoom } from '../../domain/models/user_rooms.model';
import { IMessageRepository, MessageRepository } from '../../domain/repositories/message.repos';
import { IRoomRepository, RoomRepository } from '../../domain/repositories/room.repos';
import { MessageDto } from '../dtos/message.dto';
import { RoomChatDto } from '../dtos/room_chat.dto';
import { RoomSimpleDto } from '../dtos/room_simple.dto';

class RoomService {
  private commandBus: CommandBus;
  private roomRepos: IRoomRepository;
  private userRepos: UserRepository;
  private messageRepos: IMessageRepository;

  constructor() {
    this.commandBus = container.commandBus;
    this.roomRepos = new RoomRepository();
    this.userRepos = new UserRepository();
    this.messageRepos = new MessageRepository();
  }

  public async createRoomChat(accountId: string, receiverId: string): Promise<Room> {
    const account = await this.userRepos.getOrCreateAccountByBaseAccountId(accountId);
    const receiver = await this.userRepos.getOrCreateAccountByBaseAccountId(receiverId);

    // find existed room chat.
    const availableRooms = await account.getRooms();

    let room: Room = null;
    for (let idx = 0; idx < availableRooms.length; idx++) {
      const element: Room = availableRooms[idx];
      const availableMemberIds: Array<string> = await element.getMemberIds();
      if (availableMemberIds.includes(receiver.id)) {
        room = element;
        break;
      }
    }
    if (room) {
      return room;
    }

    await RunInTransaction(async (_manager: EntityManager) => {
      // Create new room chat
      room = new RoomEntity(RoomType.NORMAL);
      room = await this.roomRepos.save(room);
      await account.joinRoom(room);
      await receiver.joinRoom(room);
    });

    return room;
  }

  public async sendMessage(accountId: string, roomId: string, message_data: any): Promise<void> {
    const { content, media } = message_data;
    const { mediaUrl, type } = media;

    if (![MediaType.PHOTO, MediaType.VIDEO].includes(type)) {
      throw new BaseException(`Type photo is not existed.`);
    }

    const account = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    const availableRooms: Array<Room> = await account.getRooms();
    if (!availableRooms.some(item => item.id == room.id)) {
      throw new BaseException(`User ${accountId} isn't in this room`);
    }

    const accountRefRoom: UserRoom = await account.getUserRefRoom(room);
    // Create message
    await this.messageRepos.save(new MessageEntity(accountRefRoom, room, content));
  }

  public async sendSmartMsg(accountId: string, roomId: string, msg_data: any): Promise<void> {
    const { content } = msg_data;

    const account: User = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    // validate room active
    if (!room.isSmartRoomAlive()) {
      throw new BaseException(`Room ${roomId} isn't available.`);
    }

    // validate account in room
    if (!(await this.checkAccountInRoom(account, room))) {
      throw new BaseException(`User ${accountId} isn't existed in room ${roomId}.`);
    }

    const accountRefRoom: UserRoom = await account.getUserRefRoom(room);

    await this.messageRepos.save(new MessageEntity(accountRefRoom, room, content));
  }

  public async getAccountRoomChatList(accountId: string): Promise<any> {
    const account = await this.userRepos.findUserById(accountId, true);

    const availableRooms: Array<Room> = await account.getRooms();

    const data: Array<Promise<RoomChatDto>> = availableRooms.map(async item => {
      const lastMsg: Message = await item.getLastestMsg();

      return new RoomChatDto(item.id, '', item.generalName, 0, lastMsg.content, lastMsg.createdAt);
    });
    return await Promise.all(data);
  }

  public async getMessagesInRoomChat(accountId: string, roomId: string): Promise<Array<MessageDto>> {
    const account = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    const availableRooms: Array<Room> = await account.getRooms();
    if (!availableRooms.some(item => item.id == room.id)) {
      throw new BaseException(`This user can't access to room ${room.id}`);
    }

    const msgs = await room.getMsgs();

    return msgs.map(item => new MessageDto(item, []));
  }

  public async createSmartRoom(partnerAId: string, partnerBId: string): Promise<any> {
    const partnerA = await this.userRepos.findUserById(partnerAId, true);
    const partnerB = await this.userRepos.findUserById(partnerBId, true);

    // Validate
    const existedRoom: Room = await this.roomRepos.findRoomByTwoPartners(partnerA, partnerB);

    if (existedRoom) {
      if (existedRoom.type != RoomType.SMART) {
        throw new BaseException("Can't create smart chat for two partners.");
      }

      if (existedRoom.isSmartRoomAlive()) {
        return new RoomSimpleDto(existedRoom);
      } else {
        await this.roomRepos.delete(existedRoom.id);
      }
    }

    const partnerAIsReady: boolean = await partnerA.isReadyForNewSmartRoom();
    const partnerBIsReady: boolean = await partnerB.isReadyForNewSmartRoom();
    if (!(partnerAIsReady && partnerBIsReady)) {
      throw new BaseException("A partner isn't ready for new smart chat.");
    }

    // Create room
    const room: Room = await this.roomRepos.save(new RoomEntity(RoomType.SMART));
    await partnerA.joinRoom(room);
    await partnerB.joinRoom(room);

    return new RoomSimpleDto(room);
  }

  public async checkAccountInRoom(account: User, room: Room): Promise<boolean> {
    const availableMembers: Array<User> = await Promise.all(await room.getMembers());

    return availableMembers.some(mem => mem.id == account.id);
  }

  public async checkAccountInRoomType(accountId: string, roomId: string, type: number): Promise<boolean> {
    const account: User = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    return room.type == type && this.checkAccountInRoom(account, room);
  }
}

export default RoomService;
