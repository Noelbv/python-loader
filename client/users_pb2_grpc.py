# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import users_pb2 as users__pb2


class UsersStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUsers = channel.unary_stream(
                '/user.Users/GetUsers',
                request_serializer=users__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=users__pb2.UserResponse.FromString,
                )
        self.GetUserById = channel.unary_unary(
                '/user.Users/GetUserById',
                request_serializer=users__pb2.GetUserByIdRequest.SerializeToString,
                response_deserializer=users__pb2.UserResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/user.Users/UpdateUser',
                request_serializer=users__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=users__pb2.UpdateUserResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/user.Users/DeleteUser',
                request_serializer=users__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=users__pb2.DeleteUserResponse.FromString,
                )


class UsersServicer(object):
    """The greeting service definition.
    """

    def GetUsers(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUsers': grpc.unary_stream_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=users__pb2.GetUsersRequest.FromString,
                    response_serializer=users__pb2.UserResponse.SerializeToString,
            ),
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=users__pb2.GetUserByIdRequest.FromString,
                    response_serializer=users__pb2.UserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=users__pb2.UpdateUserRequest.FromString,
                    response_serializer=users__pb2.UpdateUserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=users__pb2.DeleteUserRequest.FromString,
                    response_serializer=users__pb2.DeleteUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """The greeting service definition.
    """

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user.Users/GetUsers',
            users__pb2.GetUsersRequest.SerializeToString,
            users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.Users/GetUserById',
            users__pb2.GetUserByIdRequest.SerializeToString,
            users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.Users/UpdateUser',
            users__pb2.UpdateUserRequest.SerializeToString,
            users__pb2.UpdateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.Users/DeleteUser',
            users__pb2.DeleteUserRequest.SerializeToString,
            users__pb2.DeleteUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
