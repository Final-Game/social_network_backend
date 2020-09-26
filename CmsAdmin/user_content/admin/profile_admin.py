from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from user_content.models import Profile


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ["avatar", "email", "phone_number", "full_name", "gender"]
    list_display_links = ["avatar"]
    fields = [
        "avatar",
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
    ]
