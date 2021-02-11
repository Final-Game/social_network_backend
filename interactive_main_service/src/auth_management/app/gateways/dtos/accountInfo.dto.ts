export class AccountInfoDto {
  id: string;
  fullName: string;
  avatar: string;
  birthDate: Date;
  gender: number;
  bio: string;
  address: string;
  job: string;
  reason: string;

  constructor(id: string, fullName: string, avatar: string, birthDate: Date, gender: number, bio = '', address = '', job = '', reason = '') {
    this.id = id;
    this.fullName = fullName;
    this.avatar = avatar;
    this.birthDate = birthDate;
    this.gender = gender;
    this.bio = bio;
    this.address = address;
    this.job = job;
    this.reason = reason;
  }
}
