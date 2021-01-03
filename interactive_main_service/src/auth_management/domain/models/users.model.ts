export interface User {
  id: string;
  fullName: string;
  avatar: string;
  birthDate: Date;
  gender: number;
  refId: string;

  getAge: () => number;
  getRooms: () => Promise<Array<any>>;
  getCurrentSmartRooms: () => Promise<Array<any>>;
  joinRoom: (room: any) => Promise<void>;
  getUserRefRoom: (room: any) => Promise<any>;
  getMatchSetting: () => Promise<any>;
  canMatch: (partner: any) => Promise<boolean>;
  isReadyForNewSmartRoom: () => Promise<boolean>;
}
