from chat_management.api.schemas.queries.media_type import MediaType
import graphene


class MatcherInfoType(graphene.ObjectType):
    matcher_id = graphene.String(description="Matcher id")
    name = graphene.String(description="Name")
    age = graphene.Int(description="Age")
    gender = graphene.Int(description="Gender")
    address = graphene.String(description="Address")
    job = graphene.String(description="Job")
    reason = graphene.String(description="Reason")
    medias = graphene.List(MediaType, description="Medias")
    status = graphene.Int(description="Status")
