import graphene
from graphene_django import DjangoObjectType
from user_content.models import Account


class UserStoryMediaType(graphene.ObjectType):
    media_url = graphene.String(description="Media url")
    content = graphene.String(description="Content")
    id = graphene.String(description="story id")

    class Meta:
        fields = ["content", "media_url", "id"]


class UserStoryDataType(graphene.ObjectType):
    id = graphene.String(description="User id")
    name = graphene.String(description="Name of user")
    media_datas = graphene.List(UserStoryMediaType, description="List of media data")

    class Meta:
        fields = ["id", "name", "media_datas"]
