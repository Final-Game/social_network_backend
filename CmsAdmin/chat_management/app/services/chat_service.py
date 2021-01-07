from abc import ABC
from chat_management.app.dtos.message_chat_response_dto import MessageChatReponseDto
from typing import List
from chat_management.app.dtos.room_chat_response_dto import RoomChatResponseDto
from chat_management.app.dtos.create_room_response_dto import CreateRoomResponseDto


class ChatService:
    async def create_room_chat(
        self, account_id: str, receiver_id: str
    ) -> CreateRoomResponseDto:
        raise NotImplementedError()

    async def get_list_room_chat(self, account_id: str) -> List[RoomChatResponseDto]:
        raise NotImplementedError()

    async def get_messages_in_room_chat(
        self, account_id: str, room_id: str
    ) -> List[MessageChatReponseDto]:
        raise NotImplementedError()