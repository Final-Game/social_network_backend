import { CommandBus } from 'node-cqrs';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import { logger } from '../../../common/utils/logger';
import container from '../../../container';
import { MatchSettingEntity } from '../../domain/entities/match_settings.entity';
import { Gender } from '../../domain/enums/gender.enum';
import { Match } from '../../domain/models/matches.model';
import { MatchSetting } from '../../domain/models/match_settings.model';
import { IMatchRepository, MatchRepository } from '../../domain/repositories/match.repos';
import { IMatchSettingRepository, MatchSettingRepository } from '../../domain/repositories/match_setting.repos';
import { CreateMatchDto } from '../dtos/matches.dto';
import { MatchSettingDto } from '../dtos/match_setting.dto';

class MatchService {
  private commandBus: CommandBus;
  private matchRepos: IMatchRepository;
  private matchSettingRepos: IMatchSettingRepository;
  private userRepos: UserRepository;

  constructor() {
    this.commandBus = container.commandBus;
    this.matchRepos = new MatchRepository();
    this.userRepos = new UserRepository();
    this.matchSettingRepos = new MatchSettingRepository();
  }

  public async createMatch(data: CreateMatchDto): Promise<Match> {
    const sender = await this.userRepos.findUserById(data.accountId, true);
    const receiver = await this.userRepos.findUserById(data.dto.receiverId, true);

    const payload = {
      senderId: sender.id,
      dto: {
        receiverId: receiver.id,
        status: data.dto.status,
      },
    };

    data = await this.commandBus.send('createMatchCommand', undefined, { payload });
    container.eventStore.once('matchCreatedEvent', event => {
      logger.info(`Match aggregate created with ID ${event.aggregateId}`);
    });

    console.log(data);
    return;
  }

  public async getAccountMatchSetting(accountId: string): Promise<MatchSetting> {
    const account = await this.userRepos.getOrCreateAccountByBaseAccountId(accountId);

    let matchSetting: MatchSetting = await this.matchSettingRepos.findMatchSettingByAccountId(account.id, false);

    if (!matchSetting) {
      matchSetting = new MatchSettingEntity(account.id, Gender.UN_KNOWN);

      matchSetting = await this.matchSettingRepos.save(matchSetting);
    }

    return matchSetting;
  }

  public async updateAccountMatchSetting(accountId: string, data: MatchSettingDto) {
    const payload = {
      accountId: accountId,
      data: data,
    };

    data = await this.commandBus.send('updateMatchSettingCommand', undefined, { payload });

    container.eventStore.once('matchSettingUpdatedEvent', event => {
      logger.info(`Match aggregate created with ID ${event.aggregateId}`);
    });

    console.log(data);
  }
}

export default MatchService;
