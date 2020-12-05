from datetime import datetime, timedelta
from user_content.domain.managers.user_story_manager import UserStoryManager
from user_content.domain.exceptions.uc_domain_exception import UcDomainException
from user_content.domain.enums.model_status_enum import ModelStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class UserStory(BaseModel):
    account = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, blank=True, null=True
    )
    content = models.CharField(max_length=300, null=True, blank=True)
    media_url = models.CharField(max_length=500, null=True, blank=True)

    status = models.IntegerField(
        blank=False,
        null=False,
        choices=ModelStatusEnum.to_choices(),
        default=int(ModelStatusEnum.ACTIVE),
    )

    viewers = models.ManyToManyField(
        "Account",
        through="StoryViewer",
        through_fields=["story", "viewer"],
        related_name="story_viewers",
    )

    objects: UserStoryManager = UserStoryManager()

    def save(self, *args, **kwargs) -> None:
        if not (self.media_url or self.content):
            raise UcDomainException("Invalid data")
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "user_content_user_story"

    def is_visible(self) -> bool:
        import pytz

        threshold: datetime = datetime.utcnow().replace(tzinfo=pytz.UTC) - timedelta(
            days=1
        )
        return self.created_at > threshold
