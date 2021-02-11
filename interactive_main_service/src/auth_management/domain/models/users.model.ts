export interface User {
  id: string;
  fullName: string;
  avatar: string;
  birthDate: string;
  gender: number;
  refId: string;
  bio: string;
  address: string;
  job: string;
  reason: string;
  createdAt: Date;
  updatedAt: Date;

  getAge: () => number;
  getBirthDate: () => Date;
  updateData: (fullName: string, avatar: string, birthDate: Date, gender: number, bio: string, address: string, job: string, reason: string) => void;
  getRooms: () => Promise<Array<any>>;
  getCurrentSmartRooms: () => Promise<Array<any>>;
  joinRoom: (room: any) => Promise<void>;
  getUserRefRoom: (room: any) => Promise<any>;
  getMatchSetting: () => Promise<any>;
  canMatch: (partner: any) => Promise<boolean>;
  isReadyForNewSmartRoom: () => Promise<boolean>;
}
