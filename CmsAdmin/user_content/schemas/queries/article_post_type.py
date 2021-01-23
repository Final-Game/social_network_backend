import graphene
from .media_data_type import MediaDataType


class ArticlePostType(graphene.ObjectType):
    id = graphene.String(description="Id")
    account_id = graphene.String(description="Account id")
    content = graphene.String(description="Content")
    medias = graphene.List(MediaDataType, description="medias")
    user_comment_count = graphene.Int(description="User comment count")
    user_react_count = graphene.Int(description="User react count")
