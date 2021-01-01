import { Message } from './message.model';

export interface Room {
  id: string;
  generalName: string;
  type: number;
  createdAt: Date;
  updatedAt: Date;

  getMemberIds: () => Promise<Array<any>>;
  getLastestMsg: () => Promise<any>;
  getMsgs: () => Promise<Array<Message>>;
}
