import asyncio
from core.common.base_api_exception import BaseApiException
from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.infras.gateway_impls.user_content_gateway_impl import (
    UserContentGatewayImpl,
)
from chat_management.app.gateways.user_content_gateway import UserContentGateway

from chat_management.app.dtos.create_room_response_dto import CreateRoomResponseDto
from chat_management.infras.service_impls.chat_service_impl import ChatServiceImpl
from chat_management.app.services.chat_service import ChatService
from core.app.bus import Command, CommandHandler


class UserCreateRoomCommand(Command):
    account_id: str
    receiver_id: str

    def __init__(self, account_id: str, receiver_id: str) -> None:
        self.account_id = account_id
        self.receiver_id = receiver_id


class UserCreateRoomCommandHandler(CommandHandler):
    _chat_service: ChatService
    _user_content_gateway: UserContentGateway

    def __init__(
        self,
        chat_service: ChatService = ChatServiceImpl(),
        user_content_gw: UserContentGateway = UserContentGatewayImpl(),
    ) -> None:
        self._chat_service = chat_service
        self._user_content_gateway = user_content_gw

    def handle(self, command: UserCreateRoomCommand) -> CreateRoomResponseDto:
        account: AccountInfoDto = self._user_content_gateway.get_account_info(
            command.account_id
        )
        receiver: AccountInfoDto = self._user_content_gateway.get_account_info(
            command.receiver_id
        )

        # validate
        self.validate_account_can_create_room_with_receiver(account, receiver)

        room_data: CreateRoomResponseDto = asyncio.run(
            self._chat_service.create_room_chat(account.id, receiver.id)
        )

        return room_data

    def validate_account_can_create_room_with_receiver(
        self, account: AccountInfoDto, receiver: AccountInfoDto
    ):
        if not account:
            raise BaseApiException("Account not found!")

        if not receiver:
            raise BaseApiException("Receiver not found!")
