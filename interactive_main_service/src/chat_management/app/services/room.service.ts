import { CommandBus } from 'node-cqrs';
import { EntityManager, getManager } from 'typeorm';
import { AccountGateway } from '../../../auth_management/app/gateways/account.gateway';
import { AccountReportDto } from '../../../auth_management/app/gateways/dtos/accountReport.dto';
import { User } from '../../../auth_management/domain/models/users.model';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import { AccountGatewayImpl } from '../../../auth_management/infras/gateway_impls/account.gatewayImpl';
import BaseException from '../../../common/exceptions/BaseException';
import { RunInTransaction } from '../../../common/repos/transaction';
import container from '../../../container';
import { MessageEntity } from '../../domain/entities/message.entity';
import { RoomEntity } from '../../domain/entities/rooms.entity';
import { MediaType } from '../../domain/enums/mediaType.enum';
import { RoomType } from '../../domain/enums/roomType.enum';
import { Message } from '../../domain/models/message.model';
import { ReactType } from '../../domain/models/react_smart_rooms.model';
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
  private accountGw: AccountGateway;

  constructor() {
    this.commandBus = container.commandBus;
    this.roomRepos = new RoomRepository();
    this.userRepos = new UserRepository();
    this.messageRepos = new MessageRepository();
    this.accountGw = new AccountGatewayImpl();
  }

  public async createRoomChat(accountId: string, receiverId: string, type: RoomType = RoomType.NORMAL): Promise<Room> {
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
      room = new RoomEntity(type);
      room = await this.roomRepos.save(room);
      await account.joinRoom(room);
      await receiver.joinRoom(room);
    });

    return room;
  }

  public async sendMessage(accountId: string, roomId: string, message_data: any): Promise<void> {
    const { content } = message_data;
    // const { mediaUrl, type } = media;

    // if (![MediaType.PHOTO, MediaType.VIDEO].includes(type)) {
    //   throw new BaseException(`Type photo is not existed.`);
    // }

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
    const account = await this.userRepos.getOrCreateAccountByBaseAccountId(accountId);

    const availableRooms: Array<Room> = await account.getRooms();

    const data: Array<Promise<RoomChatDto>> = availableRooms.map(async item => {
      const lastMsg: Message = await item.getLastestMsg();
      const content: string = (lastMsg && lastMsg.content) || '';
      const createdAt: Date = (lastMsg && lastMsg.createdAt) || new Date();

      const partner: User = await item.getParterOf(account);

      return new RoomChatDto(item.id, partner && partner.avatar, partner && partner.fullName, 0, content, createdAt);
    });
    return await Promise.all(data);
  }

  public async getMessagesInRoomChat(accountId: string, roomId: string): Promise<Array<MessageDto>> {
    const account = await this.userRepos.findAccountByBaseAccountId(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    const availableRooms: Array<Room> = await account.getRooms();
    if (!availableRooms.some(item => item.id == room.id)) {
      throw new BaseException(`This user can't access to room ${room.id}`);
    }

    const msgs = await room.getMsgs();

    return Promise.all(msgs.map(async item => new MessageDto(item, (await (await item.getSender()).getAccount()).refId, [])));
  }

  public async canCreateSmartRoom(parterAId: string, partnerBId: string): Promise<boolean> {
    const partnerA = await this.userRepos.findUserById(parterAId, true);
    const partnerB = await this.userRepos.findUserById(partnerBId, true);

    // Validate
    const existedRoom: Room = await this.roomRepos.findRoomByTwoPartners(partnerA, partnerB);

    if (existedRoom && existedRoom.type != RoomType.SMART) {
      return false;
    }

    return true;
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

      await this.roomRepos.delete(existedRoom.id);

      // if (existedRoom.isSmartRoomAlive()) {
      //   return new RoomSimpleDto(existedRoom);
      // } else {
      //   await this.roomRepos.delete(existedRoom.id);
      // }
    }

    const partnerAIsReady: boolean = await partnerA.isReadyForNewSmartRoom();
    const partnerBIsReady: boolean = await partnerB.isReadyForNewSmartRoom();
    if (!(partnerAIsReady && partnerBIsReady)) {
      throw new BaseException("A partner isn't ready for new smart chat.");
    }

    // Create room
    let room: Room = null;

    await RunInTransaction(async (_manager: EntityManager) => {
      room = await this.roomRepos.save(new RoomEntity(RoomType.SMART));
      await partnerA.joinRoom(room);
      await partnerB.joinRoom(room);
    });

    return new RoomSimpleDto(room);
  }

  public async checkAccountInRoom(account: User, room: Room): Promise<boolean> {
    const availableMembers: Array<User> = await room.getMembers();

    return availableMembers.some(mem => mem.id == account.id);
  }

  public async checkAccountInRoomType(accountId: string, roomId: string, type: number): Promise<boolean> {
    const account: User = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    return room.type == type && this.checkAccountInRoom(account, room);
  }

  public async reactSmartRoom(accountId: string, roomId: string): Promise<void> {
    const account: User = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    if (room.type !== RoomType.SMART) {
      throw new BaseException("Can't react this kind of room.");
    }

    await account.reactSmartRoom(room, ReactType.LOVE);
  }

  public async canMoveToNormalRoom(roomId: string): Promise<boolean> {
    const room: Room = await this.roomRepos.findById(roomId, true);

    return await room.canContinueIntoNormalRoom();
  }

  public async moveIntoNormalRoom(roomId: string): Promise<void> {
    const room: Room = await this.roomRepos.findById(roomId, true);

    if (await this.canMoveToNormalRoom(roomId)) {
      room.moveIntoNormalRoom();
      await this.roomRepos.update(roomId, room);
    }
  }

  public async reportUserSmartRoom(accountId: string, roomId: string, reason: string): Promise<void> {
    const account: User = await this.userRepos.findUserById(accountId, true);
    const room: Room = await this.roomRepos.findById(roomId, true);

    if (room.type !== RoomType.SMART) {
      throw new BaseException("Can't report this kind of room");
    }

    const partner: User = await room.getParterOf(account);

    await this.accountGw.reportUser(account.refId, new AccountReportDto(partner.refId, reason));
  }
}

export default RoomService;
