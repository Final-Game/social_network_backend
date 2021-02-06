from user_content.api.resources.filters.account_verify_filter import AccountVerifyFilter
from user_content.api.serializers.resources.account_verify_serializer import (
    AccountVerifySerializer,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from user_content.models import AccountVerify
from core.api.rest_frameworks import StandardResultsSetPagination
from core.api.rest_frameworks.order_filter import CustomOrderingFilter


class AccountVerifyApi(ModelViewSet):
    queryset = AccountVerify.objects.all()
    serializer_class = AccountVerifySerializer
    filter_class = AccountVerifyFilter
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        SearchFilter,
        OrderingFilter,
        CustomOrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["account__profile__first_name", "account__profile__last_name"]
    ordering_fields = ["created_at", "updated_at"]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
