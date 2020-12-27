import { Column, CreateDateColumn, Entity, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { MediaMessage } from '../models/media_messages.model';
import { MessageEntity } from './message.entity';

@Entity('cm_media_messages')
export class MediaMessageEntity implements MediaMessage {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @ManyToOne(type => MessageEntity)
  message: MessageEntity;

  @Column({ name: 'media_url' })
  mediaUrl: string;

  @Column()
  type: number;

  @Column({ name: 'created_at' })
  @CreateDateColumn()
  createdAt: Date;

  @Column({ name: 'updated_at' })
  @UpdateDateColumn()
  updatedAt: Date;
}
