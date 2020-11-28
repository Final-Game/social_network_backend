import graphene
from .test_mutation import TestMutation
from .register_account_mutation import RegisterAccountMutation
from .login_account_mutation import LoginAccountMutation


class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()
    register_account_mutation = RegisterAccountMutation.Field()
    login_account_mutation = LoginAccountMutation.Field()