from django.contrib import admin
from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from chat_management.models import AccountMapper


@admin.register(AccountMapper)
class AccountMapperAdmin(BaseAdmin):
    list_display = [linkify("ref"), "full_name", "gender", "address"]
    list_display_links = ["full_name"]
    search_fields = ["id", "full_name"]
    fields = [
        "ref",
        "avatar",
        "birth_date",
        "gender",
        "full_name",
        "bio",
        "address",
        "job",
        "reason",
    ]
