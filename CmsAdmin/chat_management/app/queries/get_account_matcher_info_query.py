import asyncio
from chat_management.app.dtos.matcher_info_dto import MatcherInfoDto
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.infras.service_impls.match_v1_service_impl import (
    MatchV1ServiceImpl,
)
from core.common.base_api_exception import BaseApiException
from chat_management.app.gateways.user_content_gateway import UserContentGateway
from chat_management.app.services.match_v1_service import MatchV1Service
from core.app.bus import Query, QueryHandler


class GetAccountMatcherInfoQuery(Query):
    account_id: str
    matcher_id: str

    def __init__(self, account_id: str, matcher_id: str) -> None:
        self.account_id = account_id
        self.matcher_id = matcher_id


class GetAccountMatcherInfoQueryHandler(QueryHandler):
    _match_service: MatchV1Service
    _uc_gw: UserContentGateway

    def __init__(
        self,
        match_service: MatchV1Service = MatchV1ServiceImpl(),
        uc_gw: UserContentGateway = UserContentGatewayImpl(),
    ) -> None:
        self._match_service = match_service
        self._uc_gw = uc_gw

    def handle(self, query: GetAccountMatcherInfoQuery) -> MatcherInfoDto:
        account: AccountInfoDto = self._uc_gw.get_account_info(query.account_id)

        if not account:
            raise BaseApiException(f"Account with id: ${query.account_id} not found.")

        matcher_info: MatcherInfoDto = asyncio.run(
            self._match_service.get_matcher_info(account.id, query.matcher_id)
        )
        return matcher_info