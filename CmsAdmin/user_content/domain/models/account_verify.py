from user_content.domain.enums.verify_status_enum import VerifyStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class AccountVerify(BaseModel):
    account = models.OneToOneField(
        "Account", on_delete=models.CASCADE, blank=False, null=False
    )
    front_photo_url = models.TextField(blank=True, null=True)
    back_photo_url = models.TextField(blank=True, null=True)
    status = models.IntegerField(
        blank=True,
        null=True,
        default=VerifyStatusEnum.PENDING.value,
        choices=VerifyStatusEnum.to_choices(),
    )

    class Meta:
        db_table = "uc_account_verifies"

    def update_data(self, front_photo_url: str, back_photo_url: str):
        self.front_photo_url = front_photo_url
        self.back_photo_url = back_photo_url

    def set_pending(self):
        self.status = VerifyStatusEnum.PENDING.value