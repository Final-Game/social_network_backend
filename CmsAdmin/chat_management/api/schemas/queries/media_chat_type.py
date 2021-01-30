import graphene


class MediaChatType(graphene.ObjectType):
    url = graphene.String(description="Url")
    type = graphene.Int(description="Type")
