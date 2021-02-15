import { IsNotEmpty } from 'class-validator';
import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { ReactSmartRoom, ReactType } from '../models/react_smart_rooms.model';
import { RoomEntity } from './rooms.entity';
import { UserRoomEntity } from './user_rooms.entity';

@Entity('cm_react_smart_rooms')
export class ReactSmartRoomEntity extends GenericEntity implements ReactSmartRoom {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'room_id' })
  roomId: string;

  @Column({ name: 'sender_id' })
  senderId: string;

  @Column()
  @IsNotEmpty()
  status: number;

  constructor(roomId: string, senderRoomId: string, status: ReactType) {
    super();

    this.roomId = roomId;
    this.senderId = senderRoomId;
    this.status = status;

    this.triggerCreate();
  }
}
