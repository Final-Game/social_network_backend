import graphene


class UserCommentType(graphene.ObjectType):
    id = graphene.String(description="Comment id")
    account_id = graphene.String(description="Account id")
    content = graphene.String(description="Comment content")
    # child_comments = graphene.List("self", description="Base id")
