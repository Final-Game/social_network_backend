from rest_framework import serializers

from user_content.models import AccountVerify


class AccountVerifySerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(source="created_at")
    updated_date = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = AccountVerify
        fields = [
            "id",
            "short_id",
            "account_id",
            "front_photo_url",
            "back_photo_url",
            "status",
            "updated_date",
            "created_date",
        ]