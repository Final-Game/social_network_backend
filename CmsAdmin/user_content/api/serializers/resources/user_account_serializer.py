from rest_framework import serializers
from user_content.models import Account
from datetime import date


class UserAccountSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source="get_avatar")
    name = serializers.SerializerMethodField(source="get_name")
    phone_number = serializers.SerializerMethodField(source="get_phone_number")
    marital_status = serializers.SerializerMethodField(source="get_marital_status")
    age = serializers.SerializerMethodField(source="get_age")
    created_date = serializers.DateTimeField(source="created_at")
    updated_date = serializers.DateTimeField(source="updated_at")

    class Meta:
        fields = [
            "id",
            "avatar",
            "name",
            "phone_number",
            "marital_status",
            "age",
            "created_date",
            "updated_date",
        ]
        model = Account

    def get_avatar(self, account: Account):
        return account.profile and account.profile.avatar

    def get_name(self, account: Account):
        return account.profile and account.profile.full_name

    def get_phone_number(self, account: Account):
        return account.profile and account.profile.phone_number

    def get_marital_status(self, account: Account):
        return account.profile and account.profile.marital_status

    def get_age(self, account: Account):
        return (
            account.profile
            and account.profile.birth_date
            and calculate_age(account.profile.birth_date)
        )


def calculate_age(birth_date):
    today = date.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )

    return age
