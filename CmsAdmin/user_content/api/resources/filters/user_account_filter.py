from django_filters.filters import CharFilter
from user_content.domain.models.account import Account
from django_filters import FilterSet, NumberFilter
from django.db.models import Q


class UserAccountFilter(FilterSet):
    marital_status = NumberFilter(field_name="profile__marital_status")

    class Meta:
        model = Account
        fields = ["marital_status", "status"]