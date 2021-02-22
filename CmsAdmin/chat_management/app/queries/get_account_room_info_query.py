from chat_management.app.dtos.room_info_dto import RoomInfoDto
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.service_impls.chat_service_impl import ChatServiceImpl
from chat_management.app.services.chat_service import ChatService
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.app.gateways.user_content_gateway import UserContentGateway
from core.app.bus import Query, QueryHandler
import asyncio


class GetAccountRoomInfoQuery(Query):
    account_id: str
    room_id: str

    def __init__(self, account_id: str, room_id: str) -> None:
        self.account_id = account_id
        self.room_id = room_id


class GetAccountRoomInfoQueryHandler(QueryHandler):
    _user_content_gw: UserContentGateway
    _chat_service: ChatService

    def __init__(
        self,
        user_content_gw: UserContentGateway = UserContentGatewayImpl(),
        chat_service: ChatService = ChatServiceImpl(),
    ) -> None:
        self._user_content_gw = user_content_gw
        self._chat_service = chat_service

    def handle(self, query: GetAccountRoomInfoQuery) -> RoomInfoDto:
        account: AccountInfoDto = self._user_content_gw.get_account_info(
            query.account_id
        )

        room: RoomInfoDto = asyncio.run(
            self._chat_service.get_room_info(account.id, query.room_id)
        )
        return room