import asyncio
from core.common.base_api_exception import BaseApiException
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.service_impls.match_v1_service_impl import (
    MatchV1ServiceImpl,
)
from chat_management.app.services.match_v1_service import MatchV1Service
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.app.gateways.user_content_gateway import UserContentGateway
from chat_management.app.dtos.match_setting_request_dto import MatchSettingRequestDto
from core.app.bus import Command, CommandHandler


class UpdateUserMatchSettingCommand(Command):
    account_id: str
    dto: MatchSettingRequestDto

    def __init__(self, account_id: str, dto: MatchSettingRequestDto) -> None:
        self.account_id = account_id
        self.dto = dto


class UpdateUserMatchSettingCommandHandler(CommandHandler):
    _user_content_gw: UserContentGateway
    _match_service: MatchV1Service

    def __init__(
        self,
        user_content_gw: UserContentGateway = UserContentGatewayImpl(),
        match_service: MatchV1Service = MatchV1ServiceImpl(),
    ) -> None:
        self._match_service = match_service
        self._user_content_gw = user_content_gw
        super().__init__()

    def handle(self, command: UpdateUserMatchSettingCommand):
        account: AccountInfoDto = self._user_content_gw.get_account_info(
            command.account_id
        )
        if not account:
            raise BaseApiException(f"Account with id {command.account_id} not found!")

        asyncio.run(
            self._match_service.update_account_match_setting(
                account.id, match_setting_dto=command.dto
            )
        )

        return