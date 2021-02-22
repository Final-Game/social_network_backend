from abc import ABC
from chat_management.app.dtos.matching_data_dto import MatchingDataDto
from chat_management.app.dtos.matcher_info_dto import MatcherInfoDto
from chat_management.app.dtos.matcher_dto import MatcherDto
from typing import List
from chat_management.app.dtos.match_setting_request_dto import MatchSettingRequestDto
from chat_management.app.dtos.match_setting_response_dto import MatchSettingResponseDto


class MatchV1Service:
    async def get_account_match_setting(
        self, account_id: str
    ) -> MatchSettingResponseDto:
        raise NotImplementedError()

    async def update_account_match_setting(
        self, account_id: str, match_setting_dto: MatchSettingRequestDto
    ):
        raise NotImplementedError()

    async def get_matcher_list(self, account_id: str) -> List[MatcherDto]:
        raise NotImplementedError()

    async def get_matcher_info(
        self, account_id: str, matcher_id: str
    ) -> MatcherInfoDto:
        raise NotImplementedError()

    async def get_matching_data(self) -> MatchingDataDto:
        raise NotImplementedError()