from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from user_content.models import Profile
from django.utils.html import format_html


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = [
        "avatar_image",
        "cover_image",
        "email",
        "phone_number",
        "full_name",
        "gender",
    ]
    list_display_links = ["avatar"]
    fields = [
        "avatar",
        "cover",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "gender",
        "marital_status",
        "birth_date",
        "school",
        "address",
        "bio",
        "reason_dating",
    ]

    def avatar_image(self, obj):
        return format_html(
            '<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.avatar)
        )

    def cover_image(self, obj: Profile):
        return format_html(
            '<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.cover)
        )
