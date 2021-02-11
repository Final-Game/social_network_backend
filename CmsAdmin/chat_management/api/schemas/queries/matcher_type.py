from chat_management.api.schemas.queries.media_type import MediaType
import graphene


class MatcherType(graphene.ObjectType):
    matcher_id = graphene.String(description="Matcher id")
    name = graphene.String(description="Name")
    age = graphene.Int(description="Age")
    bio = graphene.String(description="Bio")
    status = graphene.Int(description="Status")
    medias = graphene.List(MediaType, description="Medias")
