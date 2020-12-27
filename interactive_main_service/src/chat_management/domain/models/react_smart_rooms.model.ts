import { UserRoom } from './user_rooms.model';
import { Room } from './rooms.model';

export interface ReactSmartRoom {
  id: string;
  room: Room;
  sender: UserRoom;
  status: number;
}
