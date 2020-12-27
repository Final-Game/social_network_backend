import { IsNotEmpty } from 'class-validator';
import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';
import { Match } from '../models/matches.model';

@Entity('cm_matches')
export class MatchEntity implements Match {
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
}
