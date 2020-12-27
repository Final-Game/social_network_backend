import { IsNotEmpty } from 'class-validator';
import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { ReactSmartRoom } from '../models/react_smart_rooms.model';
import { RoomEntity } from './rooms.entity';
import { UserRoomEntity } from './user_rooms.entity';

@Entity('cm_react_smart_rooms')
export class ReactSmartRoomEntity implements ReactSmartRoom {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @ManyToOne(type => RoomEntity)
  room: RoomEntity;

  @ManyToOne(type => UserRoomEntity)
  sender: UserRoomEntity;

  @Column()
  @IsNotEmpty()
  status: number;

  @Column({ name: 'created_at' })
  createdAt: Date;

  @Column({ name: 'updated_at' })
  updatedAt: Date;
}
