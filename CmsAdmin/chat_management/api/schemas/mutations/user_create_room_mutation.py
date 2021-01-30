from chat_management.app.commands.user_create_room_command import UserCreateRoomCommand
from chat_management.app.dtos.create_room_response_dto import CreateRoomResponseDto
from core.app.bus import Bus
from core.schemas.base_auth import authenticate_permission
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.authenticates.account_authentication import AccountAuthentication


class UserCreateRoomMutation(BaseMutation, BaseAuth):
    room_id = graphene.String(description="Room id", default_value=None)

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")
        receiver_id = graphene.String(required=True, description="Receiver id")

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        receiver_id: str = kwargs["receiver_id"]

        bus: Bus = cls.get_bus()
        room_data: CreateRoomResponseDto = bus.dispatch(
            UserCreateRoomCommand(account_id, receiver_id)
        )

        return cls(room_id=room_data.room_id)
