import { Gender } from '../../../domain/enums/gender.enum';
import { MatchSetting } from '../../../domain/models/match_settings.model';

const convertGenderName = (gender: Gender): string => {
  switch (gender) {
    case Gender.MALE:
      return 'MALE';
    case Gender.FEMALE:
      return 'FEMALE';
    case Gender.UN_KNOWN:
      return 'UN_KNOWN';
    default:
      return null;
  }
};

export class MatchSettingDto {
  public min_age: number;
  public max_age: number;
  public max_distance: number;
  public target_gender: string;

  constructor(matchSetting: MatchSetting) {
    this.max_age = matchSetting.maxAge;
    this.min_age = matchSetting.minAge;
    this.max_distance = matchSetting.maxDistance;
    this.target_gender = convertGenderName(matchSetting.targetGender);
  }
}
