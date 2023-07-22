import os
import json

import grpc
import dataloader_pb2 as rpc_objects
from dataloader_pb2_grpc import DataLoaderStub

from google.protobuf.json_format import MessageToJson


class LoaderClient:
    def __init__(self, grpc_host='localhost', grpc_port='50051') -> None:
        self.grpc_channel = grpc.insecure_channel('%s:%s' % (grpc_host, grpc_port))
        self.grpc_stub = DataLoaderStub(self.grpc_channel)

    #!================ Media/media functions ======================================================================

    def get_media(self, id: int):
    # Get a single media with the given ID
        request = rpc_objects.IdRequest(id=id)
        response = self.grpc_stub.getMediaById(request)
        return response.error_message if response.error_message \
        else response.media

    
    def get_id(self, file_uri: str):
    # Get a an media ID using its URI
        request = rpc_objects.GetMediaIdFromURIRequest(uri=file_uri)
        response = self.grpc_stub.getMediaIdFromURI(request)
        return response.error_message if response.error_message \
        else response.id


    def listall_medias(self):
    # List all the medias stored
        request = rpc_objects.EmptyRequest()
        response_iterator = self.grpc_stub.getMedias(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.media
            

    def add_dir(self, directory: str, formats):
    # Add files from a specified directory to the database.
        file_count = 0
        def add_media_requests_generator(directory: str):
            nonlocal file_count
            for file in os.listdir(directory):
                if any(file.endswith('.' + ext) for ext in formats):
                    file_path = os.path.abspath(os.path.join(directory, file))
                    if file.lower().endswith(('jpg', 'png', 'bmp')):
                        file_type = 0		# Image
                    elif file.lower().endswith(('mp3', 'wav', 'flac')):
                        file_type = 1		# Audio
                    elif file.lower().endswith(('mp4', 'avi')):
                        file_type = 2		# Video
                    else: 
                        file_type = 3		# Other
                    file_count += 1
                    request = rpc_objects.CreateMediaRequest(media={
                        "file_uri": file_path,
                        "file_type": file_type,
                        "thumbnail_uri": file_path
                        })
                    yield request
        
       
        response_iterator = self.grpc_stub.createMedias(add_media_requests_generator(directory))
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else 'Info: added %d medias to database.' % (response.count)
        if file_count == 0 : yield 'Info: no files of the specified format were found in the directory.'
        else : yield 'Info: %d files were found in the directory.' % file_count


    def add_file(self, path: str):
    # Add a specific file to the database.
        file_path = os.path.abspath(path)
        if path.lower().endswith(('jpg', 'png', 'bmp')):
            file_type = 0		# Image
        elif path.lower().endswith(('mp3', 'wav', 'flac')):
            file_type = 1		# Audio
        elif path.lower().endswith(('mp4', 'avi')):
            file_type = 2		# Video
        else: 
            file_type = 3		# Other
        request = rpc_objects.CreateMediaRequest(media={
            "file_uri": file_path,
            "file_type": file_type,
            "thumbnail_uri": file_path
            })
        
        response = self.grpc_stub.createMedia(request)
        return response.error_message if response.error_message \
        else response.media


    # Delete a single media with the given ID
    def delete(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response = self.grpc_stub.deleteMedia(request)
        return response.error_message if response.error_message \
        else 'Success, media removed from database.'


    #!================ Tagset functions ======================================================================

    def listall_tagsets(self, tagtype_id: int):
        if tagtype_id > 0: request = rpc_objects.GetTagSetsRequest(tagTypeId=tagtype_id)
        else : request = rpc_objects.GetTagSetsRequest()
        response_iterator = self.grpc_stub.getTagSets(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.tagset

    def add_tagset(self, name: str, tagtype_id: int):
        request = rpc_objects.CreateTagSetRequest(name=name, tagTypeId=tagtype_id)
        response = self.grpc_stub.createTagSet(request)
        return response.error_message if response.error_message \
        else response.tagset
    
    def get_tagset_by_id(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response = self.grpc_stub.getTagSetById(request)
        return response.error_message if response.error_message \
        else response.tagset
    
    def get_tagset_by_name(self, name: str):
        request = rpc_objects.GetTagSetRequestByName(name=name)
        response = self.grpc_stub.getTagSetByName(request)
        return response.error_message if response.error_message \
        else response.tagset
        
    #!================ Tag functions ======================================================================
    
    def listall_tags(self, tagtype_id: int, tagset_id: int):
        if tagtype_id > 0 and tagset_id > 0:
            request = rpc_objects.GetTagsRequest(
                tagTypeId=tagtype_id,
                tagSetId=tagset_id
            )
        elif tagtype_id > 0:
            request = rpc_objects.GetTagsRequest(
                tagTypeId=tagtype_id
            )
        elif tagset_id > 0:
            request = rpc_objects.GetTagsRequest(
                tagSetId=tagset_id
            )
        else:
            request = rpc_objects.GetTagsRequest()
            
        response_iterator = self.grpc_stub.getTags(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.tag

    def add_tag(self, tagset_id: int, tagtype_id: int, value):
        match tagtype_id:
            case 1: 
                request = rpc_objects.CreateTagRequest(
                    tagSetId=tagset_id, 
                    tagTypeId=tagtype_id,
                    alphanumerical = rpc_objects.AlphanumericalValue(value=value)
                )
            case 2: 
                value = value.replace('/', ' ')
                request = rpc_objects.CreateTagRequest(
                    tagSetId=tagset_id, 
                    tagTypeId=tagtype_id,
                    timestamp = rpc_objects.TimeStampValue(value=value)
                )
            case 3: 
                request = rpc_objects.CreateTagRequest(
                    tagSetId=tagset_id, 
                    tagTypeId=tagtype_id,
                    time = rpc_objects.TimeValue(value=value)
                )
            case 4: 
                request = rpc_objects.CreateTagRequest(
                    tagSetId=tagset_id, 
                    tagTypeId=tagtype_id,
                    date = rpc_objects.DateValue(value=value)
                )
            case 5: 
                request = rpc_objects.CreateTagRequest(
                    tagSetId=tagset_id, 
                    tagTypeId=tagtype_id,
                    numerical = rpc_objects.NumericalValue(value=int(value))
                )
            case _:
                return 'Error : Not a valid tag type. Range is [1:5]'
            
        response = self.grpc_stub.createOrGetTag(request)
        return response.error_message if response.error_message \
        else response.tag
    
    def get_tag(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response = self.grpc_stub.getTag(request)
        return response.error_message if response.error_message \
        else response.tag

    #!================ Tagging functions ======================================================================
    def listall_taggings(self):
        request = rpc_objects.EmptyRequest()
        response_iterator = self.grpc_stub.getTaggings(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.tagging

    def add_tagging(self, tag_id: int, media_id: int):
        request = rpc_objects.CreateTaggingRequest(
            tagId=tag_id,
            mediaId=media_id
        )
        response = self.grpc_stub.createTagging(request)
        return response.error_message if response.error_message \
        else response.tagging
    

    def get_medias_with_tag(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response_iterator = self.grpc_stub.getMediasWithTag(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.id

    def get_media_tags(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response_iterator = self.grpc_stub.getMediaTags(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.id

#!================ Hierarchy functions ====================================================================

    def listall_hierarchies(self):
        request = rpc_objects.EmptyRequest()
        response_iterator = self.grpc_stub.getHierarchies(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.hierarchy

    def add_hierarchy(self, name: str, tagset_id: int):
        request = rpc_objects.CreateHierarchyRequest(
            name=name,
            tagsetId=tagset_id
        )
        response = self.grpc_stub.createHierarchy(request)
        return response.error_message if response.error_message \
        else response.hierarchy
    

    def get_hierarchy(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response = self.grpc_stub.getHierarchy(request)
        return response.error_message if response.error_message \
        else response.hierarchy



    #!================ Node functions ======================================================================

    def add_node(self, tag_id: int, hierarchy_id: int, parentnode_id: int):
        request = rpc_objects.CreateNodeRequest(
            tagId=tag_id,
            hierarchyId=hierarchy_id,
            parentNodeId=parentnode_id
        )
        response = self.grpc_stub.createNode(request)
        return response.error_message if response.error_message \
        else response.node

        

    def add_rootnode(self, tag_id: int, hierarchy_id: int):
        request = rpc_objects.CreateNodeRequest(
            tagId=tag_id,
            hierarchyId=hierarchy_id
        )
        response = self.grpc_stub.createNode(request)
        return response.error_message if response.error_message \
        else response.node
        
        
    def get_node(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response = self.grpc_stub.getNode(request)
        return response.error_message if response.error_message \
        else response.node
    
    def get_nodes_of_hierarchy(self, hierarchy_id: int):
        request = rpc_objects.IdRequest(id=hierarchy_id)
        response_iterator = self.grpc_stub.getNodesOfHierarchy(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.node
    
    def get_child_nodes(self, id: int):
        request = rpc_objects.IdRequest(id=id)
        response_iterator = self.grpc_stub.getChildNodes(request)
        for response in response_iterator:
            yield response.error_message if response.error_message \
            else response.node

    
    #!================ DB management ======================================================================

    # Reset the database
    def reset(self):
        request = rpc_objects.EmptyRequest()
        response = self.grpc_stub.resetDatabase(request)
        return response.error_message if response.error_message \
        else 'Success, database was successfully reset.'