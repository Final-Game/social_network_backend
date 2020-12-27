import { Message } from './message.model';

export interface MediaMessage {
  id: string;
  message: Message;
  type: number;
  mediaUrl: string;
}
