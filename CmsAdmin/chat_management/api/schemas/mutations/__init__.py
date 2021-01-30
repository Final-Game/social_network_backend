import graphene
from .user_create_room_mutation import UserCreateRoomMutation


class Mutation(graphene.ObjectType):
    user_create_room = UserCreateRoomMutation.Field()