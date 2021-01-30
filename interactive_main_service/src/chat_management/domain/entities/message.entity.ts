import { IsNotEmpty } from 'class-validator';
import { Column, CreateDateColumn, Entity, getRepository, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { Message } from '../models/message.model';
import { MediaMessageEntity } from './media_messages.entity';
import { RoomEntity } from './rooms.entity';
import { UserRoomEntity } from './user_rooms.entity';

@Entity('cm_messages')
export class MessageEntity extends GenericEntity implements Message {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'sender_id' })
  senderId: string;

  @Column({ name: 'room_id' })
  roomId: string;

  @Column()
  @IsNotEmpty()
  content: string;

  constructor(sender: any, room: any, content: string) {
    super();

    this.senderId = sender?.id;
    this.roomId = room?.id;
    this.content = content;

    this.triggerCreate();
  }

  public async getMedias(): Promise<Array<MediaMessageEntity>> {
    const mediaMsgRepos = getRepository(MediaMessageEntity);
    const mediaMsgs = await mediaMsgRepos
      .createQueryBuilder('media_msg')
      .where('media_msg.message_id = :message_id', { message_id: this.id })
      .getMany();
    return await Promise.all(mediaMsgs);
  }
}
