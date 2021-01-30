# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import interactive_main_service_pb2 as interactive__main__service__pb2


class MatchServiceV1Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAccountMatchSetting = channel.unary_unary(
            "/interactive_main_service.MatchServiceV1/GetAccountMatchSetting",
            request_serializer=interactive__main__service__pb2.GetAccountMatchSettingRequest.SerializeToString,
            response_deserializer=interactive__main__service__pb2.GetAccountMatchSettingReply.FromString,
        )
        self.UpdateAccountMatchSetting = channel.unary_unary(
            "/interactive_main_service.MatchServiceV1/UpdateAccountMatchSetting",
            request_serializer=interactive__main__service__pb2.UpdateAccountMatchSettingRequest.SerializeToString,
            response_deserializer=interactive__main__service__pb2.UpdateAccountMatchSettingReply.FromString,
        )


class MatchServiceV1Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAccountMatchSetting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateAccountMatchSetting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MatchServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetAccountMatchSetting": grpc.unary_unary_rpc_method_handler(
            servicer.GetAccountMatchSetting,
            request_deserializer=interactive__main__service__pb2.GetAccountMatchSettingRequest.FromString,
            response_serializer=interactive__main__service__pb2.GetAccountMatchSettingReply.SerializeToString,
        ),
        "UpdateAccountMatchSetting": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateAccountMatchSetting,
            request_deserializer=interactive__main__service__pb2.UpdateAccountMatchSettingRequest.FromString,
            response_serializer=interactive__main__service__pb2.UpdateAccountMatchSettingReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "interactive_main_service.MatchServiceV1", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MatchServiceV1(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAccountMatchSetting(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/interactive_main_service.MatchServiceV1/GetAccountMatchSetting",
            interactive__main__service__pb2.GetAccountMatchSettingRequest.SerializeToString,
            interactive__main__service__pb2.GetAccountMatchSettingReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateAccountMatchSetting(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/interactive_main_service.MatchServiceV1/UpdateAccountMatchSetting",
            interactive__main__service__pb2.UpdateAccountMatchSettingRequest.SerializeToString,
            interactive__main__service__pb2.UpdateAccountMatchSettingReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRoomChat = channel.unary_unary(
            "/interactive_main_service.ChatService/CreateRoomChat",
            request_serializer=interactive__main__service__pb2.CreateRoomChatRequest.SerializeToString,
            response_deserializer=interactive__main__service__pb2.CreateRoomChatReply.FromString,
        )
        self.GetListRoomChat = channel.unary_unary(
            "/interactive_main_service.ChatService/GetListRoomChat",
            request_serializer=interactive__main__service__pb2.GetListRoomChatRequest.SerializeToString,
            response_deserializer=interactive__main__service__pb2.GetListRoomChatReply.FromString,
        )
        self.GetMessagesInRoomChat = channel.unary_unary(
            "/interactive_main_service.ChatService/GetMessagesInRoomChat",
            request_serializer=interactive__main__service__pb2.GetListMessagesInRoomChatRequest.SerializeToString,
            response_deserializer=interactive__main__service__pb2.GetListMessagesInRoomChatReply.FromString,
        )


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRoomChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetListRoomChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetMessagesInRoomChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateRoomChat": grpc.unary_unary_rpc_method_handler(
            servicer.CreateRoomChat,
            request_deserializer=interactive__main__service__pb2.CreateRoomChatRequest.FromString,
            response_serializer=interactive__main__service__pb2.CreateRoomChatReply.SerializeToString,
        ),
        "GetListRoomChat": grpc.unary_unary_rpc_method_handler(
            servicer.GetListRoomChat,
            request_deserializer=interactive__main__service__pb2.GetListRoomChatRequest.FromString,
            response_serializer=interactive__main__service__pb2.GetListRoomChatReply.SerializeToString,
        ),
        "GetMessagesInRoomChat": grpc.unary_unary_rpc_method_handler(
            servicer.GetMessagesInRoomChat,
            request_deserializer=interactive__main__service__pb2.GetListMessagesInRoomChatRequest.FromString,
            response_serializer=interactive__main__service__pb2.GetListMessagesInRoomChatReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "interactive_main_service.ChatService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRoomChat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/interactive_main_service.ChatService/CreateRoomChat",
            interactive__main__service__pb2.CreateRoomChatRequest.SerializeToString,
            interactive__main__service__pb2.CreateRoomChatReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetListRoomChat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/interactive_main_service.ChatService/GetListRoomChat",
            interactive__main__service__pb2.GetListRoomChatRequest.SerializeToString,
            interactive__main__service__pb2.GetListRoomChatReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetMessagesInRoomChat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/interactive_main_service.ChatService/GetMessagesInRoomChat",
            interactive__main__service__pb2.GetListMessagesInRoomChatRequest.SerializeToString,
            interactive__main__service__pb2.GetListMessagesInRoomChatReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )