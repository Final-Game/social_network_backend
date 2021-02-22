import graphene
from .matcher_data_type import MatcherDataType


class MatchingDataType(graphene.ObjectType):
    num_smart_chat_users = graphene.Int(description="Number of smart chat users active")
    num_traditional_match_users = graphene.Int(
        description="Number of traditional match users"
    )
    nearly_users = graphene.List(MatcherDataType, description="Nearly users")
