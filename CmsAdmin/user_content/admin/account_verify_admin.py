from django.contrib import admin
from django.utils.html import format_html

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin
from user_content.models import AccountVerify


@admin.register(AccountVerify)
class AccountVerifyAdmin(BaseAdmin):
    list_display = [linkify("account"), "front_photo", "back_photo", "status"]
    list_display_links = []
    fields = ["account", "front_photo_url", "back_photo_url", "status"]

    def front_photo(self, obj: AccountVerify):
        return format_html(
            '<img src="{0}" style="width: 45px; height:45px;" />'.format(
                obj.front_photo_url
            )
        )

    def back_photo(self, obj: AccountVerify):
        return format_html(
            '<img src="{0}" style="width: 45px; height:45px;" />'.format(
                obj.back_photo_url
            )
        )
