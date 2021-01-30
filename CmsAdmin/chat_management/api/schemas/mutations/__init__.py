import graphene
from .user_create_room_mutation import UserCreateRoomMutation
from .user_update_match_setting_mutation import UserUpdateMatchSettingMutation
from .user_create_match_mutation import UserCreateMatchMutation


class Mutation(graphene.ObjectType):
    user_create_room = UserCreateRoomMutation.Field()
    user_update_match_setting = UserUpdateMatchSettingMutation.Field()
    user_create_match = UserCreateMatchMutation.Field()