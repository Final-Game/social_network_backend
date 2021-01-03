from user_content.app.dtos.account_info_dto import AccountInfoDto
from user_content.api.serializers.account_info_response_serializer import (
    AccountInfoResponseSerializer,
)
from user_content.app.queries.get_account_info_query import GetAccountInfoQuery
from rest_framework.decorators import api_view

from core.api import response
from core.app.bus import Bus

__bus: Bus = Bus()


@api_view(["GET"])
def account_info_api(request, *args, **kwargs):
    account_id: str = kwargs["account_id"]

    account_info_dto: AccountInfoDto = __bus.dispatch(GetAccountInfoQuery(account_id))
    return response.success(
        AccountInfoResponseSerializer(account_info_dto.__dict__).data
    )
