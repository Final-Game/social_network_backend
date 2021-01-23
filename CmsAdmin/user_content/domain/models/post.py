from user_content.domain.enums.post_type_enum import PostTypeEnum
from user_content.domain.managers.post_manager import PostManager
from user_content.domain.enums.model_status_enum import ModelStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class Post(BaseModel):
    own_reaction = models.IntegerField(null=True, blank=True, help_text="User feeling")
    account = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, blank=True, null=True, max_length=36
    )
    content = models.CharField(max_length=500, null=True, blank=True)
    type = models.IntegerField(
        default=1,
        null=False,
        blank=False,
        help_text="type hide from timeline",
        choices=PostTypeEnum.to_choices(),
    )
    base = models.ForeignKey(
        to="self", on_delete=models.SET_NULL, blank=True, null=True
    )

    medias = models.ManyToManyField(
        "media_content.Media",
        through="media_content.MediaPost",
        through_fields=["post", "media"],
    )

    status = models.IntegerField(
        blank=False,
        null=False,
        choices=ModelStatusEnum.to_choices(),
        default=int(ModelStatusEnum.ACTIVE),
    )

    objects: PostManager = PostManager()

    @classmethod
    def create_new_post(cls, account, content: str):
        return cls(account=account, content=content)
