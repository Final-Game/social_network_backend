from user_content.domain.enums.marital_status_enum import MaritalStatusEnum
from user_content.domain.enums.account_gender_enum import AccountGenderEnum
import graphene
from graphene.types.objecttype import ObjectType

from graphene_django.types import DjangoObjectType
from user_content.models import Profile


class AccountProfileType(DjangoObjectType):
    avatar_url = graphene.Field(type=graphene.String, source="avatar")
    cover_url = graphene.Field(type=graphene.String, source="cover")
    gender = graphene.Field(
        type=graphene.String,
    )
    marital_status = graphene.Field(
        type=graphene.String,
    )

    class Meta:
        model = Profile
        fields = [
            "avatar_url",
            "cover_url",
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "gender",
            "marital_status",
            "birth_date",
            "school",
            "address",
            "bio",
        ]

    @classmethod
    def resolve_gender(cls, info, *args, **kwargs):
        return AccountGenderEnum.to_value(info.gender)

    @classmethod
    def resolve_marital_status(cls, info, *args, **kwargs):
        return MaritalStatusEnum.to_value(info.marital_status)
