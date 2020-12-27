import { IsNotEmpty } from 'class-validator';
import { Column, CreateDateColumn, Entity, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { Message } from '../models/message.model';
import { RoomEntity } from './rooms.entity';
import { UserRoomEntity } from './user_rooms.entity';

@Entity('cm_messages')
export class MessageEntity implements Message {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @ManyToOne(type => UserRoomEntity)
  sender: UserRoomEntity;

  @ManyToOne(type => RoomEntity, room => room.messages)
  room: RoomEntity;

  @Column()
  @IsNotEmpty()
  content: string;

  @Column({ name: 'created_at' })
  @CreateDateColumn()
  createdAt: Date;

  @Column({ name: 'updated_at' })
  @UpdateDateColumn()
  updatedAt: Date;
}
