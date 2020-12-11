import graphene
from .article_post_type import ArticlePostType


class AccountHomePageType(graphene.ObjectType):
    article_posts = graphene.List(ArticlePostType, description="Article posts")
