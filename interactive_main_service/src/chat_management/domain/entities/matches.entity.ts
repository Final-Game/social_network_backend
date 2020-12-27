import { IsNotEmpty } from 'class-validator';
import { BeforeInsert, BeforeUpdate, Column, CreateDateColumn, Entity, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { Match } from '../models/matches.model';

@Entity('cm_matches')
export class MatchEntity extends GenericEntity implements Match {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'sender_id' })
  @IsNotEmpty()
  senderId: string;

  @Column({ name: 'receiver_id' })
  @IsNotEmpty()
  receiverId: string;

  @Column()
  @IsNotEmpty()
  status: number;

  @Column({ name: 'created_at' })
  createdAt: Date;

  @Column({ name: 'updated_at' })
  updatedAt: Date;

  constructor(senderId: string, receiverId: string, status: number) {
    super();

    this.senderId = senderId;
    this.receiverId = receiverId;
    this.status = status;

    this.triggerCreate();
  }
}
