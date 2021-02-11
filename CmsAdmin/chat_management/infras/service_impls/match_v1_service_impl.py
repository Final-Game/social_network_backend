from chat_management.app.dtos.matcher_info_dto import MatcherInfoDto
import grpc
from chat_management.app.dtos.matcher_dto import MatcherDto
from typing import Any, List
from core.common.base_api_exception import BaseApiException
from core.services.grpc_service import GrpcService
from chat_management.app.dtos.match_setting_request_dto import MatchSettingRequestDto
from chat_management.app.dtos.match_setting_response_dto import MatchSettingResponseDto
from chat_management.app.services import MatchV1Service

from codegen_protos.interactive_main_service_pb2 import (
    GetAccountMatchSettingRequest,
    GetAccountMatchSettingReply,
    UpdateAccountMatchSettingRequest,
    UpdateAccountMatchSettingReply,
    GetMatcherListRequest,
    GetMatcherListReply,
    GetMatcherInfoRequest,
    GetMatcherInfoReply,
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
                UpdateAccountMatchSettingRequest(
                    account_id=account_id, **match_setting_dto.__dict__
                )
            )
            result = res

        print(f"Update account match setting with status {result.status}")
        return super().update_account_match_setting(account_id, match_setting_dto)

    async def get_matcher_list(self, account_id: str) -> List[MatcherDto]:
        result: list

        try:
            async with self.get_connection() as channel:
                stub = MatchServiceV1Stub(channel)
                res: GetMatcherListReply = await stub.GetMatcherList(
                    GetMatcherListRequest(account_id=account_id)
                )

                result = res.data
        except grpc.RpcError as ex:
            raise BaseApiException(ex.details())
        return list(
            map(
                lambda x: MatcherDto(x.matcher_id, x.name, x.age, x.bio, x.status),
                result,
            )
        )

    async def get_matcher_info(
        self, account_id: str, matcher_id: str
    ) -> MatcherInfoDto:
        result: Any

        try:
            async with self.get_connection() as channel:
                stub = MatchServiceV1Stub(channel)
                res: GetMatcherInfoReply = await stub.GetMatcherInfo(
                    GetMatcherInfoRequest(account_id=account_id, matcher_id=matcher_id)
                )

                result = res
        except grpc.RpcError as ex:
            raise BaseApiException(ex.details())

        return MatcherInfoDto(
            result.matcher_id,
            result.name,
            result.age,
            result.gender,
            result.address,
            result.job,
            result.reason,
        )
