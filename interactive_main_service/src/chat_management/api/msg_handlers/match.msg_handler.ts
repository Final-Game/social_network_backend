import { MATCH_PROTO_PATH } from '../../../common/grpc/contants';
import protoLoader from '../../../common/grpc/protoLoader';

class MatchMsgHandler {
  public static createMatch = (call, callback) => {
    console.log(call.request);
    callback(null, { status: 'Success' });
  };
}

// function createMatch(call, callback) {
//   console.log(call.request);
//   callback(null, { status: 'Success' });
// }

const matchProto: any = protoLoader(MATCH_PROTO_PATH).match_service;

export const matchHandlers = [
  {
    key: matchProto.MatchService.service,
    value: {
      CreateMatch: MatchMsgHandler.createMatch,
    },
  },
];
