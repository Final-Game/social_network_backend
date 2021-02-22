export class MatcherData {
  id: string;
  avatar: string;
  name: string;
  bio: string;
  age: number;
  gender: number;

  constructor(id: string, avatar: string, name: string, bio: string, age: number, gender: number) {
    this.id = id;
    this.avatar = avatar;
    this.name = name;
    this.bio = bio;
    this.age = age;
    this.gender = gender;
  }

  public toResData(): any {
    return {
      id: this.id,
      avatar: this.avatar,
      name: this.name,
      bio: this.bio,
      age: this.age,
      gender: this.gender,
    };
  }
}

export class MatchingDataDto {
  numSmartChatUsers: number;
  numTraditionalMatchUsers: number;
  nearlyUsers: Array<MatcherData>;

  constructor(numSmartChatUsers: number, numTraditionalMatchUsers: number, nearlyUsers: Array<MatcherData>) {
    this.numSmartChatUsers = numSmartChatUsers;
    this.numTraditionalMatchUsers = numTraditionalMatchUsers;
    this.nearlyUsers = nearlyUsers;
  }

  public toResData(): any {
    return {
      num_smart_chat_users: this.numSmartChatUsers,
      num_traditional_match_users: this.numTraditionalMatchUsers,
      nearly_users: this.nearlyUsers,
    };
  }
}
