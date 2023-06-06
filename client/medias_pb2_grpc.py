# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import medias_pb2 as medias__pb2


class MediasStub(object):
    """I don't care that media is already a latin plural, Oxford dictionnary has accepted the new "medias" plural form 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMedias = channel.unary_stream(
                '/media.Medias/GetMedias',
                request_serializer=medias__pb2.GetMediasRequest.SerializeToString,
                response_deserializer=medias__pb2.MediaResponse.FromString,
                )
        self.GetMediaById = channel.unary_unary(
                '/media.Medias/GetMediaById',
                request_serializer=medias__pb2.GetMediaByIdRequest.SerializeToString,
                response_deserializer=medias__pb2.MediaResponse.FromString,
                )
        self.AddMedia = channel.stream_unary(
                '/media.Medias/AddMedia',
                request_serializer=medias__pb2.AddMediaRequest.SerializeToString,
                response_deserializer=medias__pb2.AddMediaResponse.FromString,
                )
        self.DeleteMedia = channel.unary_unary(
                '/media.Medias/DeleteMedia',
                request_serializer=medias__pb2.DeleteMediaRequest.SerializeToString,
                response_deserializer=medias__pb2.DeleteMediaResponse.FromString,
                )


class MediasServicer(object):
    """I don't care that media is already a latin plural, Oxford dictionnary has accepted the new "medias" plural form 
    """

    def GetMedias(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMediaById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMedia(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMedia(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MediasServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMedias': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMedias,
                    request_deserializer=medias__pb2.GetMediasRequest.FromString,
                    response_serializer=medias__pb2.MediaResponse.SerializeToString,
            ),
            'GetMediaById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMediaById,
                    request_deserializer=medias__pb2.GetMediaByIdRequest.FromString,
                    response_serializer=medias__pb2.MediaResponse.SerializeToString,
            ),
            'AddMedia': grpc.stream_unary_rpc_method_handler(
                    servicer.AddMedia,
                    request_deserializer=medias__pb2.AddMediaRequest.FromString,
                    response_serializer=medias__pb2.AddMediaResponse.SerializeToString,
            ),
            'DeleteMedia': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMedia,
                    request_deserializer=medias__pb2.DeleteMediaRequest.FromString,
                    response_serializer=medias__pb2.DeleteMediaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'media.Medias', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Medias(object):
    """I don't care that media is already a latin plural, Oxford dictionnary has accepted the new "medias" plural form 
    """

    @staticmethod
    def GetMedias(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/media.Medias/GetMedias',
            medias__pb2.GetMediasRequest.SerializeToString,
            medias__pb2.MediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMediaById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/media.Medias/GetMediaById',
            medias__pb2.GetMediaByIdRequest.SerializeToString,
            medias__pb2.MediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMedia(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/media.Medias/AddMedia',
            medias__pb2.AddMediaRequest.SerializeToString,
            medias__pb2.AddMediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMedia(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/media.Medias/DeleteMedia',
            medias__pb2.DeleteMediaRequest.SerializeToString,
            medias__pb2.DeleteMediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)