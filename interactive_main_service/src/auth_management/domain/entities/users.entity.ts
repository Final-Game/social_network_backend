import {
  Entity,
  PrimaryGeneratedColumn,
  Column,
  Unique,
  CreateDateColumn,
  UpdateDateColumn,
  AfterInsert,
  BeforeUpdate,
  BeforeInsert,
  getConnection,
  getRepository,
} from 'typeorm';
import { IsNotEmpty } from 'class-validator';
import { User } from '../models/users.model';
import { UserRoomEntity } from '../../../chat_management/domain/entities/user_rooms.entity';
import { UserRoom } from '../../../chat_management/domain/models/user_rooms.model';
import { RoomType } from '../../../chat_management/domain/enums/roomType.enum';
import { MatchSettingEntity } from '../../../chat_management/domain/entities/match_settings.entity';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { MatchSetting } from '../../../chat_management/domain/models/match_settings.model';
import { dateToString, stringToDate } from '../../../common/utils/util';
import { ConnectManager } from '../../../common/repos/transaction';
import { ReactSmartRoomEntity } from '../../../chat_management/domain/entities/react_smart_rooms.entity';
import { ReactSmartRoom, ReactType } from '../../../chat_management/domain/models/react_smart_rooms.model';

@Entity('cm_account_mappers')
export class UserEntity extends GenericEntity implements User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'full_name' })
  fullName: string;

  @Column()
  avatar: string;

  @Column({ name: 'birth_date' })
  birthDate: string;

  @Column()
  gender: number;

  @Column()
  bio: string;

  @Column()
  address: string;

  @Column()
  job: string;

  @Column()
  reason: string;

  @Column({ name: 'ref_id' })
  @IsNotEmpty()
  refId: string;

  constructor(refId: string) {
    super();

    this.refId = refId;

    this.triggerCreate();
  }

  public async updateData(
    fullName: string,
    avatar: string,
    birthDate: Date,
    gender: number,
    bio: string,
    address: string,
    job: string,
    reason: string,
  ) {
    this.fullName = fullName;
    this.avatar = avatar;
    this.birthDate = dateToString(birthDate);
    this.gender = gender;
    this.bio = bio;
    this.address = address;
    this.job = job;
    this.reason = reason;

    this.triggerUpdate();
  }

  public async getRooms(): Promise<Array<any>> {
    const userRoomRepos = getRepository(UserRoomEntity);
    const userRooms = await userRoomRepos
      .createQueryBuilder('user_room')
      .where('user_room.account_id = :account_id', { account_id: this.id })
      .getMany();

    return await Promise.all(userRooms.map(async item => await item.getRoom()));
  }

  public async getCurrentSmartRooms(): Promise<Array<any>> {
    const userRoomRepos = getRepository(UserRoomEntity);
    const userRooms = await userRoomRepos
      .createQueryBuilder('user_room')
      .where('user_room.account_id = :account_id', { account_id: this.id })
      .getMany();

    return (await Promise.all(userRooms.map(async ur => await ur.getRoom()))).filter(room => room.canChatNormal());
  }

  public async isReadyForNewSmartRoom(): Promise<boolean> {
    const currentSmartRooms = await this.getCurrentSmartRooms();

    return !(currentSmartRooms && currentSmartRooms.length > 0);
  }

  public async joinRoom(room: any): Promise<void> {
    let userRoom: UserRoom = await this.getUserRefRoom(room);

    if (!userRoom) {
      userRoom = new UserRoomEntity(this.id, room.id);
      userRoom.updateNickName(this.fullName);
      await ConnectManager.getManager().save(UserRoomEntity, userRoom);
    }
  }

  public async reactSmartRoom(room: any): Promise<void> {
    const userRoom: UserRoom = await this.getUserRefRoom(room);

    if (userRoom) {
      const reactSmartRoom: ReactSmartRoom = new ReactSmartRoomEntity(room.id, userRoom.id, ReactType.LOVE);
      ConnectManager.getManager().save(ReactSmartRoomEntity, reactSmartRoom);
    }
  }

  public async getUserRefRoom(room: any): Promise<any> {
    const userRoomRepos = getRepository(UserRoomEntity);
    return await userRoomRepos.findOne({ where: { accountId: this.id, roomId: room.id } });
  }

  public async getMatchSetting(): Promise<any> {
    const matchSettingRepos = getRepository(MatchSettingEntity);

    return await matchSettingRepos.findOne({ where: { accountId: this.id } });
  }

  public async canMatch(partner: User): Promise<boolean> {
    const matchSetting: MatchSetting = (await this.getMatchSetting()) || MatchSettingEntity.DefaultMatchSetting();

    const partnerAge: number = partner.getAge();
    if (partnerAge && (partnerAge > matchSetting.maxAge || partnerAge < matchSetting.minAge)) {
      return false;
    }

    if (matchSetting.targetGender && matchSetting.targetGender != partner.gender) {
      return false;
    }

    return true;
  }

  public getAge(): number {
    const today = new Date();
    const birthDate = this.getBirthDate();

    if (!birthDate) {
      return 0;
    }

    let age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  }

  public getBirthDate(): Date {
    return stringToDate(this.birthDate);
  }
}
