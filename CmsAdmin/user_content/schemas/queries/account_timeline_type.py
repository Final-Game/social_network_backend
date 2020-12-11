import graphene
from .article_post_type import ArticlePostType
from .media_data_type import MediaDataType


class AccountTimeLineType(graphene.ObjectType):
    article_posts = graphene.List(ArticlePostType, description="Article posts")
