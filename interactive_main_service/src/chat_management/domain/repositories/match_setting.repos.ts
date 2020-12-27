import { getConnection } from 'typeorm';
import BaseException from '../../../common/exceptions/BaseException';
import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { MatchSettingEntity } from '../entities/match_settings.entity';
import { MatchSetting } from '../models/match_settings.model';

export interface IMatchSettingRepository extends IBaseRepository {
  findMatchSettingByAccountId(accountId: string, raiseException: boolean): Promise<MatchSetting>;
}

export class MatchSettingRepository extends BaseRepository implements IMatchSettingRepository {
  protected model = MatchSettingEntity;
  async findMatchSettingByAccountId(accountId: string, raiseException: boolean): Promise<MatchSetting> {
    const manager = getConnection().manager;

    const matchSetting: MatchSetting = await manager.findOne(this.model, { where: { accountId: accountId } });

    if (raiseException && !matchSetting) {
      throw new BaseException(`Can't find match setting for accountId: ${accountId}`);
    }

    return matchSetting;
  }
}
