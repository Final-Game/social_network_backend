export interface User {
  id: string;
  username: string;
  password: string;
  type: number;

  getRooms: () => Promise<Array<any>>;
  joinRoom: (room: any) => Promise<void>;
  getUserRefRoom: (room: any) => Promise<any>;
}
