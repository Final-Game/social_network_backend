import asyncio
from chat_management.app.dtos.matcher_dto import MatcherDto
from typing import List
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.infras.service_impls.match_v1_service_impl import (
    MatchV1ServiceImpl,
)
from core.common.base_api_exception import BaseApiException
from chat_management.app.gateways.user_content_gateway import UserContentGateway
from core.app.bus import Query, QueryHandler

from chat_management.app.services.match_v1_service import MatchV1Service


class GetAccountMatcherListQuery(Query):
    account_id: str

    def __init__(self, account_id: str) -> None:
        self.account_id = account_id


class GetAccountMatcherListQueryHandler(QueryHandler):
    _matcher_service: MatchV1Service
    _uc_gw: UserContentGateway

    def __init__(
        self,
        match_service: MatchV1Service = MatchV1ServiceImpl(),
        uc_gw: UserContentGateway = UserContentGatewayImpl(),
    ) -> None:
        self._matcher_service = match_service
        self._uc_gw = uc_gw

    def handle(self, query: GetAccountMatcherListQuery) -> List[MatcherDto]:
        account: AccountInfoDto = self._uc_gw.get_account_info(query.account_id)
        if not account:
            raise BaseApiException(f"Account with id: ${query.account_id} not found.")

        matcher_list: List[MatcherDto] = asyncio.run(
            self._matcher_service.get_matcher_list(account.id)
        )

        return matcher_list