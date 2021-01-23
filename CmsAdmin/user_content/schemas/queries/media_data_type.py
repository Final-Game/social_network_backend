import graphene


class MediaDataType(graphene.ObjectType):
    url = graphene.String(description="Url")
    type = graphene.String(description="Type")
