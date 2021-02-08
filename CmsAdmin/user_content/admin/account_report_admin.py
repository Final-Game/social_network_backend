from django.contrib import admin
from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from user_content.models import AccountReport


@admin.register(AccountReport)
class AccountReportAdmin(BaseAdmin):
    list_display = [
        linkify("sender"),
        linkify("receiver"),
        linkify("related_post"),
        "reason",
        "status",
    ]
    list_filter = ["status"]
    list_display_links = []
    fields = ["sender", "receiver", "related_post", "reason", "status"]
