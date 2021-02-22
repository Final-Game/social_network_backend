from chat_management.app.dtos.matching_data_dto import MatchingDataDto
from chat_management.app.dtos.matcher_data_dto import MatcherDataDto
from chat_management.infras.service_impls.match_v1_service_impl import (
    MatchV1ServiceImpl,
)
from chat_management.app.services.match_v1_service import MatchV1Service
from core.app.bus import Query, QueryHandler
import asyncio


class GetMatchingDataQuery(Query):
    def __init__(self) -> None:
        super().__init__()


class GetMatchingDataQueryHandler(QueryHandler):
    _match_service: MatchV1Service

    def __init__(self, match_service: MatchV1Service = MatchV1ServiceImpl()) -> None:
        self._match_service = match_service

    def handle(self, query: GetMatchingDataQuery) -> MatchingDataDto:

        data: MatchingDataDto = asyncio.run(self._match_service.get_matching_data())
        return data