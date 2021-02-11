import graphene


class MediaType(graphene.ObjectType):
    type = graphene.Int(description="Type")
    url = graphene.String(description="Url")
