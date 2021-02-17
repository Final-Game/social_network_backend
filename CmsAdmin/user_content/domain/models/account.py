from typing import List
from user_content.domain.enums.verify_status_enum import VerifyStatusEnum
from user_content.domain.enums.account_status_enum import AccountStatusEnum
from user_content.domain.managers.account_manager import AccountManager
from user_content.domain.enums.account_type_enum import AccountTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel
from django.contrib.auth.hashers import check_password, make_password


class Account(BaseModel):
    username = models.CharField(blank=False, null=False, max_length=50, unique=True)
    password = models.CharField(blank=False, null=False, max_length=250)
    connection = models.OneToOneField(
        to="Connection", on_delete=models.SET_NULL, blank=True, null=True
    )
    profile = models.OneToOneField(
        to="Profile", on_delete=models.SET_NULL, blank=True, null=True
    )
    type = models.IntegerField(
        blank=False,
        null=False,
        default=int(AccountTypeEnum.NORMAL),
        choices=AccountTypeEnum.to_choices(),
    )
    followers = models.ManyToManyField(
        "self",
        through="UserFollow",
        through_fields=["target", "source"],
        symmetrical=False,
    )

    following_users = models.ManyToManyField(
        "self",
        through="UserFollow",
        through_fields=["source", "target"],
        symmetrical=False,
        related_name="following_user_relate",
    )
    reporters = models.ManyToManyField(
        "self",
        through="AccountReport",
        through_fields=["receiver", "sender"],
        symmetrical=False,
        related_name="account_reporter_relate",
    )
    status = models.IntegerField(
        null=True,
        blank=True,
        default=AccountStatusEnum.ACTIVE.value,
        choices=AccountStatusEnum.to_choices(),
    )

    objects: AccountManager = AccountManager()

    class Meta:
        db_table = "uc_accounts"

    def __str__(self) -> str:
        return super().__str__() + f" {self.username}"

    def save(self, *args, **kwargs) -> None:
        if self.profile:
            self.profile.save()

        # support create account over django admin.
        old_account = Account.objects.find_account_by_id(self.id)
        if old_account and not (
            old_account.password == self.password
            or check_password(self.password, old_account.password)
        ):
            self.password = make_password(self.password)

        super(Account, self).save(*args, **kwargs)

    def generate_token(self):
        from user_content.domain.models import AccessToken

        access_token: AccessToken = AccessToken.objects.create(sub=self)
        return {
            "auth_token": access_token.generate_token(),
            "refresh_token": access_token.generate_token(is_refresh=True),
        }

    def change_password(self, new_password):
        self.password = make_password(new_password)

    def get_verify_status(self) -> int:
        from user_content.models import AccountVerify

        account_verify: AccountVerify = getattr(self, "accountverify", None)
        if not account_verify:
            return VerifyStatusEnum.NOT_VERIFIED.value

        return account_verify.status

    @property
    def article_posts(self):
        return list(self.post_set.order_by("-created_at"))

    @classmethod
    def check_email(cls, email: str):
        from user_content.domain.models.profile import Profile

        return Profile.objects.filter(email=email).first() is None

    @classmethod
    def check_username(cls, username: str):
        return cls.objects.filter(username=username).first() is None

    @classmethod
    def new_normal_account(cls, username: str, password: str, email: str):
        from user_content.domain.models.profile import Profile

        profile: Profile = Profile.objects.create(email=email)

        return cls(
            username=username,
            password=make_password(password),
            type=int(AccountTypeEnum.NORMAL),
            profile=profile,
        )
