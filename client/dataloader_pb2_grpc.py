# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dataloader_pb2 as dataloader__pb2


class DataLoaderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getMedias = channel.unary_stream(
                '/dataloader.DataLoader/getMedias',
                request_serializer=dataloader__pb2.GetMediasRequest.SerializeToString,
                response_deserializer=dataloader__pb2.MediaResponse.FromString,
                )
        self.getMediaById = channel.unary_unary(
                '/dataloader.DataLoader/getMediaById',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.MediaResponse.FromString,
                )
        self.getMediaByURI = channel.unary_unary(
                '/dataloader.DataLoader/getMediaByURI',
                request_serializer=dataloader__pb2.GetMediaByURIRequest.SerializeToString,
                response_deserializer=dataloader__pb2.MediaResponse.FromString,
                )
        self.createMedia = channel.unary_unary(
                '/dataloader.DataLoader/createMedia',
                request_serializer=dataloader__pb2.CreateMediaRequest.SerializeToString,
                response_deserializer=dataloader__pb2.MediaResponse.FromString,
                )
        self.createMedias = channel.stream_stream(
                '/dataloader.DataLoader/createMedias',
                request_serializer=dataloader__pb2.CreateMediaRequest.SerializeToString,
                response_deserializer=dataloader__pb2.CreateMediaStreamResponse.FromString,
                )
        self.deleteMedia = channel.unary_unary(
                '/dataloader.DataLoader/deleteMedia',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.StatusResponse.FromString,
                )
        self.getTagSets = channel.unary_stream(
                '/dataloader.DataLoader/getTagSets',
                request_serializer=dataloader__pb2.GetTagSetsRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TagSetResponse.FromString,
                )
        self.getTagSetById = channel.unary_unary(
                '/dataloader.DataLoader/getTagSetById',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TagSetResponse.FromString,
                )
        self.getTagSetByName = channel.unary_unary(
                '/dataloader.DataLoader/getTagSetByName',
                request_serializer=dataloader__pb2.GetTagSetRequestByName.SerializeToString,
                response_deserializer=dataloader__pb2.TagSetResponse.FromString,
                )
        self.createTagSet = channel.unary_unary(
                '/dataloader.DataLoader/createTagSet',
                request_serializer=dataloader__pb2.CreateTagSetRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TagSetResponse.FromString,
                )
        self.getTags = channel.unary_stream(
                '/dataloader.DataLoader/getTags',
                request_serializer=dataloader__pb2.GetTagsRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TagResponse.FromString,
                )
        self.getTag = channel.unary_unary(
                '/dataloader.DataLoader/getTag',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TagResponse.FromString,
                )
        self.createTag = channel.unary_unary(
                '/dataloader.DataLoader/createTag',
                request_serializer=dataloader__pb2.CreateTagRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TagResponse.FromString,
                )
        self.getTaggings = channel.unary_stream(
                '/dataloader.DataLoader/getTaggings',
                request_serializer=dataloader__pb2.EmptyRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TaggingResponse.FromString,
                )
        self.getMediasWithTag = channel.unary_unary(
                '/dataloader.DataLoader/getMediasWithTag',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.RepeatedIdResponse.FromString,
                )
        self.getMediaTags = channel.unary_unary(
                '/dataloader.DataLoader/getMediaTags',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.RepeatedIdResponse.FromString,
                )
        self.createTagging = channel.unary_unary(
                '/dataloader.DataLoader/createTagging',
                request_serializer=dataloader__pb2.CreateTaggingRequest.SerializeToString,
                response_deserializer=dataloader__pb2.TaggingResponse.FromString,
                )
        self.getHierarchies = channel.unary_stream(
                '/dataloader.DataLoader/getHierarchies',
                request_serializer=dataloader__pb2.GetHierarchiesRequest.SerializeToString,
                response_deserializer=dataloader__pb2.HierarchyResponse.FromString,
                )
        self.getHierarchy = channel.unary_unary(
                '/dataloader.DataLoader/getHierarchy',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.HierarchyResponse.FromString,
                )
        self.createHierarchy = channel.unary_unary(
                '/dataloader.DataLoader/createHierarchy',
                request_serializer=dataloader__pb2.CreateHierarchyRequest.SerializeToString,
                response_deserializer=dataloader__pb2.HierarchyResponse.FromString,
                )
        self.getNode = channel.unary_unary(
                '/dataloader.DataLoader/getNode',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.NodeResponse.FromString,
                )
        self.getNodes = channel.unary_stream(
                '/dataloader.DataLoader/getNodes',
                request_serializer=dataloader__pb2.GetNodesRequest.SerializeToString,
                response_deserializer=dataloader__pb2.NodeResponse.FromString,
                )
        self.createNode = channel.unary_unary(
                '/dataloader.DataLoader/createNode',
                request_serializer=dataloader__pb2.CreateNodeRequest.SerializeToString,
                response_deserializer=dataloader__pb2.NodeResponse.FromString,
                )
        self.deleteNode = channel.unary_unary(
                '/dataloader.DataLoader/deleteNode',
                request_serializer=dataloader__pb2.IdRequest.SerializeToString,
                response_deserializer=dataloader__pb2.StatusResponse.FromString,
                )
        self.resetDatabase = channel.unary_unary(
                '/dataloader.DataLoader/resetDatabase',
                request_serializer=dataloader__pb2.EmptyRequest.SerializeToString,
                response_deserializer=dataloader__pb2.StatusResponse.FromString,
                )


class DataLoaderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getMedias(self, request, context):
        """Medias
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMediaById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMediaByURI(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createMedia(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createMedias(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteMedia(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTagSets(self, request, context):
        """TagSets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTagSetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTagSetByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createTagSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTags(self, request, context):
        """Tags
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTaggings(self, request, context):
        """Tagging
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMediasWithTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMediaTags(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createTagging(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getHierarchies(self, request, context):
        """Hierarchies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getHierarchy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createHierarchy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getNode(self, request, context):
        """Nodes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resetDatabase(self, request, context):
        """Other
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataLoaderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getMedias': grpc.unary_stream_rpc_method_handler(
                    servicer.getMedias,
                    request_deserializer=dataloader__pb2.GetMediasRequest.FromString,
                    response_serializer=dataloader__pb2.MediaResponse.SerializeToString,
            ),
            'getMediaById': grpc.unary_unary_rpc_method_handler(
                    servicer.getMediaById,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.MediaResponse.SerializeToString,
            ),
            'getMediaByURI': grpc.unary_unary_rpc_method_handler(
                    servicer.getMediaByURI,
                    request_deserializer=dataloader__pb2.GetMediaByURIRequest.FromString,
                    response_serializer=dataloader__pb2.MediaResponse.SerializeToString,
            ),
            'createMedia': grpc.unary_unary_rpc_method_handler(
                    servicer.createMedia,
                    request_deserializer=dataloader__pb2.CreateMediaRequest.FromString,
                    response_serializer=dataloader__pb2.MediaResponse.SerializeToString,
            ),
            'createMedias': grpc.stream_stream_rpc_method_handler(
                    servicer.createMedias,
                    request_deserializer=dataloader__pb2.CreateMediaRequest.FromString,
                    response_serializer=dataloader__pb2.CreateMediaStreamResponse.SerializeToString,
            ),
            'deleteMedia': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteMedia,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.StatusResponse.SerializeToString,
            ),
            'getTagSets': grpc.unary_stream_rpc_method_handler(
                    servicer.getTagSets,
                    request_deserializer=dataloader__pb2.GetTagSetsRequest.FromString,
                    response_serializer=dataloader__pb2.TagSetResponse.SerializeToString,
            ),
            'getTagSetById': grpc.unary_unary_rpc_method_handler(
                    servicer.getTagSetById,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.TagSetResponse.SerializeToString,
            ),
            'getTagSetByName': grpc.unary_unary_rpc_method_handler(
                    servicer.getTagSetByName,
                    request_deserializer=dataloader__pb2.GetTagSetRequestByName.FromString,
                    response_serializer=dataloader__pb2.TagSetResponse.SerializeToString,
            ),
            'createTagSet': grpc.unary_unary_rpc_method_handler(
                    servicer.createTagSet,
                    request_deserializer=dataloader__pb2.CreateTagSetRequest.FromString,
                    response_serializer=dataloader__pb2.TagSetResponse.SerializeToString,
            ),
            'getTags': grpc.unary_stream_rpc_method_handler(
                    servicer.getTags,
                    request_deserializer=dataloader__pb2.GetTagsRequest.FromString,
                    response_serializer=dataloader__pb2.TagResponse.SerializeToString,
            ),
            'getTag': grpc.unary_unary_rpc_method_handler(
                    servicer.getTag,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.TagResponse.SerializeToString,
            ),
            'createTag': grpc.unary_unary_rpc_method_handler(
                    servicer.createTag,
                    request_deserializer=dataloader__pb2.CreateTagRequest.FromString,
                    response_serializer=dataloader__pb2.TagResponse.SerializeToString,
            ),
            'getTaggings': grpc.unary_stream_rpc_method_handler(
                    servicer.getTaggings,
                    request_deserializer=dataloader__pb2.EmptyRequest.FromString,
                    response_serializer=dataloader__pb2.TaggingResponse.SerializeToString,
            ),
            'getMediasWithTag': grpc.unary_unary_rpc_method_handler(
                    servicer.getMediasWithTag,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.RepeatedIdResponse.SerializeToString,
            ),
            'getMediaTags': grpc.unary_unary_rpc_method_handler(
                    servicer.getMediaTags,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.RepeatedIdResponse.SerializeToString,
            ),
            'createTagging': grpc.unary_unary_rpc_method_handler(
                    servicer.createTagging,
                    request_deserializer=dataloader__pb2.CreateTaggingRequest.FromString,
                    response_serializer=dataloader__pb2.TaggingResponse.SerializeToString,
            ),
            'getHierarchies': grpc.unary_stream_rpc_method_handler(
                    servicer.getHierarchies,
                    request_deserializer=dataloader__pb2.GetHierarchiesRequest.FromString,
                    response_serializer=dataloader__pb2.HierarchyResponse.SerializeToString,
            ),
            'getHierarchy': grpc.unary_unary_rpc_method_handler(
                    servicer.getHierarchy,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.HierarchyResponse.SerializeToString,
            ),
            'createHierarchy': grpc.unary_unary_rpc_method_handler(
                    servicer.createHierarchy,
                    request_deserializer=dataloader__pb2.CreateHierarchyRequest.FromString,
                    response_serializer=dataloader__pb2.HierarchyResponse.SerializeToString,
            ),
            'getNode': grpc.unary_unary_rpc_method_handler(
                    servicer.getNode,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.NodeResponse.SerializeToString,
            ),
            'getNodes': grpc.unary_stream_rpc_method_handler(
                    servicer.getNodes,
                    request_deserializer=dataloader__pb2.GetNodesRequest.FromString,
                    response_serializer=dataloader__pb2.NodeResponse.SerializeToString,
            ),
            'createNode': grpc.unary_unary_rpc_method_handler(
                    servicer.createNode,
                    request_deserializer=dataloader__pb2.CreateNodeRequest.FromString,
                    response_serializer=dataloader__pb2.NodeResponse.SerializeToString,
            ),
            'deleteNode': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteNode,
                    request_deserializer=dataloader__pb2.IdRequest.FromString,
                    response_serializer=dataloader__pb2.StatusResponse.SerializeToString,
            ),
            'resetDatabase': grpc.unary_unary_rpc_method_handler(
                    servicer.resetDatabase,
                    request_deserializer=dataloader__pb2.EmptyRequest.FromString,
                    response_serializer=dataloader__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dataloader.DataLoader', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataLoader(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getMedias(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataloader.DataLoader/getMedias',
            dataloader__pb2.GetMediasRequest.SerializeToString,
            dataloader__pb2.MediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMediaById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getMediaById',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.MediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMediaByURI(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getMediaByURI',
            dataloader__pb2.GetMediaByURIRequest.SerializeToString,
            dataloader__pb2.MediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createMedia(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/createMedia',
            dataloader__pb2.CreateMediaRequest.SerializeToString,
            dataloader__pb2.MediaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createMedias(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/dataloader.DataLoader/createMedias',
            dataloader__pb2.CreateMediaRequest.SerializeToString,
            dataloader__pb2.CreateMediaStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteMedia(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/deleteMedia',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTagSets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataloader.DataLoader/getTagSets',
            dataloader__pb2.GetTagSetsRequest.SerializeToString,
            dataloader__pb2.TagSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTagSetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getTagSetById',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.TagSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTagSetByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getTagSetByName',
            dataloader__pb2.GetTagSetRequestByName.SerializeToString,
            dataloader__pb2.TagSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createTagSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/createTagSet',
            dataloader__pb2.CreateTagSetRequest.SerializeToString,
            dataloader__pb2.TagSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTags(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataloader.DataLoader/getTags',
            dataloader__pb2.GetTagsRequest.SerializeToString,
            dataloader__pb2.TagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getTag',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.TagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/createTag',
            dataloader__pb2.CreateTagRequest.SerializeToString,
            dataloader__pb2.TagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTaggings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataloader.DataLoader/getTaggings',
            dataloader__pb2.EmptyRequest.SerializeToString,
            dataloader__pb2.TaggingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMediasWithTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getMediasWithTag',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.RepeatedIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMediaTags(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getMediaTags',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.RepeatedIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createTagging(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/createTagging',
            dataloader__pb2.CreateTaggingRequest.SerializeToString,
            dataloader__pb2.TaggingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getHierarchies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataloader.DataLoader/getHierarchies',
            dataloader__pb2.GetHierarchiesRequest.SerializeToString,
            dataloader__pb2.HierarchyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getHierarchy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getHierarchy',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.HierarchyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createHierarchy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/createHierarchy',
            dataloader__pb2.CreateHierarchyRequest.SerializeToString,
            dataloader__pb2.HierarchyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/getNode',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataloader.DataLoader/getNodes',
            dataloader__pb2.GetNodesRequest.SerializeToString,
            dataloader__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/createNode',
            dataloader__pb2.CreateNodeRequest.SerializeToString,
            dataloader__pb2.NodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/deleteNode',
            dataloader__pb2.IdRequest.SerializeToString,
            dataloader__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resetDatabase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataloader.DataLoader/resetDatabase',
            dataloader__pb2.EmptyRequest.SerializeToString,
            dataloader__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
