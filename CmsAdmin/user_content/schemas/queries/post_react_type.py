from typing import List
import graphene


class PostReactType(graphene.ObjectType):
    type = graphene.String(description="React type")
    account_ids = graphene.List(graphene.String, description="list of account id")
