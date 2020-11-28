import graphene
from .test_mutation import TestMutation
from .register_account_mutation import RegisterAccountMutation
from .login_account_mutation import LoginAccountMutation
from .change_account_password_mutation import ChangeAccountPasswordMutation
from .update_account_profile_mutation import UpdateAccountProfileMutation


class Mutation(graphene.ObjectType):
    test = TestMutation.Field()
    register_account = RegisterAccountMutation.Field()
    login_account = LoginAccountMutation.Field()
    change_account_password = ChangeAccountPasswordMutation.Field()
    update_account_profile = UpdateAccountProfileMutation.Field()