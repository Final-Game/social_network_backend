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

@Entity('uc_accounts')
export class UserEntity implements User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  @IsNotEmpty()
  username: string;

  @Column()
  @IsNotEmpty()
  password: string;

  @Column()
  type: number;

  @Column({ name: 'created_at' })
  // @CreateDateColumn()
  createdAt: Date;

  @Column({ name: 'updated_at' })
  // @UpdateDateColumn()
  updatedAt: Date;

  @BeforeUpdate()
  updateEntity() {
    this.updatedAt = new Date();
  }

  @BeforeInsert()
  createEntity() {
    this.createdAt = new Date();
    this.updatedAt = new Date();
  }

  public async getRooms(): Promise<Array<any>> {
    const userRoomRepos = getRepository(UserRoomEntity);
    const userRooms = await userRoomRepos
      .createQueryBuilder('user_room')
      .where('user_room.account_id = :account_id', { account_id: this.id })
      .getMany();

    return await Promise.all(userRooms.map(async item => await item.getRoom()));
  }

  public async joinRoom(room: any): Promise<void> {
    const userRoom: UserRoom = new UserRoomEntity(this.id, room.id);
    userRoom.updateNickName(this.username);
    await getRepository(UserRoomEntity).save(userRoom);

    return;
  }

  public async getUserRefRoom(room: any): Promise<any> {
    const userRoomRepos = getRepository(UserRoomEntity);
    return await userRoomRepos.findOne({ where: { accountId: this.id, roomId: room.id } });
  }
}
