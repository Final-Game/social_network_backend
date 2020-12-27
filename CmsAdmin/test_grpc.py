from chat_management.app.dtos.create_match_dto import CreateMatchDto
from chat_management.infras.service_impls.match_service_impl import MatchServiceImpl
from chat_management.app.services.match_service import MatchService
import logging
import grpc
import asyncio


# async def run() -> None:
#     async with grpc.aio.insecure_channel("localhost:50051") as channel:
#         # stub = hello_pb2_grpc.GreeterStub(channel)
#         # response = await stub.SayHello(hello_pb2.HelloRequest(name="you"))

#         stub = match_service_pb2_grpc.MatchServiceStub(channel)
#         response = await stub.CreateMatch(
#             match_service_pb2.CreateMatchRequest(
#                 sender_id="1234", receiver_id="1234", status=123
#             )
#         )
#     print("Greeter client received: " + response.status)

_match_service: MatchService = MatchServiceImpl()


def test_create_match():
    asyncio.run(_match_service.create_match("123", CreateMatchDto("123", 1)))


def run_test():
    logging.basicConfig()
    test_create_match()