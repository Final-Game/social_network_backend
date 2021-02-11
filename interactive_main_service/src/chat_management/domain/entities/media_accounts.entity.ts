import { Column, CreateDateColumn, Entity, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm';
import { GenericEntity } from '../../../common/entities/generic.entity';
import { MediaAccount } from '../models/media_accounts.model';

@Entity('cm_media_accounts')
export class MediaAccountEntity extends GenericEntity implements MediaAccount {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ name: 'account_id' })
  accountId: string;

  @Column({ name: 'media_url' })
  mediaUrl: string;

  @Column()
  type: number;

  constructor(accountId: string, mediaUrl: string, type: number) {
    super();

    this.accountId = accountId;
    this.mediaUrl = mediaUrl;
    this.type = type;

    this.triggerCreate();
  }
}
