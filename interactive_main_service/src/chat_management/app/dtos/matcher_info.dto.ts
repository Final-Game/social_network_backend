import { MediaDto } from './media.dto';

export class MatcherInfoDto {
  public matcherId: string;
  public name: string;
  public age: number;
  public status: number;
  public gender: number;
  public address: string;
  public job: string;
  public reason: string;
  public medias: Array<MediaDto>;

  constructor(
    matcherId: string,
    name: string,
    age: number,
    status: number,
    gender: number,
    address: string,
    job: string,
    reason: string,
    medias: Array<MediaDto> = [],
  ) {
    this.matcherId = matcherId;
    this.name = name;
    this.age = age;
    this.status = status;
    this.gender = gender;
    this.address = address;
    this.reason = reason;
    this.job = job;
    this.medias = medias;
  }

  public toResData(): any {
    return {
      matcher_id: this.matcherId,
      name: this.name,
      age: this.age,
      status: this.status,
      gender: this.gender,
      address: this.address,
      reason: this.reason,
      job: this.job,
      medias: this.medias.map(_m => _m.toResData()),
    };
  }
}
