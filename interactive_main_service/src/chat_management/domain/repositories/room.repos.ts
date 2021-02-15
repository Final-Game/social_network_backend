import { getConnection } from 'typeorm';
import { User } from '../../../auth_management/domain/models/users.model';
import BaseException from '../../../common/exceptions/BaseException';
import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { MessageEntity } from '../entities/message.entity';
import { ReactSmartRoomEntity } from '../entities/react_smart_rooms.entity';
import { RoomEntity } from '../entities/rooms.entity';
import { UserRoomEntity } from '../entities/user_rooms.entity';
import { Room } from '../models/rooms.model';
import { IMessageRepository, MessageRepository } from './message.repos';

export interface IRoomRepository extends IBaseRepository {
  findRoomByTwoPartners: (partnerA: User, partnerB: User) => Promise<Room>;
}

export class RoomRepository extends BaseRepository implements IRoomRepository {
  protected model = RoomEntity;

  private msgRepos: IMessageRepository;

  constructor() {
    super();

    this.msgRepos = new MessageRepository();
  }

  public async findRoomByTwoPartners(partnerA: User, partnerB: User, raiseException = false): Promise<Room | null> {
    const availableRoomsOfPartnerA: Array<Room> = await partnerA.getRooms();
    const availableRoomsOfPartnerB: Array<Room> = await partnerB.getRooms();

    for (let idx = 0; idx < availableRoomsOfPartnerA.length; idx++) {
      const room: Room = availableRoomsOfPartnerA[idx];

      if (availableRoomsOfPartnerB.some(r => r.id == room.id)) {
        return room;
      }
    }

    if (raiseException) {
      throw new BaseException("Don't have room between two partners.");
    }

    return null;
  }

  public async delete(roomId: string): Promise<void> {
    const manager = getConnection().manager;

    // delete remove user room related
    await this.msgRepos.removeMsgsInRoom(roomId);
    await manager.delete(ReactSmartRoomEntity, { roomId: roomId });
    await manager.delete(UserRoomEntity, { roomId: roomId });

    await manager.delete(this.model, roomId);
  }
}
