import { IsNotEmpty } from 'class-validator';
import { Column, CreateDateColumn, Entity, getRepository, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { UserRoom } from '../models/user_rooms.model';
import { RoomEntity } from './rooms.entity';

@Entity('cm_user_rooms')
export class UserRoomEntity extends GenericEntity implements UserRoom {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'account_id' })
  @IsNotEmpty()
  accountId: string;

  @Column({ name: 'nick_name' })
  @IsNotEmpty()
  nickName: string;

  @Column({ name: 'room_id' })
  // @ManyToOne(type => RoomEntity, room => room.userRooms)
  @IsNotEmpty()
  roomId: string;

  constructor(accountId: string, roomId: string) {
    super();

    this.accountId = accountId;
    this.roomId = roomId;

    this.triggerCreate();
  }

  public async getRoom(): Promise<RoomEntity> {
    const roomRepos = getRepository(RoomEntity);
    return await roomRepos.findOne(this.roomId);
  }

  public updateNickName(nickName: string): void {
    this.nickName = nickName;
  }
}
