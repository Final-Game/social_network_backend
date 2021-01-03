from rest_framework import serializers


class AccountInfoResponseSerializer(serializers.Serializer):
    id = serializers.CharField(help_text="account id")
    full_name = serializers.CharField(help_text="Full name")
    avatar = serializers.CharField(help_text="Avatar url")
    birth_date = serializers.DateField(help_text="Birth date")
    gender = serializers.IntegerField(help_text="Gender")

    class Meta:
        fields = ["id", "full_name", "avatar", "birth_date", "gender"]
