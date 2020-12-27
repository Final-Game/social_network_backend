export interface MatchSetting {
  id: string;
  accountId: string;
  targetGender: number;
  minAge: number;
  maxAge: number;
  maxDistance: number;
  createdAt: Date;
  updatedAt: Date;
}
