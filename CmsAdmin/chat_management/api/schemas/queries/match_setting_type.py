import graphene


class MatchSettingType(graphene.ObjectType):
    min_age = graphene.Int(description="min age")
    max_age = graphene.Int(description="max age")
    max_distance = graphene.Float(description="Max distance")
    target_gender = graphene.String(description="Gender")
