import { MediaDto } from './media.dto';

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

  medias: Array<MediaDto>;

  constructor(
    id: string,
    fullName: string,
    avatar: string,
    birthDate: Date,
    gender: number,
    bio = '',
    address = '',
    job = '',
    reason = '',
    medias: Array<MediaDto> = [],
  ) {
    this.id = id;
    this.fullName = fullName;
    this.avatar = avatar;
    this.birthDate = birthDate;
    this.gender = gender;
    this.bio = bio;
    this.address = address;
    this.job = job;
    this.reason = reason;
    this.medias = medias;
  }
}
