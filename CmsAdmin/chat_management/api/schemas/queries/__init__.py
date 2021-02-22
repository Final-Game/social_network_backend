from chat_management.app.queries.get_matching_data_query import GetMatchingDataQuery
from chat_management.app.dtos.matching_data_dto import MatchingDataDto
from chat_management.app.queries.get_account_room_info_query import (
    GetAccountRoomInfoQuery,
)
from chat_management.app.dtos.room_info_dto import RoomInfoDto
from chat_management.app.queries.get_account_matcher_info_query import (
    GetAccountMatcherInfoQuery,
)
from chat_management.app.dtos.matcher_info_dto import MatcherInfoDto
from chat_management.app.queries.get_account_matcher_list_query import (
    GetAccountMatcherListQuery,
)
from chat_management.app.dtos.matcher_dto import MatcherDto
from chat_management.app.queries.get_account_match_setting_query import (
    GetAccountMatchSettingQuery,
)
from chat_management.app.dtos.match_setting_response_dto import MatchSettingResponseDto
from chat_management.app.queries.get_messages_in_room_chat_query import (
    GetMessagesInRoomChatQuery,
)
from chat_management.app.dtos.message_chat_response_dto import MessageChatReponseDto
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
from .media_chat_type import MediaChatType
from .message_chat_type import MessageChatType
from .match_setting_type import MatchSettingType
from .matcher_type import MatcherType
from .matcher_info_type import MatcherInfoType
from .room_info_type import RoomInfoType
from .matching_data_type import MatchingDataType


auth_data: dict = {
    "auth_token": graphene.String(required=True, description="Auth token"),
    "account_id": graphene.String(required=True, description="Account id"),
}


class Query(graphene.ObjectType, BaseAuth):

    authentication_classes = [AccountAuthentication]
    user_rooms = graphene.List(UserRoomType, **auth_data)
    user_room_messages = graphene.List(
        MessageChatType,
        **auth_data,
        room_id=graphene.String(required=True, description="Room id")
    )
    user_match_setting = graphene.Field(
        MatchSettingType, **auth_data, description="Match setting"
    )
    matchers = graphene.List(MatcherType, **auth_data)
    matcher_info = graphene.Field(
        MatcherInfoType,
        **auth_data,
        matcher_id=graphene.String(required=True, description="Matcher id"),
        description="Matcher info"
    )
    room_info = graphene.Field(
        RoomInfoType,
        **auth_data,
        room_id=graphene.String(required=True, description="Room id"),
        description="Room info"
    )
    matching_data = graphene.Field(
        MatchingDataType, **auth_data, description="Matching data"
    )

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

    @classmethod
    @authenticate_permission
    def resolve_user_room_messages(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        room_id: str = kwargs["room_id"]

        room_msgs: List[MessageChatReponseDto] = _bus.dispatch(
            GetMessagesInRoomChatQuery(account_id, room_id)
        )

        return list(map(lambda msg: msg.__dict__, room_msgs))

    @classmethod
    @authenticate_permission
    def resolve_user_match_setting(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]

        match_setting: MatchSettingResponseDto = _bus.dispatch(
            GetAccountMatchSettingQuery(account_id)
        )

        return match_setting.__dict__

    @classmethod
    @authenticate_permission
    def resolve_matchers(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]

        matchers: List[MatcherDto] = _bus.dispatch(
            GetAccountMatcherListQuery(account_id)
        )
        return list(map(lambda _m: _m.__dict__, matchers))

    @classmethod
    @authenticate_permission
    def resolve_matcher_info(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        matcher_id: str = kwargs["matcher_id"]

        matcher_info: MatcherInfoDto = _bus.dispatch(
            GetAccountMatcherInfoQuery(account_id, matcher_id)
        )

        return matcher_info.__dict__

    @classmethod
    @authenticate_permission
    def resolve_room_info(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        room_id: str = kwargs["room_id"]

        room_info: RoomInfoDto = _bus.dispatch(
            GetAccountRoomInfoQuery(account_id, room_id)
        )

        return room_info.__dict__

    @classmethod
    @authenticate_permission
    def resolve_matching_data(cls, *args, **kwargs):
        _bus: Bus = cls.get_bus()

        matching_data: MatchingDataDto = _bus.dispatch(GetMatchingDataQuery())

        return matching_data.__dict__
