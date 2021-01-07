from abc import ABC
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