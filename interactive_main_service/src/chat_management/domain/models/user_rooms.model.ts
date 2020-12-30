import { Room } from './rooms.model';

export interface UserRoom {
  id: string;
  accountId: string;
  nickName: string;
  roomId: string;

  updateNickName: (nickName: string) => void;
  getRoom: () => Promise<Room>;
}
