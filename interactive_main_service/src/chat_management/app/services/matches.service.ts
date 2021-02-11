import { CommandBus } from 'node-cqrs';
import { User } from '../../../auth_management/domain/models/users.model';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import { logger } from '../../../common/utils/logger';
import container from '../../../container';
import { MatchSettingEntity } from '../../domain/entities/match_settings.entity';
import { Gender } from '../../domain/enums/gender.enum';
import { Match } from '../../domain/models/matches.model';
import { MatchSetting } from '../../domain/models/match_settings.model';
import { MediaAccount } from '../../domain/models/media_accounts.model';
import { IMatchRepository, MatchRepository } from '../../domain/repositories/match.repos';
import { IMatchSettingRepository, MatchSettingRepository } from '../../domain/repositories/match_setting.repos';
import { IMediaAccountRepository, MediaAccountRepository } from '../../domain/repositories/media_account.repos';
import { MatcherDto } from '../dtos/matcher.dto';
import { MatcherInfoDto } from '../dtos/matcher_info.dto';
import { CreateMatchDto } from '../dtos/matches.dto';
import { MatchSettingDto } from '../dtos/match_setting.dto';
import { MediaDto } from '../dtos/media.dto';

class MatchService {
  private commandBus: CommandBus;
  private matchRepos: IMatchRepository;
  private matchSettingRepos: IMatchSettingRepository;
  private userRepos: UserRepository;
  private mediaAccountRepos: IMediaAccountRepository;

  constructor() {
    this.commandBus = container.commandBus;
    this.matchRepos = new MatchRepository();
    this.userRepos = new UserRepository();
    this.matchSettingRepos = new MatchSettingRepository();
    this.mediaAccountRepos = new MediaAccountRepository();
  }

  public async createMatch(data: CreateMatchDto): Promise<Match> {
    const sender = await this.userRepos.findAccountByBaseAccountId(data.accountId, true);
    const receiver = await this.userRepos.findAccountByBaseAccountId(data.dto.receiverId, true);

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
    const account = await this.userRepos.getOrCreateAccountByBaseAccountId(accountId);

    const payload = {
      accountId: account.id,
      data: data,
    };

    data = await this.commandBus.send('updateMatchSettingCommand', undefined, { payload });

    container.eventStore.once('matchSettingUpdatedEvent', event => {
      logger.info(`Match aggregate created with ID ${event.aggregateId}`);
    });

    console.log(data);
  }

  public async getMatchUserRecs(accountId: string): Promise<Array<MatcherDto>> {
    const account = await this.userRepos.getOrCreateAccountByBaseAccountId(accountId);

    const matchers: Array<User> = await this.userRepos.findAllUser();

    return await Promise.all(
      matchers
        .filter(async _m => {
          return await account.canMatch(_m);
        })
        .map(async _m => {
          const medias: Array<MediaAccount> = await this.mediaAccountRepos.queryMediasByAccountId(_m.id);
          const mainMedias = medias.slice(0, 3);

          return new MatcherDto(
            _m.id,
            _m.fullName,
            _m.getAge(),
            _m.bio,
            1,
            mainMedias.map(_media => new MediaDto(_media.mediaUrl, _media.type)),
          );
        }),
    );
  }

  public async getMatcherInfo(accountId: string, matcherId: string): Promise<MatcherInfoDto> {
    const account = await this.userRepos.getOrCreateAccountByBaseAccountId(accountId);
    const matcher: User = await this.userRepos.findUserById(matcherId, true);
    // TODO validate account can view matcher
    const medias: Array<MediaAccount> = await this.mediaAccountRepos.queryMediasByAccountId(matcher.id);

    return new MatcherInfoDto(
      matcher.id,
      matcher.fullName,
      matcher.getAge(),
      1,
      matcher.gender,
      matcher.address,
      matcher.job,
      matcher.reason,
      medias.map(_m => new MediaDto(_m.mediaUrl, _m.type)),
    );
  }
}

export default MatchService;
