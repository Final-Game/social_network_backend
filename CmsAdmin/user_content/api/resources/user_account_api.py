from user_content.api.serializers.resources.user_account_serializer import (
    UserAccountSerializer,
)
from user_content.domain.models.account import Account
from rest_framework.viewsets import ModelViewSet


class UserAccountApi(ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = UserAccountSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)