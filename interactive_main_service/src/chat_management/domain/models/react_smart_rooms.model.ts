import { UserRoom } from './user_rooms.model';
import { Room } from './rooms.model';

export enum ReactType {
  HATE = 0,
  LOVE = 1,
}
export interface ReactSmartRoom {
  id: string;
  roomId: string;
  senderId: string;
  status: number;
}
