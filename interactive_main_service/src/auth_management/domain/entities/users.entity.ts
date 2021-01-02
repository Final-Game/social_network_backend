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

@Entity('cm_account_mappers')
export class UserEntity extends GenericEntity implements User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'full_name' })
  fullName: string;

  @Column()
  avatar: string;

  @Column({ name: 'birth_date' })
  birthDate: Date;

  @Column()
  gender: number;

  @Column({ name: 'ref_id' })
  refId: string;

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

    return (await Promise.all(userRooms.map(async ur => await ur.getRoom()))).filter(item => item.type == RoomType.SMART);
  }

  public async joinRoom(room: any): Promise<void> {
    const userRoom: UserRoom = new UserRoomEntity(this.id, room.id);
    userRoom.updateNickName(this.fullName);
    await getRepository(UserRoomEntity).save(userRoom);

    return;
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
    const birthDate = this.birthDate;

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
}
