from django_filters import FilterSet
from user_content.domain.models.account_report import AccountReport


class AccountReportFilter(FilterSet):
    class Meta:
        model = AccountReport
        fields = ["status"]