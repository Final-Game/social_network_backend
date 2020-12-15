import { IsNotEmpty } from 'class-validator';
import { Entity, PrimaryGeneratedColumn, Column, Unique, CreateDateColumn, UpdateDateColumn, OneToMany } from 'typeorm';
import { Message } from '../models/message.model';
import { Room } from '../models/rooms.model';
import { MessageEntity } from './message.entity';
import { UserRoomEntity } from './user_rooms.entity';

@Entity('cm_rooms')
export class RoomEntity implements Room {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'general_name' })
  @IsNotEmpty()
  generalName: string;

  @Column({ name: 'created_at' })
  // @CreateDateColumn()
  createdAt: Date;

  @Column({ name: 'updated_at' })
  // @UpdateDateColumn()
  updatedAt: Date;

  @OneToMany(type => UserRoomEntity, userRoom => userRoom.room)
  userRooms: UserRoomEntity[];

  @OneToMany(type => MessageEntity, message => message.room)
  @IsNotEmpty()
  messages: Message[];
}
