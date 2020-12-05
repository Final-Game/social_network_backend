import graphene
from .test_mutation import TestMutation
from .register_account_mutation import RegisterAccountMutation
from .login_account_mutation import LoginAccountMutation
from .change_account_password_mutation import ChangeAccountPasswordMutation
from .update_account_profile_mutation import UpdateAccountProfileMutation
from .user_create_post_mutation import UserCreatePostMutation
from .user_comment_in_post_mutation import UserCommentInPostMutation


class Mutation(graphene.ObjectType):
    test = TestMutation.Field()
    register_account = RegisterAccountMutation.Field()
    login_account = LoginAccountMutation.Field()
    change_account_password = ChangeAccountPasswordMutation.Field()
    update_account_profile = UpdateAccountProfileMutation.Field()
    user_create_post = UserCreatePostMutation.Field()
    user_comment_in_post = UserCommentInPostMutation.Field()