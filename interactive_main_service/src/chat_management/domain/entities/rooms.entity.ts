import { IsNotEmpty } from 'class-validator';
import {
  Entity,
  PrimaryGeneratedColumn,
  Column,
  Unique,
  CreateDateColumn,
  UpdateDateColumn,
  OneToMany,
  getRepository,
  Not,
  IsNull,
  getConnection,
} from 'typeorm';
import { UserEntity } from '../../../auth_management/domain/entities/users.entity';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { Message } from '../models/message.model';
import { Room } from '../models/rooms.model';
import { MessageEntity } from './message.entity';
import { UserRoomEntity } from './user_rooms.entity';

@Entity('cm_rooms')
export class RoomEntity extends GenericEntity implements Room {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'general_name' })
  @IsNotEmpty()
  generalName: string;

  @Column()
  type: number;

  // @OneToMany(type => UserRoomEntity, userRoom => userRoom.room)
  // userRooms: UserRoomEntity[];

  // @OneToMany(type => MessageEntity, message => message.room)
  // @IsNotEmpty()
  // messages: Message[];

  constructor(type: number) {
    super();

    this.type = type;
    this.generalName = 'Private';

    this.triggerCreate();
  }

  public async getMemberIds(): Promise<Array<any>> {
    const userRoomsRepos = getRepository(UserRoomEntity);
    const userRooms = await userRoomsRepos.createQueryBuilder('user_room').where('user_room.room_id = :room_id', { room_id: this.id }).getMany();
    return userRooms.map(item => item.accountId);
  }

  public async getMembers(): Promise<Array<any>> {
    const accountIds = await Promise.all(await this.getMemberIds());
    const manager = getConnection().manager;

    return accountIds.map(async accountId => await manager.findOne(UserEntity, { where: { id: accountId } }));
  }

  public async getLastestMsg(): Promise<any> {
    const msgList = await this.getMsgs();
    return msgList[0];
  }

  public async getMsgs(): Promise<Array<Message>> {
    const msgRepos = getRepository(MessageEntity);

    return await msgRepos.find({ where: { roomId: this.id, senderId: Not(IsNull()) }, order: { createdAt: 'DESC' } });
  }
}
