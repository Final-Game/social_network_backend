from user_content.domain.managers.account_manager import AccountManager
from user_content.domain.enums.account_type_enum import AccountTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel
from django.contrib.auth.hashers import make_password


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

    objects: AccountManager = AccountManager()

    def save(self, *args, **kwargs) -> None:
        self.profile.save()
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
