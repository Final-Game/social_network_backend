from graphene_django import DjangoObjectType
import graphene
from user_content.schemas import Mutation as UC_Mutation, Query as UC_Query
from chat_management.api.schemas import Mutation as CM_Mutation, Query as CM_Query


class Query(CM_Query, UC_Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(UC_Mutation, CM_Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
