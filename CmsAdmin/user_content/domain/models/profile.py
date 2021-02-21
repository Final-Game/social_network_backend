from datetime import date
from user_content.domain.enums.marital_status_enum import MaritalStatusEnum
from user_content.domain.enums.account_gender_enum import AccountGenderEnum
from django.db import models

from core.domain.models.base_model import BaseModel


class Profile(BaseModel):
    avatar = models.CharField(
        blank=True, null=True, max_length=200, help_text="Avatar url"
    )
    cover = models.CharField(
        blank=True, null=True, max_length=200, help_text="Cover url"
    )
    email = models.CharField(blank=True, null=True, max_length=30, unique=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    first_name = models.CharField(blank=True, null=True, max_length=15)
    last_name = models.CharField(blank=True, null=True, max_length=15)
    gender = models.IntegerField(
        blank=True,
        null=True,
        choices=AccountGenderEnum.to_choices(),
    )

    marital_status = models.IntegerField(
        blank=True,
        null=True,
        help_text="Marital status: 0 - Single, 1 - Got married",
        choices=MaritalStatusEnum.to_choices(),
    )
    birth_date = models.DateField(blank=True, null=True)
    school = models.CharField(blank=True, null=True, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=200)
    bio = models.CharField(blank=True, null=True, max_length=500)
    reason_dating = models.CharField(blank=True, null=True, max_length=256)

    def __str__(
        self,
    ) -> str:
        return super().__str__() + f" - {self.email}"

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}"

    def update_data(
        self,
        avatar: str,
        cover: str,
        email: str,
        phone_number: str,
        first_name: str,
        last_name: str,
        gender: int,
        marital_status: int,
        birth_date: date,
        school: str,
        address: str,
        bio: str,
    ):
        # self.avatar = avatar
        # self.cover, self.email,
        self.phone_number = phone_number
        self.first_name, self.last_name = first_name, last_name
        self.gender, self.birth_date = (
            gender,
            birth_date,
        )
        self.school, self.address, self.bio = school, address, bio

    def create_collection(self):
        from user_content.models import Collection

        return Collection.objects.create(profile_id=self.id)

    def update_avatar(self, media_url: str):
        self.avatar = media_url
