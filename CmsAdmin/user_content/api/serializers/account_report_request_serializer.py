from user_content.app.dtos.report_user_dto import ReportUserDto
from rest_framework import serializers


class AccountReportRequestSerializer(serializers.Serializer):
    receiver_id = serializers.CharField(help_text="Receiver id")
    reason = serializers.CharField(help_text="reason")

    def create(self, validated_data):
        return ReportUserDto(**validated_data)