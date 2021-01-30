import { MediaMessage } from './media_messages.model';
import { Room } from './rooms.model';
import { UserRoom } from './user_rooms.model';

export interface Message {
  id: string;
  senderId: string;
  roomId: string;
  content: string;
  createdAt: Date;
  updatedAt: Date;
  getMedias: () => Promise<Array<MediaMessage>>;
}
