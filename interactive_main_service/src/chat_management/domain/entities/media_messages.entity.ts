import { Column, CreateDateColumn, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { MediaMessage } from '../models/media_messages.model';
import { MessageEntity } from './message.entity';

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
