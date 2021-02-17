import graphene
from .test_mutation import TestMutation
from .register_account_mutation import RegisterAccountMutation
from .login_account_mutation import LoginAccountMutation
from .change_account_password_mutation import ChangeAccountPasswordMutation
from .update_account_profile_mutation import UpdateAccountProfileMutation
from .user_create_post_mutation import UserCreatePostMutation
from .user_comment_in_post_mutation import UserCommentInPostMutation
from .user_react_post_mutation import UserReactPostMutation
from .user_react_comment_mutation import UserReactCommentMutation
from .user_delete_comment_mutation import UserDeleteCommentMutation
from .user_delete_post_mutation import UserDeletePostMutation
from .user_follow_user_mutation import UserFollowUserMutation
from .user_create_story_mutation import UserCreateStoryMutation
from .user_view_story_mutation import UserViewStoryMutation
from .user_delete_story_mutation import UserDeleteStoryMutation
from .verify_account_mutation import AccountVerifyMutation


class Mutation(graphene.ObjectType):
    test = TestMutation.Field()
    register_account = RegisterAccountMutation.Field()
    login_account = LoginAccountMutation.Field()
    change_account_password = ChangeAccountPasswordMutation.Field()
    update_account_profile = UpdateAccountProfileMutation.Field()
    user_create_post = UserCreatePostMutation.Field()
    user_comment_in_post = UserCommentInPostMutation.Field()
    user_react_post = UserReactPostMutation.Field()
    user_react_comment = UserReactCommentMutation.Field()
    user_delete_comment = UserDeleteCommentMutation.Field()
    user_delete_post = UserDeletePostMutation.Field()
    user_follow_user = UserFollowUserMutation.Field()
    user_create_story = UserCreateStoryMutation.Field()
    user_view_story = UserViewStoryMutation.Field()
    user_delete_story = UserDeleteStoryMutation.Field()
    account_verify = AccountVerifyMutation.Field()