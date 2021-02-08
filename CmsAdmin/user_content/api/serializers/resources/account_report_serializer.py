from rest_framework import serializers
from user_content.models import AccountReport


class AccountReportSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(source="created_at")
    updated_date = serializers.DateTimeField(source="updated_at")
    short_reason = serializers.SerializerMethodField(source="get_short_reason")

    class Meta:
        model = AccountReport
        fields = [
            "id",
            "short_id",
            "sender_id",
            "receiver_id",
            "related_post_id",
            "short_reason",
            "reason",
            "status",
            "updated_date",
            "created_date",
        ]

    def get_short_reason(self, instance: AccountReport) -> str:
        return instance.reason and instance.reason[:15]