from django_filters import FilterSet, NumberFilter
from django.db.models import Q

from user_content.domain.models.account_verify import AccountVerify


class AccountVerifyFilter(FilterSet):
    class Meta:
        model = AccountVerify
        fields = ["status"]