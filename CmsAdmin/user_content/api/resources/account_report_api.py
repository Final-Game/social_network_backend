from user_content.domain.enums.account_status_enum import AccountStatusEnum
from django.db.models import Q
from user_content.api.serializers.resources.account_report_serializer import (
    AccountReportSerializer,
)
from user_content.api.resources.filters.account_report_filter import AccountReportFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from core.api.rest_frameworks import StandardResultsSetPagination
from core.api.rest_frameworks.order_filter import CustomOrderingFilter
from user_content.models import AccountReport


class AccountReportApi(ModelViewSet):
    queryset = AccountReport.objects.filter(
        ~Q(receiver__status=AccountStatusEnum.BANNED.value)
    )
    serializer_class = AccountReportSerializer
    filter_class = AccountReportFilter
    pagination_class = StandardResultsSetPagination

    search_fields = [
        "sender__profile__last_name",
        "sender__profile__first_name",
        "receiver__profile__last_name",
        "receiver__profile__first_name",
    ]
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        CustomOrderingFilter,
        DjangoFilterBackend,
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