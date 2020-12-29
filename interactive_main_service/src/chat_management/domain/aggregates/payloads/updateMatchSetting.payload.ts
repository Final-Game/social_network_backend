export interface MatchSettingDto {
  maxAge: number;
  minAge: number;
  maxDistance: number;
  targetGender: string;
}

export interface UpdateMatchSettingPayload {
  accountId: string;
  data: MatchSettingDto;
}
