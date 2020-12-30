import { CommandBus } from 'node-cqrs';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import container from '../../../container';
import { RoomEntity } from '../../domain/entities/rooms.entity';
import { RoomType } from '../../domain/enums/roomType.enum';
import { Room } from '../../domain/models/rooms.model';
import { IRoomRepository, RoomRepository } from '../../domain/repositories/room.repos';

class RoomService {
  private commandBus: CommandBus;
  private roomRepos: IRoomRepository;
  private userRepos: UserRepository;

  constructor() {
    this.commandBus = container.commandBus;
    this.roomRepos = new RoomRepository();
    this.userRepos = new UserRepository();
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
}

export default RoomService;
