import { Room } from './rooms.model';

export interface UserRoom {
  id: string;
  accountId: string;
  nickName: string;
  room: Room;
}
