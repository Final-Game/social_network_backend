import { Room } from './rooms.model';
import { UserRoom } from './user_rooms.model';

export interface Message {
  id: string;
  sender: UserRoom;
  room: Room;
  content: string;
}
