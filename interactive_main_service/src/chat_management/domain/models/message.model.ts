import { Room } from './rooms.model';

export interface Message {
  id: string;
  senderId: string;
  room: Room;
  content: string;
}
