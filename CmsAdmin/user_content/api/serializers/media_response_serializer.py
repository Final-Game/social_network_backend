from rest_framework import serializers


class MediaReponseSerializer(serializers.Serializer):
    url = serializers.CharField(help_text="Url")
    type = serializers.IntegerField(help_text="Type")

    class Meta:
        fields = ["url", "type"]
