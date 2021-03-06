from user_content.api.match_event_api import match_event_api
from user_content.api.account_report_api import account_report_api
from user_content.api.resources.account_verify_api import AccountVerifyApi
from user_content.api.resources.user_account_api import UserAccountApi
from user_content.api.resources.account_report_api import AccountReportApi
from django.urls import path
from user_content.api import account_info_api
from django.conf.urls import url

cms_urlpatterns = [
    url(r"^user_accounts/$", UserAccountApi.as_view({"get": "list", "post": "create"})),
    url(
        r"^user_accounts/(?P<pk>[\w-]+)/$",
        UserAccountApi.as_view({"get": "retrieve", "put": "update"}),
    ),
    url(
        r"^account_verifies/$",
        AccountVerifyApi.as_view({"get": "list", "post": "create"}),
    ),
    url(
        r"^account_verifies/(?P<pk>[\w-]+)/$",
        AccountVerifyApi.as_view({"get": "retrieve", "put": "update"}),
    ),
    url(
        r"^account_reports/$",
        AccountReportApi.as_view({"get": "list", "post": "create"}),
    ),
    url(
        r"^account_reports/(?P<pk>[\w-]+)/$",
        AccountReportApi.as_view({"get": "retrieve", "put": "update"}),
    ),
]


urlpatterns = [
    url(r"^accounts/(?P<account_id>[\w-]+)/info$", account_info_api),
    url(r"^accounts/(?P<account_id>[\w-]+)/report$", account_report_api),
    url(r"^match_events$", match_event_api),
] + cms_urlpatterns
