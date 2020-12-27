from chat_management.app.dtos.create_match_dto import CreateMatchDto
from core.services.grpc_service import GrpcService
from chat_management.app.services.match_service import MatchService

from codegen_protos.match_service_pb2 import CreateMatchRequest, CreateMatchReply
from codegen_protos.match_service_pb2_grpc import MatchServiceStub


class MatchServiceImpl(GrpcService, MatchService):
    def __init__(self, *args, **kwargs) -> None:
        GrpcService.__init__(self)
        MatchService.__init__(self)

    async def create_match(self, account_id: str, dto: CreateMatchDto):
        async with self.get_connection() as channel:
            stub = MatchServiceStub(channel)
            response = await stub.CreateMatch(
                CreateMatchRequest(
                    sender_id=account_id, receiver_id=dto.receiver_id, status=dto.status
                )
            )

        print("Greeter client received: " + response.status)
