from datetime import datetime
import maya
from core.common.base_api_exception import BaseApiException
from codegen_protos.interactive_main_service_pb2_grpc import ChatServiceStub
from core.services.grpc_service import GrpcService
from chat_management.app.dtos.message_chat_response_dto import (
    MediaChatDto,
    MessageChatReponseDto,
)
from chat_management.app.dtos.room_chat_response_dto import RoomChatResponseDto
from typing import List
from chat_management.app.dtos.create_room_response_dto import CreateRoomResponseDto
from chat_management.app.services import ChatService
import grpc
from codegen_protos.interactive_main_service_pb2 import (
    CreateRoomChatRequest,
    CreateRoomChatReply,
    GetListRoomChatReply,
    GetListRoomChatRequest,
    GetListMessagesInRoomChatRequest,
    GetListMessagesInRoomChatReply,
    UpdateAccountMatchSettingReply,
)


class ChatServiceImpl(GrpcService, ChatService):
    def __init__(self, *args, **kwargs) -> None:
        GrpcService.__init__(self)
        ChatService.__init__(self)

    async def create_room_chat(
        self, account_id: str, receiver_id: str
    ) -> CreateRoomResponseDto:
        try:
            result: CreateRoomChatReply
            async with self.get_connection() as channel:
                stub = ChatServiceStub(channel)

                res: UpdateAccountMatchSettingReply = await stub.CreateRoomChat(
                    CreateRoomChatRequest(
                        account_id=account_id, receiver_id=receiver_id
                    )
                )
                result = res

            return CreateRoomResponseDto(result.room_id)
        except grpc.RpcError as ex:
            raise BaseApiException(ex.details())

    async def get_list_room_chat(self, account_id: str) -> List[RoomChatResponseDto]:
        result: list

        try:
            async with self.get_connection() as channel:
                stub = ChatServiceStub(channel)
                res: GetListRoomChatReply = await stub.GetListRoomChat(
                    GetListMessagesInRoomChatRequest(account_id=account_id)
                )

                result = res.data
        except grpc.RpcError as ex:
            raise BaseApiException(ex.details())

        return list(
            map(
                lambda x: RoomChatResponseDto(
                    x.id,
                    x.avt_icon_url,
                    x.name,
                    x.latest_msg,
                    maya.parse(x.latest_msg_time).datetime(),
                    x.num_un_read_msg,
                ),
                result,
            )
        )

    async def get_messages_in_room_chat(
        self, account_id: str, room_id: str
    ) -> List[MessageChatReponseDto]:
        result: list = []

        async with self.get_connection() as channel:
            stub = ChatServiceStub(channel)

            res: GetListMessagesInRoomChatReply = await stub.GetMessagesInRoomChat(
                GetListMessagesInRoomChatRequest(account_id=account_id, room_id=room_id)
            )
            result = res.data

        return list(
            map(
                lambda x: MessageChatReponseDto(
                    x.id,
                    x.sender_id,
                    x.content,
                    x.created_at,
                    list(map(lambda _x: MediaChatDto(_x.url, _x.type), x.media_data)),
                ),
                result,
            )
        )