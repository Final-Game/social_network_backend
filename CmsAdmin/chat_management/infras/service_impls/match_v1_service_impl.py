from core.services.grpc_service import GrpcService
from chat_management.app.dtos.match_setting_request_dto import MatchSettingRequestDto
from chat_management.app.dtos.match_setting_response_dto import MatchSettingResponseDto
from chat_management.app.services import MatchV1Service

from codegen_protos.interactive_main_service_pb2 import (
    GetAccountMatchSettingRequest,
    GetAccountMatchSettingReply,
    UpdateAccountMatchSettingRequest,
    UpdateAccountMatchSettingReply,
)
from codegen_protos.interactive_main_service_pb2_grpc import (
    MatchServiceV1,
    MatchServiceV1Stub,
)


class MatchV1ServiceImpl(GrpcService, MatchV1Service):
    def __init__(self, *args, **kwargs) -> None:
        GrpcService.__init__(self)
        MatchServiceV1.__init__(self)

    async def get_account_match_setting(
        self, account_id: str
    ) -> MatchSettingResponseDto:
        result: GetAccountMatchSettingReply

        async with self.get_connection() as channel:
            stub = MatchServiceV1Stub(channel)

            response: GetAccountMatchSettingReply = await stub.GetAccountMatchSetting(
                GetAccountMatchSettingRequest(account_id=account_id)
            )

            result = response

        return MatchSettingResponseDto(
            result.min_age,
            result.max_age,
            result.max_distance,
            result.target_gender,
        )

    async def update_account_match_setting(
        self, account_id: str, match_setting_dto: MatchSettingRequestDto
    ):
        result: UpdateAccountMatchSettingReply
        async with self.get_connection() as channel:
            stub = MatchServiceV1Stub(channel)

            res: UpdateAccountMatchSettingReply = await stub.UpdateAccountMatchSetting(
                account_id=account_id, **match_setting_dto.__dict__
            )
            result = res

        print(f"Update account match setting with status {result.status}")
        return super().update_account_match_setting(account_id, match_setting_dto)