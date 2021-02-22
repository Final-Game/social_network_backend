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
import { RoomType } from '../enums/roomType.enum';
import { Message } from '../models/message.model';
import { ReactType } from '../models/react_smart_rooms.model';
import { Room } from '../models/rooms.model';
import { UserRoom } from '../models/user_rooms.model';
import { MessageEntity } from './message.entity';
import { ReactSmartRoomEntity } from './react_smart_rooms.entity';
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
    return await Promise.all(userRooms.map(item => item.accountId));
  }

  public async getMembers(): Promise<Array<any>> {
    const accountRoomIds = await this.getMemberIds();
    const manager = getConnection().manager;

    return await Promise.all(accountRoomIds.map(async accountId => await manager.findOne(UserEntity, { where: { id: accountId } })));
  }
  public async getParterOf(account: any): Promise<any> {
    const members: Array<any> = await this.getMembers();

    const partners: Array<any> = members.filter(item => item.id !== account.id);

    if (partners.length > 0) {
      return partners[0];
    }

    return null;
  }

  public async getLastestMsg(): Promise<any> {
    const msgList = await this.getMsgs();
    return msgList[0];
  }

  public async getMsgs(): Promise<Array<Message>> {
    const msgRepos = getRepository(MessageEntity);

    return await msgRepos.find({ where: { roomId: this.id, senderId: Not(IsNull()) }, order: { createdAt: 'DESC' } });
  }

  public isSmartRoomAlive(): boolean {
    const threshTime = new Date(this.createdAt.getTime() + 4 * 60 * 1000); // delay a minute for setup

    return this.type == RoomType.SMART_PENDING && new Date() <= threshTime;
  }

  public async canContinueChatNormal(): Promise<boolean> {
    const manager = getConnection().manager;
    const members = await this.getMembers();

    for (let idx = 0; idx < members.length; idx++) {
      const _mem = members[idx];

      const userRoom: UserRoom = await _mem.getUserRefRoom(this);
      const reaction = await manager.findOne(ReactSmartRoomEntity, {
        where: {
          senderId: userRoom.id,
          roomId: this.id,
          status: ReactType.LOVE,
        },
      });

      if (!reaction) {
        return false;
      }
    }
    return true;
  }

  public makeRoomNormalChatForSmartChat(): void {
    this.type = RoomType.SMART;

    this.triggerUpdate();
  }

  public canChatNormal(): boolean {
    return [RoomType.MATCH, RoomType.NORMAL, RoomType.SMART].includes(this.type);
  }
}
