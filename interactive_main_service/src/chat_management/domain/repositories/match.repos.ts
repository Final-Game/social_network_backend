import { getConnection } from 'typeorm';
import BaseException from '../../../common/exceptions/BaseException';
import { BaseRepository, IBaseRepository } from '../../../common/repos/base.repos';
import { MatchEntity } from '../entities/matches.entity';
import { Match } from '../models/matches.model';

export interface IMatchRepository extends IBaseRepository {
  findMatchBySenderIdAndReceiverId(senderId: string, receiverId: string, raiseException: boolean);
}

export class MatchRepository extends BaseRepository implements IMatchRepository {
  protected model = MatchEntity;

  async findMatchBySenderIdAndReceiverId(senderId: string, receiverId: string, raiseException = false): Promise<Match> {
    const manager = getConnection().manager;

    const match: Match = await manager.findOne(this.model, { where: { senderId: senderId, receiverId: receiverId } });

    if (raiseException && !match) {
      throw new BaseException(`Can't find match for sender ${senderId} and receiver ${receiverId}`);
    }
    return match;
  }
}
