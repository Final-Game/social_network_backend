import BaseException from '../../../common/exceptions/BaseException';
import { INTERACTIVE_MAIN_PROTO_PATH, MATCH_PROTO_PATH } from '../../../common/grpc/contants';
import protoLoader from '../../../common/grpc/protoLoader';
import MatchService from '../../app/services/matches.service';
import grpc from 'grpc';

export class GrpcInternalError {
  public code: number;
  public status: number;
  public message: string;

  constructor(message: string) {
    this.message = message;

    this.code = 500;
    this.status = grpc.status.INTERNAL;
  }
}

class MatchMsgHandler {
  public static matchService: MatchService = new MatchService();

  public static createMatch = (call, callback) => {
    console.log(call.request);
    const senderId = call.request.sender_id;
    const receiverId = call.request.receiver_id;
    const status = call.request.status;

    MatchMsgHandler.matchService
      .createMatch({
        accountId: senderId,
        dto: {
          receiverId: receiverId,
          status: status,
        },
      })
      .then(data => {
        callback(null, { status: 'Success' });
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };
}

// function createMatch(call, callback) {
//   console.log(call.request);
//   callback(null, { status: 'Success' });
// }

const matchProto: any = protoLoader(MATCH_PROTO_PATH).match_service;
const interactiveMainProto: any = protoLoader(INTERACTIVE_MAIN_PROTO_PATH).interactive_main_service;

export const matchHandlers = [
  {
    key: matchProto.MatchService.service,
    value: {
      CreateMatch: MatchMsgHandler.createMatch,
    },
  },
];