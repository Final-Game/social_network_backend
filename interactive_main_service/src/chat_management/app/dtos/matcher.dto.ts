export class MatcherDto {
  public matcherId: string;
  public name: string;
  public age: number;
  public bio: string;
  public status: number;

  constructor(matcherId: string, name: string, age: number, bio: string, status: number) {
    this.matcherId = matcherId;
    this.name = name;
    this.age = age;
    this.bio = bio;
    this.status = status;
  }

  public toResData(): any {
    return {
      matcher_id: this.matcherId,
      name: this.name,
      age: this.age,
      bio: this.bio,
      status: this.status,
    };
  }
}
