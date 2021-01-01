import { INTERACTIVE_MAIN_PROTO_PATH } from '../../../common/grpc/contants';
import protoLoader from '../../../common/grpc/protoLoader';
import { RoomChatDto } from '../../app/dtos/room_chat.dto';
import RoomService from '../../app/services/room.service';
import { GrpcInternalError } from '../errors/internal.error';

class ChatMsgHandler {
  public static roomService: RoomService = new RoomService();

  public static createRoomChat = (call, callback) => {
    const accountId: string = call.request.account_id;
    const receiverId: string = call.request.receiver_id;

    ChatMsgHandler.roomService
      .createRoomChat(accountId, receiverId)
      .then(room => {
        callback(null, { room_id: room.id });
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
    return;
  };

  public static getRoomChatList = (call, callback) => {
    const accountId: string = call.request.account_id;

    ChatMsgHandler.roomService
      .getAccountRoomChatList(accountId)
      .then((data: Array<RoomChatDto>) => {
        callback(null, { data: data.map(item => item.toResData()) });
      })
      .catch(error => {
        callback(new GrpcInternalError(error.message));
      });
  };
}

const interactiveMainProto: any = protoLoader(INTERACTIVE_MAIN_PROTO_PATH).interactive_main_service;

export const chatHandlers = [
  {
    key: interactiveMainProto.ChatService.service,
    value: {
      CreateRoomChat: ChatMsgHandler.createRoomChat,
      GetListRoomChat: ChatMsgHandler.getRoomChatList,
    },
  },
];
