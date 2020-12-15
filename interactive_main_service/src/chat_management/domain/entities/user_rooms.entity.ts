import { IsNotEmpty } from 'class-validator';
import { Column, CreateDateColumn, Entity, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { UserRoom } from '../models/user_rooms.model';
import { RoomEntity } from './rooms.entity';

@Entity('cm_user_rooms')
export class UserRoomEntity implements UserRoom {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'account_id' })
  @IsNotEmpty()
  accountId: string;

  @Column({ name: 'nick_name' })
  @IsNotEmpty()
  nickName: string;

  @ManyToOne(type => RoomEntity, room => room.userRooms)
  @IsNotEmpty()
  room: RoomEntity;

  @Column({ name: 'created_at' })
  @CreateDateColumn()
  createdAt: Date;

  @Column({ name: 'updated_at' })
  @UpdateDateColumn()
  updatedAt: Date;
}
