import asyncio
from core.common.base_api_exception import BaseApiException
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.service_impls.match_service_impl import MatchServiceImpl
from chat_management.app.services.match_service import MatchService
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.app.gateways.user_content_gateway import UserContentGateway
from core.app.bus import Command, CommandHandler
from chat_management.app.dtos import CreateMatchDto


class CreateUserMatchCommand(Command):
    account_id: str
    dto: CreateMatchDto

    def __init__(self, account_id: str, dto: CreateMatchDto) -> None:
        self.account_id = account_id
        self.dto = dto


class CreateUserMatchCommandHandler(CommandHandler):
    _user_content_gw: UserContentGateway
    _match_service: MatchService

    def __init__(
        self,
        user_content_gw: UserContentGateway = UserContentGatewayImpl(),
        match_service: MatchService = MatchServiceImpl(),
    ) -> None:
        self._user_content_gw = user_content_gw
        self._match_service = match_service

    def handle(self, command: CreateUserMatchCommand):
        account: AccountInfoDto = self._user_content_gw.get_account_info(
            command.account_id
        )
        if not account:
            raise BaseApiException(f"Account with id {command.account_id} not found!")

        asyncio.run(self._match_service.create_match(account.id, dto=command.dto))

        return super().handle(command)