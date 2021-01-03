import { getConnection } from 'typeorm';
import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { MessageEntity } from '../entities/message.entity';

export interface IMessageRepository extends IBaseRepository {
  removeMsgsInRoom: (roomId: string) => Promise<void>;
}

export class MessageRepository extends BaseRepository implements IMessageRepository {
  protected model = MessageEntity;

  public async removeMsgsInRoom(roomId: string): Promise<void> {
    const manager = getConnection().manager;

    await manager.delete(this.model, { roomId: roomId });
  }
}
