from typing import List
from core.authenticates.base_authentication import BaseAuthentication
import graphene


def authenticate_permission(method):
    def inner(ref, *args, **kwargs):
        ref.authenticate(*args, **kwargs)
        return method(ref, *args, **kwargs)

    return inner


class BaseMutation(graphene.Mutation):
    authentication_classes: List[BaseAuthentication] = []

    @classmethod
    def authenticate(cls, *args, **kwargs):
        for auth_class in cls.authentication_classes:
            auth_class.check_permission(
                auth_token=kwargs.pop("auth_token"), account_id=kwargs.get("account_id")
            )

        return True

    @classmethod
    def mutate(cls, *args, **kwargs):
        return cls(*args, **kwargs)