from chat_management.app.dtos.match_setting_response_dto import MatchSettingResponseDto
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.app.gateways.user_content_gateway import UserContentGateway
from chat_management.infras.service_impls.match_v1_service_impl import (
    MatchV1ServiceImpl,
)
from chat_management.app.services.match_v1_service import MatchV1Service
from core.app.bus import Query, QueryHandler
import asyncio


class GetAccountMatchSettingQuery(Query):
    account_id: str

    def __init__(self, account_id: str) -> None:
        self.account_id = account_id


class GetAccountMatchSettingQueryHandler(QueryHandler):
    _match_service: MatchV1Service
    _user_content_gw: UserContentGateway

    def __init__(
        self,
        match_service: MatchV1Service = MatchV1ServiceImpl(),
        user_content_gw: UserContentGateway = UserContentGatewayImpl(),
    ) -> None:
        self._match_service = match_service
        self._user_content_gw = user_content_gw

    def handle(self, query: GetAccountMatchSettingQuery) -> MatchSettingResponseDto:
        account: AccountInfoDto = self._user_content_gw.get_account_info(
            query.account_id
        )

        match_seting_dto: MatchSettingResponseDto = asyncio.run(
            self._match_service.get_account_match_setting(account.id)
        )
        return match_seting_dto