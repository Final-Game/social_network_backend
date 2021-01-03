export class AccountInfoDto {
  id: string;
  fullName: string;
  avatar: string;
  birthDate: Date;
  gender: number;

  constructor(id: string, fullName: string, avatar: string, birthDate: Date, gender: number) {
    this.id = id;
    this.fullName = fullName;
    this.avatar = avatar;
    this.birthDate = birthDate;
    this.gender = gender;
  }
}
