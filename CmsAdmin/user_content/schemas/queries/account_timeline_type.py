import graphene


class MediaDataType(graphene.ObjectType):
    url = graphene.String(description="Url")
    type = graphene.Int(description="Type")


class ArticlePostType(graphene.ObjectType):
    id = graphene.String(description="Id")
    account_id = graphene.String(description="Account id")
    content = graphene.String(description="Content")
    medias = graphene.List(MediaDataType, description="medias")


class AccountTimeLineType(graphene.ObjectType):
    article_posts = graphene.List(ArticlePostType, description="Article posts")
