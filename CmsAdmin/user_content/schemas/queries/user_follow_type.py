import graphene
from graphene_django.types import DjangoObjectType
from user_content.models import Account


class UserFollowType(DjangoObjectType):
    name = graphene.Field(type=graphene.String)
    avatar = graphene.Field(type=graphene.String)

    class Meta:
        model = Account
        fields = ["id", "name", "avatar"]

    @classmethod
    def resolve_name(cls, info: Account, *args, **kwargs):
        return info.profile and info.profile.full_name or ""

    @classmethod
    def resolve_avatar(cls, info: Account, *args, **kwargs):
        return info.profile and info.profile.avatar
