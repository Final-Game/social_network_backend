import asyncio
from user_content.domain.models.account import Account

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

    def __init__(self, chat_service: ChatService = ChatServiceImpl()) -> None:
        self._chat_service = chat_service

    def handle(self, command: UserCreateRoomCommand) -> CreateRoomResponseDto:
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        receiver: Account = Account.objects.find_account_by_id(
            command.receiver_id, raise_exception=True
        )

        # validate
        self.validate_account_can_create_room_with_receiver(account, receiver)

        room_data: CreateRoomResponseDto = asyncio.run(
            self._chat_service.create_room_chat(account.id, receiver.id)
        )

        return room_data

    def validate_account_can_create_room_with_receiver(
        self, account: Account, receiver: Account
    ):
        return