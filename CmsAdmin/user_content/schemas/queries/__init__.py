import graphene

from .test_type import TestType


class Query(graphene.ObjectType):
    abc = graphene.Field(TestType)

    def resolve_abc(self, *args, **kwargs):
        return TestType(x="Nguyen Minh Tuan")