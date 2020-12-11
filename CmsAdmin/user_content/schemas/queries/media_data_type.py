import graphene


class MediaDataType(graphene.ObjectType):
    url = graphene.String(description="Url")
    type = graphene.Int(description="Type")
