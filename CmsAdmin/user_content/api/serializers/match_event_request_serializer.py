from rest_framework import serializers


class MatchEventRequestSerializer(serializers.Serializer):
    account_id = serializers.CharField(help_text="Account id")
    partner_id = serializers.CharField(help_text="Parner id")