from core.api.rest_frameworks.order_filter import CustomOrderingFilter
from user_content.api.serializers.resources.user_account_serializer import (
    UserAccountSerializer,
)
from user_content.domain.models.account import Account
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from core.api.rest_frameworks import StandardResultsSetPagination
from .filters import UserAccountFilter


class UserAccountApi(ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = UserAccountSerializer
    filter_class = UserAccountFilter
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
        CustomOrderingFilter,
    ]

    search_fields = [
        "profile__first_name",
        "profile__last_name",
        "profile__phone_number",
    ]
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