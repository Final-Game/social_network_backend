from chat_management.app.queries.get_account_room_list_query import (
    GetAccountRoomListQuery,
)
from chat_management.app.dtos.room_chat_response_dto import RoomChatResponseDto
from typing import List
import graphene
from core.schemas.base_auth import BaseAuth, authenticate_permission
from core.authenticates.account_authentication import AccountAuthentication
from core.app.bus import Bus

from .user_room_type import UserRoomType

auth_data: dict = {
    "auth_token": graphene.String(required=True, description="Auth token"),
    "account_id": graphene.String(required=True, description="Account id"),
}


class Query(graphene.ObjectType, BaseAuth):

    authentication_classes = [AccountAuthentication]
    user_rooms = graphene.List(UserRoomType, **auth_data)

    @classmethod
    def get_bus(cls):
        return Bus()

    @classmethod
    @authenticate_permission
    def resolve_user_rooms(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]

        room_list: List[RoomChatResponseDto] = _bus.dispatch(
            GetAccountRoomListQuery(account_id)
        )

        return list(map(lambda x: x.__dict__, room_list))
