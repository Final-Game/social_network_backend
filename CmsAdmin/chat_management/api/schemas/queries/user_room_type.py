import graphene


class UserRoomType(graphene.ObjectType):
    id = graphene.String(description="Id")
    avt_icon_url = graphene.String(description="Avt icon url")
    name = graphene.String(description="Name")
    latest_msg = graphene.String(description="Latest msg")
    latest_msg_time = graphene.DateTime(description="Latest msg time")
    num_un_read_msg = graphene.Int(description="Number of unread messages")
