import { AbstractAggregate } from 'node-cqrs';
import BaseException from '../../../common/exceptions/BaseException';
import { RunInTransaction } from '../../../common/repos/transaction';
import { logger } from '../../../common/utils/logger';
import { MatchEntity } from '../entities/matches.entity';
import { MatchSettingEntity } from '../entities/match_settings.entity';
import { Gender, getGender } from '../enums/gender.enum';
import { MatchStatus } from '../enums/matchStatus.enum';
import { Match } from '../models/matches.model';
import { MatchSetting } from '../models/match_settings.model';
import { IMatchRepository, MatchRepository } from '../repositories/match.repos';
import { IMatchSettingRepository, MatchSettingRepository } from '../repositories/match_setting.repos';
import { ICreateMatchPayload } from './payloads/createMatch.payload';
import { UpdateMatchSettingPayload } from './payloads/updateMatchSetting.payload';

class MatchAggregateState {
  matchCreatedEvent(event) {
    logger.info(`Create Match Event is created: ${JSON.stringify(event)}`);
  }

  matchSettingUpdatedEvent(event) {
    logger.info(`Update Match Setting Event is created ${JSON.stringify(event)}`);
  }
}

class MatchAggregate extends AbstractAggregate {
  [x: string]: any;
  static get handles() {
    return ['createMatchCommand', 'updateMatchSettingCommand'];
  }

  private matchRepos: IMatchRepository;
  private matchSettingRepos: IMatchSettingRepository;

  /**
   * Creates an instance of UserAggregate
   *
   * @param {object} options
   * @param {string} options.id - aggregate ID
   * @param {object[]} options.events - past aggregate events
   */
  constructor({ id, events }) {
    super({
      id,
      events,
      state: new MatchAggregateState(),
    });
    this.matchRepos = new MatchRepository();
    this.matchSettingRepos = new MatchSettingRepository();
  }

  async createMatchCommand(_payload: ICreateMatchPayload) {
    const status: number = _payload.dto.status;
    if (!Object.values(MatchStatus).includes(status)) {
      throw new BaseException(`Can't react with invalid status`);
    }
    const senderId: string = _payload.senderId;
    const receiverId: string = _payload.dto.receiverId;

    const existedMatch: Match = await this.matchRepos.findMatchBySenderIdAndReceiverId(senderId, receiverId, false);

    let createdMatch: Match = null;

    await RunInTransaction(async _ => {
      if (existedMatch) {
        if (existedMatch.status == MatchStatus.CLOSE && status != MatchStatus.CLOSE) {
          existedMatch.updateStatus(status);

          this.matchRepos.update(existedMatch.id, existedMatch);
        }
        return;
      }

      const match: Match = new MatchEntity(_payload.senderId, _payload.dto.receiverId, _payload.dto.status);
      createdMatch = await this.matchRepos.save(match);
    });

    this.emit('matchCreatedEvent', {
      id: createdMatch.id,
      senderId: createdMatch.senderId,
      receiverId: createdMatch.receiverId,
      status: createdMatch.status,
    });
  }

  async updateMatchSettingCommand(_payload: UpdateMatchSettingPayload) {
    const accountId: string = _payload.accountId;
    const { targetGender, maxAge, maxDistance, minAge } = _payload.data;

    const gender = getGender(targetGender);

    let matchSetting: MatchSetting = await this.matchSettingRepos.findMatchSettingByAccountId(accountId, false);

    await RunInTransaction(async _ => {
      if (!matchSetting) {
        matchSetting = new MatchSettingEntity(accountId, gender, maxDistance, minAge, maxAge);
        await this.matchSettingRepos.save(matchSetting);
      } else {
        matchSetting.updateData(gender, maxAge, minAge, maxDistance);
        await this.matchSettingRepos.update(matchSetting.id, matchSetting);
      }
    });

    this.emit('matchSettingUpdatedEvent', { id: matchSetting.id, accountId: accountId });
  }
}

export default MatchAggregate;
