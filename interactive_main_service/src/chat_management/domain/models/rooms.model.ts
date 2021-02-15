import { Message } from './message.model';

export interface Room {
  id: string;
  generalName: string;
  type: number;
  createdAt: Date;
  updatedAt: Date;

  getMemberIds: () => Promise<Array<any>>;
  getMembers: () => Promise<Array<any>>;
  getLastestMsg: () => Promise<any>;
  getMsgs: () => Promise<Array<Message>>;
  isSmartRoomAlive: () => boolean;
  getParterOf: (account: any) => Promise<any>;
  canContinueIntoNormalRoom: () => Promise<boolean>;
  moveIntoNormalRoom: () => void;
}
