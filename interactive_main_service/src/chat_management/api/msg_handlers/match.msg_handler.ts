import BaseException from '../../../common/exceptions/BaseException';
import { INTERACTIVE_MAIN_PROTO_PATH, MATCH_PROTO_PATH } from '../../../common/grpc/contants';
import protoLoader from '../../../common/grpc/protoLoader';
import MatchService from '../../app/services/matches.service';
import { GrpcInternalError } from '../errors/internal.error';
import { MatchSettingDto } from './dtos/match_setting.dto';

class MatchMsgHandler {
  public static matchService: MatchService = new MatchService();

  public static createMatch = (call, callback) => {
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
      .then(() => {
        callback(null, { status: 'Success' });
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };

  public static getAccountMatchSetting = (call, callback) => {
    const accountId: string = call.request.account_id;

    MatchMsgHandler.matchService
      .getAccountMatchSetting(accountId)
      .then(data => {
        callback(null, new MatchSettingDto(data));
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };

  public static updateAccountMatchSetting = (call, callback) => {
    const accountId: string = call.request.account_id;

    const data: any = {
      minAge: call.request.min_age,
      maxAge: call.request.max_age,
      maxDistance: call.request.max_distance,
      targetGender: call.request.target_gender,
    };
    MatchMsgHandler.matchService
      .updateAccountMatchSetting(accountId, data)
      .then(() => callback(null, { status: 'Success' }))
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };

  public static getMatcherList = (call, callback) => {
    const accountId: string = call.request.account_id;

    MatchMsgHandler.matchService
      .getMatchUserRecs(accountId)
      .then(data => {
        callback(null, { data: data.map(item => item.toResData()) });
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };

  public static getMatcherInfo = (call, callback) => {
    const accountId: string = call.request.account_id;
    const matcherId: string = call.request.matcher_id;

    MatchMsgHandler.matchService
      .getMatcherInfo(accountId, matcherId)
      .then(data => {
        callback(null, data.toResData());
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };

  public static getMatchingData = (call, callback) => {
    MatchMsgHandler.matchService
      .getMatchingData()
      .then(data => {
        callback(null, data.toResData());
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };
}

const matchProto: any = protoLoader(MATCH_PROTO_PATH).match_service;
const interactiveMainProto: any = protoLoader(INTERACTIVE_MAIN_PROTO_PATH).interactive_main_service;

export const matchHandlers = [
  {
    key: matchProto.MatchService.service,
    value: {
      CreateMatch: MatchMsgHandler.createMatch,
    },
  },
  {
    key: interactiveMainProto.MatchServiceV1.service,
    value: {
      GetAccountMatchSetting: MatchMsgHandler.getAccountMatchSetting,
      UpdateAccountMatchSetting: MatchMsgHandler.updateAccountMatchSetting,
      GetMatcherList: MatchMsgHandler.getMatcherList,
      GetMatcherInfo: MatchMsgHandler.getMatcherInfo,
      GetMatchingData: MatchMsgHandler.getMatchingData,
    },
  },
];
