from user_content.domain.enums.account_report_status_enum import AccountReportStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class AccountReport(BaseModel):
    sender = models.ForeignKey(
        to="Account",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="sender_account",
    )
    receiver = models.ForeignKey(
        to="Account",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="receiver_account",
    )
    related_post = models.ForeignKey(
        to="Post", on_delete=models.SET_NULL, blank=True, null=True
    )
    reason = models.TextField(blank=True, null=True)
    status = models.IntegerField(
        blank=True,
        null=True,
        default=AccountReportStatusEnum.UN_RESOLVED.value,
        choices=AccountReportStatusEnum.to_choices(),
    )

    class Meta:
        db_table = "uc_account_reports"
