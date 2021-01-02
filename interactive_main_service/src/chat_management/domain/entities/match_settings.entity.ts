import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { MatchSetting } from '../models/match_settings.model';

@Entity('cm_match_settings')
export class MatchSettingEntity extends GenericEntity implements MatchSetting {
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

  constructor(accountId: string, targetGender: number, maxDistance = 0, minAge = 18, maxAge = 21) {
    super();

    this.accountId = accountId;
    this.targetGender = targetGender;
    this.maxDistance = maxDistance;
    this.maxAge = maxAge;
    this.minAge = minAge;

    this.triggerCreate();
  }

  public updateData(targetGender: number, maxAge: number, minAge: number, maxDistance: number): any {
    this.targetGender = targetGender;
    this.maxAge = maxAge;
    this.minAge = minAge;
    this.maxDistance = maxDistance;

    this.triggerUpdate();
  }

  public static DefaultMatchSetting(): any {
    return new MatchSettingEntity(null, null, 0, 18, 21);
  }
}
