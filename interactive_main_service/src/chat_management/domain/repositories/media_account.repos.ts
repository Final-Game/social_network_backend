import { getConnection } from 'typeorm';
import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { ConnectManager } from '../../../common/repos/transaction';
import { MediaAccountEntity } from '../entities/media_accounts.entity';

export interface IMediaAccountRepository extends IBaseRepository {
  removeMediasOfAccount: (accountId: string) => Promise<void>;
  queryMediasByAccountId: (accountId: string) => Promise<Array<MediaAccountEntity>>;
}

export class MediaAccountRepository extends BaseRepository implements IMediaAccountRepository {
  protected model = MediaAccountEntity;

  public async removeMediasOfAccount(accountId: string): Promise<void> {
    const manager = ConnectManager.getManager();

    await manager.delete(this.model, { accountId: accountId });
  }

  public async queryMediasByAccountId(accountId: string): Promise<Array<MediaAccountEntity>> {
    const manager = getConnection().manager;

    const medias: Array<MediaAccountEntity> = await manager.find(this.model, { where: { accountId: accountId } });
    return medias;
  }
}
