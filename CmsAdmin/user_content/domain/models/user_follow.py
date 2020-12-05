from user_content.domain.exceptions.uc_domain_exception import UcDomainException
from django.db import models
from core.domain.models.base_model import BaseModel


class UserFollow(BaseModel):
    source = models.ForeignKey(
        to="Account",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="source_follow",
    )
    target = models.ForeignKey(
        to="Account",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="target_follow",
    )

    def save(self, *args, **kwargs) -> None:
        if self.target == self.source:
            raise UcDomainException("Invalid data.")
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ["source", "target"]
