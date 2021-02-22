import graphene


class RoomInfoType(graphene.ObjectType):
    id = graphene.String(description="id")
    partner_id = graphene.String(description="partner id")
    partner_name = graphene.String(description="partner name")
