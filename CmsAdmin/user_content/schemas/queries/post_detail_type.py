from user_content.schemas.queries.media_data_type import MediaDataType
import graphene
from .user_comment_type import UserCommentType
from .post_react_type import PostReactType


class PostDetailType(graphene.ObjectType):
    id = graphene.String(description="Id")
    content = graphene.String(description="Content")
    medias = graphene.List(MediaDataType, description="medias")
    user_comment_count = graphene.Int(description="User comment count")
    user_react_count = graphene.Int(description="User react count")
    user_comments = graphene.List(UserCommentType, description="List user comment")
    user_reacts = graphene.List(PostReactType, description="Post reacts")
