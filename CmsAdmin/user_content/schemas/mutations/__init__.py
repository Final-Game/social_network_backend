import graphene
from .test_mutation import TestMutation


class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()