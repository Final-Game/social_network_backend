export class MatcherInfoDto {
  public matcherId: string;
  public name: string;
  public age: number;
  public status: number;
  public gender: number;
  public address: string;
  public job: string;
  public reason: string;

  constructor(matcherId: string, name: string, age: number, status: number, gender: number, address: string, job: string, reason: string) {
    this.matcherId = matcherId;
    this.name = name;
    this.age = age;
    this.status = status;
    this.gender = gender;
    this.address = address;
    this.reason = reason;
    this.job = job;
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
    };
  }
}
