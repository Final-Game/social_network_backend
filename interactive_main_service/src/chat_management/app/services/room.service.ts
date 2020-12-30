import { CommandBus } from 'node-cqrs';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import BaseException from '../../../common/exceptions/BaseException';
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
    const account = await this.userRepos.findUserById(accountId, true);
    const receiver = await this.userRepos.findUserById(receiverId, true);

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

    // Create new room chat
    room = new RoomEntity(RoomType.NORMAL);
    room = await this.roomRepos.save(room);
    await account.joinRoom(room);
    await receiver.joinRoom(room);

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
}

export default RoomService;
