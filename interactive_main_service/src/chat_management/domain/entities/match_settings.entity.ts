import { Column, PrimaryGeneratedColumn } from 'typeorm';
import { MatchSetting } from '../models/match_settings.model';

export class MatchSettingEntity implements MatchSetting {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'account_id' })
  accountId: string;

  @Column({ name: 'max_distance' })
  maxDistance: number;

  @Column({ name: 'min_age' })
  minAge: number;

  @Column({ name: 'max_age' })
  maxAge: number;

  @Column({ name: 'target_gender' })
  targetGender: number;

  @Column({ name: 'created_at' })
  createdAt: Date;

  @Column({ name: 'updated_at' })
  updatedAt: Date;
}
