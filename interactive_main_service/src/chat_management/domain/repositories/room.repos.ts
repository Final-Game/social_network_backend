import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { RoomEntity } from '../entities/rooms.entity';

export type IRoomRepository = IBaseRepository;

export class RoomRepository extends BaseRepository implements IRoomRepository {
  protected model = RoomEntity;
}
