from typing import Optional, Sequence
from django.contrib import admin
from django.http import HttpRequest


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = "--empty--"

    def get_list_display_links(
        self, request: HttpRequest, list_display: Sequence[str]
    ) -> Optional[Sequence[str]]:
        return ["short_id"] + list(self.list_display_links) or []

    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        return ["short_id"] + (self.list_display or []) + ["created_at", "updated_at"]
