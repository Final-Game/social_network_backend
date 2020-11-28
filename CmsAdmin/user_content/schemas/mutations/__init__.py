import graphene
from .test_mutation import TestMutation
from .register_account_mutation import RegisterAccountMutation
from .login_account_mutation import LoginAccountMutation
from .change_account_password_mutation import ChangeAccountPasswordMutation


class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()
    register_account_mutation = RegisterAccountMutation.Field()
    login_account_mutation = LoginAccountMutation.Field()
    change_account_password_mutation = ChangeAccountPasswordMutation.Field()