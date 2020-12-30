import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { MessageEntity } from '../entities/message.entity';

export type IMessageRepository = IBaseRepository;

export class MessageRepository extends BaseRepository implements IMessageRepository {
  protected model = MessageEntity;
}
