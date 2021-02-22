import graphene


class MatcherDataType(graphene.ObjectType):
    id = graphene.String(description="Id")
    avatar = graphene.String(description="Avatar")
    name = graphene.String(description="Name")
    bio = graphene.String(description="Bio")
    age = graphene.Int(description="Age")
    gender = graphene.Int(description="Gender")