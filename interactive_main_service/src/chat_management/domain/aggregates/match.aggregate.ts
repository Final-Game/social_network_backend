import { AbstractAggregate } from 'node-cqrs';
import BaseException from '../../../common/exceptions/BaseException';
import { logger } from '../../../common/utils/logger';
import { MatchEntity } from '../entities/matches.entity';
import { MatchStatus } from '../enums/matchStatus.enum';
import { Match } from '../models/matches.model';
import { IMatchRepository, MatchRepository } from '../repositories/match.repos';
import { ICreateMatchPayload } from './payloads/createMatch.payload';

class MatchAggregateState {
  matchCreatedEvent(event) {
    logger.info(`Create Match Event is created: ${JSON.stringify(event)}`);
  }
}

class MatchAggregate extends AbstractAggregate {
  [x: string]: any;
  static get handles() {
    return ['createMatchCommand'];
  }

  private matchRepos: IMatchRepository;

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
  }

  async createMatchCommand(_payload: ICreateMatchPayload) {
    const status: number = _payload.dto.status;
    if (!Object.values(MatchStatus).includes(status)) {
      throw new BaseException(`Can't react with invalid status`);
    }
    const senderId: string = _payload.senderId;
    const receiverId: string = _payload.dto.receiverId;

    const existedMatch: Match = await this.matchRepos.findMatchBySenderIdAndReceiverId(senderId, receiverId, false);

    if (existedMatch) {
      if (existedMatch.status == MatchStatus.CLOSE) {
        existedMatch.status = status;

        this.matchRepos.update(existedMatch.id, { status: status });
      }
      return;
    }

    const match: Match = new MatchEntity(_payload.senderId, _payload.dto.receiverId, _payload.dto.status);
    const createdMatch: Match = await this.matchRepos.save(match);

    this.emit('matchCreatedEvent', {
      id: createdMatch.id,
      senderId: createdMatch.senderId,
      receiverId: createdMatch.receiverId,
      status: createdMatch.status,
    });
  }
}

export default MatchAggregate;
