import graphene

from graphene_django.types import DjangoObjectType


class TestType(graphene.ObjectType):
    x = graphene.String(default_value="abc")

    class Meta:
        fields = ["x"]
