import { getConnection } from 'typeorm';
import { MatchEntity } from '../entities/matches.entity';
import { Match } from '../models/matches.model';

export interface IMatchRepository {
  save: (match: any) => Promise<Match>;
  // async function save(match):Promise<Match>
}

export class MatchRepository implements IMatchRepository {
  private model = MatchEntity;

  public async save(match: any): Promise<Match> {
    const manager = getConnection().manager;

    return await manager.save(this.model, match);
  }
}
