import graphene
from .media_chat_type import MediaChatType


class MessageChatType(graphene.ObjectType):
    id = graphene.String(description="Id")
    sender_id = graphene.String(description="Sender id")
    content = graphene.String(description="Content")
    created_at = graphene.DateTime(description="Create ad")
    media_data = graphene.List(MediaChatType, description="list of media")
