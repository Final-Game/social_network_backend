import { getConnection } from 'typeorm';
import BaseException from '../../../common/exceptions/BaseException';
import { MatchEntity } from '../entities/matches.entity';
import { Match } from '../models/matches.model';

export interface IMatchRepository {
  save: (match: any) => Promise<Match>;
  update: (matchId: string, data: any) => Promise<void>;
  findMatchBySenderIdAndReceiverId(senderId: string, receiverId: string, raiseException: boolean);
  // async function save(match):Promise<Match>
}

export class MatchRepository implements IMatchRepository {
  private model = MatchEntity;

  public async save(match: any): Promise<Match> {
    const manager = getConnection().manager;

    return await manager.save(this.model, match);
  }

  public async update(matchId: string, data: any): Promise<void> {
    const manager = getConnection().manager;

    await manager.update(this.model, matchId, data);
  }

  async findMatchBySenderIdAndReceiverId(senderId: string, receiverId: string, raiseException = false): Promise<Match> {
    const manager = getConnection().manager;

    const match: Match = await manager.findOne(this.model, { where: { senderId: senderId, receiverId: receiverId } });

    if (raiseException && !match) {
      throw new BaseException(`Can't find match for sender ${senderId} and receiver ${receiverId}`);
    }
    return match;
  }
}
