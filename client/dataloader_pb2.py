# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataloader.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x61taloader.proto\x12\ndataloader\"\x0e\n\x0c\x45mptyRequest\"!\n\x0eStatusResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x03\")\n\nIdResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\x03\"O\n\x05Media\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x66ile_uri\x18\x02 \x01(\t\x12\x11\n\tfile_type\x18\x03 \x01(\x05\x12\x15\n\rthumbnail_uri\x18\x04 \x01(\t\"B\n\rMediaResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12 \n\x05media\x18\x02 \x01(\x0b\x32\x11.dataloader.Media\"\'\n\x18GetMediaIdFromURIRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\"3\n\x0f\x41\x64\x64MediaRequest\x12 \n\x05media\x18\x01 \x01(\x0b\x32\x11.dataloader.Media\"8\n\x16\x41\x64\x64MediaStreamResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"5\n\x06TagSet\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\ttagTypeId\x18\x03 \x01(\x03\"&\n\x16GetTagSetRequestByName\x12\x0c\n\x04name\x18\x01 \x01(\t\"E\n\x0eTagSetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\"\n\x06tagset\x18\x02 \x01(\x0b\x32\x12.dataloader.TagSet\"6\n\x13\x43reateTagSetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttagTypeId\x18\x02 \x01(\x03\"$\n\x13\x41lphanumericalValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1f\n\x0eNumericalValue\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1a\n\tDateValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1a\n\tTimeValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1f\n\x0eTimeStampValue\x12\r\n\x05value\x18\x01 \x01(\t\"\xaa\x02\n\x03Tag\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08tagSetId\x18\x02 \x01(\x03\x12\x11\n\ttagTypeId\x18\x03 \x01(\x03\x12\x39\n\x0e\x61lphanumerical\x18\x04 \x01(\x0b\x32\x1f.dataloader.AlphanumericalValueH\x00\x12/\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.dataloader.TimeStampValueH\x00\x12%\n\x04time\x18\x06 \x01(\x0b\x32\x15.dataloader.TimeValueH\x00\x12%\n\x04\x64\x61te\x18\x07 \x01(\x0b\x32\x15.dataloader.DateValueH\x00\x12/\n\tnumerical\x18\x08 \x01(\x0b\x32\x1a.dataloader.NumericalValueH\x00\x42\x07\n\x05value\"<\n\x0bTagResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x03tag\x18\x02 \x01(\x0b\x32\x0f.dataloader.Tag\"\xab\x02\n\x10\x43reateTagRequest\x12\x10\n\x08tagSetId\x18\x02 \x01(\x03\x12\x11\n\ttagTypeId\x18\x03 \x01(\x03\x12\x39\n\x0e\x61lphanumerical\x18\x04 \x01(\x0b\x32\x1f.dataloader.AlphanumericalValueH\x00\x12/\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.dataloader.TimeStampValueH\x00\x12%\n\x04time\x18\x06 \x01(\x0b\x32\x15.dataloader.TimeValueH\x00\x12%\n\x04\x64\x61te\x18\x07 \x01(\x0b\x32\x15.dataloader.DateValueH\x00\x12/\n\tnumerical\x18\x08 \x01(\x0b\x32\x1a.dataloader.NumericalValueH\x00\x42\x07\n\x05value\")\n\x07Tagging\x12\x0f\n\x07mediaId\x18\x01 \x01(\x03\x12\r\n\x05tagId\x18\x02 \x01(\x03\"H\n\x0fTaggingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12$\n\x07tagging\x18\x02 \x01(\x0b\x32\x13.dataloader.Tagging\"6\n\x14\x43reateTaggingRequest\x12\x0f\n\x07mediaId\x18\x01 \x01(\x03\x12\r\n\x05tagId\x18\x02 \x01(\x03\"K\n\tHierarchy\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08tagsetId\x18\x03 \x01(\x03\x12\x12\n\nrootNodeId\x18\x04 \x01(\x03\"$\n\x13GetHierarchyRequest\x12\r\n\x05tagId\x18\x01 \x01(\x03\"N\n\x11HierarchyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12(\n\thierarchy\x18\x02 \x01(\x0b\x32\x15.dataloader.Hierarchy\"L\n\x16\x43reateHierarchyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08tagsetId\x18\x02 \x01(\x03\x12\x12\n\nrootNodeId\x18\x03 \x01(\x03\"M\n\x11\x43reateNodeRequest\x12\r\n\x05tagId\x18\x01 \x01(\x03\x12\x13\n\x0bhierarchyId\x18\x02 \x01(\x03\x12\x14\n\x0cparentNodeId\x18\x03 \x01(\x03\"L\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05tagId\x18\x02 \x01(\x03\x12\x13\n\x0bhierarchyId\x18\x03 \x01(\x03\x12\x14\n\x0cparentNodeId\x18\x04 \x01(\x03\"\x1f\n\x0cNodeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xbb\x0e\n\nDataLoader\x12\x44\n\tgetMedias\x12\x18.dataloader.EmptyRequest\x1a\x19.dataloader.MediaResponse\"\x00\x30\x01\x12\x42\n\x0cgetMediaById\x12\x15.dataloader.IdRequest\x1a\x19.dataloader.MediaResponse\"\x00\x12S\n\x11getMediaIdFromURI\x12$.dataloader.GetMediaIdFromURIRequest\x1a\x16.dataloader.IdResponse\"\x00\x12\x44\n\x08\x61\x64\x64Media\x12\x1b.dataloader.AddMediaRequest\x1a\x19.dataloader.MediaResponse\"\x00\x12R\n\taddMedias\x12\x1b.dataloader.AddMediaRequest\x1a\".dataloader.AddMediaStreamResponse\"\x00(\x01\x30\x01\x12\x42\n\x0b\x64\x65leteMedia\x12\x15.dataloader.IdRequest\x1a\x1a.dataloader.StatusResponse\"\x00\x12\x46\n\ngetTagSets\x12\x18.dataloader.EmptyRequest\x1a\x1a.dataloader.TagSetResponse\"\x00\x30\x01\x12\x44\n\rgetTagSetById\x12\x15.dataloader.IdRequest\x1a\x1a.dataloader.TagSetResponse\"\x00\x12S\n\x0fgetTagSetByName\x12\".dataloader.GetTagSetRequestByName\x1a\x1a.dataloader.TagSetResponse\"\x00\x12M\n\x0c\x63reateTagSet\x12\x1f.dataloader.CreateTagSetRequest\x1a\x1a.dataloader.TagSetResponse\"\x00\x12@\n\x07getTags\x12\x18.dataloader.EmptyRequest\x1a\x17.dataloader.TagResponse\"\x00\x30\x01\x12:\n\x06getTag\x12\x15.dataloader.IdRequest\x1a\x17.dataloader.TagResponse\"\x00\x12I\n\x0e\x63reateOrGetTag\x12\x1c.dataloader.CreateTagRequest\x1a\x17.dataloader.TagResponse\"\x00\x12H\n\x0bgetTaggings\x12\x18.dataloader.EmptyRequest\x1a\x1b.dataloader.TaggingResponse\"\x00\x30\x01\x12P\n\rcreateTagging\x12 .dataloader.CreateTaggingRequest\x1a\x1b.dataloader.TaggingResponse\"\x00\x12\x45\n\x10getMediasWithTag\x12\x15.dataloader.IdRequest\x1a\x16.dataloader.IdResponse\"\x00\x30\x01\x12\x41\n\x0cgetMediaTags\x12\x15.dataloader.IdRequest\x1a\x16.dataloader.IdResponse\"\x00\x30\x01\x12M\n\x0egetHierarchies\x12\x18.dataloader.EmptyRequest\x1a\x1d.dataloader.HierarchyResponse\"\x00\x30\x01\x12\x46\n\x0cgetHierarchy\x12\x15.dataloader.IdRequest\x1a\x1d.dataloader.HierarchyResponse\"\x00\x12V\n\x0f\x63reateHierarchy\x12\".dataloader.CreateHierarchyRequest\x1a\x1d.dataloader.HierarchyResponse\"\x00\x12G\n\ncreateNode\x12\x1d.dataloader.CreateNodeRequest\x1a\x18.dataloader.NodeResponse\"\x00\x12<\n\x07getNode\x12\x15.dataloader.IdRequest\x1a\x18.dataloader.NodeResponse\"\x00\x12J\n\x13getNodesOfHierarchy\x12\x15.dataloader.IdRequest\x1a\x18.dataloader.NodeResponse\"\x00\x30\x01\x12\x44\n\rgetChildNodes\x12\x15.dataloader.IdRequest\x1a\x18.dataloader.NodeResponse\"\x00\x30\x01\x12G\n\rresetDatabase\x12\x18.dataloader.EmptyRequest\x1a\x1a.dataloader.StatusResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataloader_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYREQUEST._serialized_start=32
  _EMPTYREQUEST._serialized_end=46
  _STATUSRESPONSE._serialized_start=48
  _STATUSRESPONSE._serialized_end=81
  _IDREQUEST._serialized_start=83
  _IDREQUEST._serialized_end=106
  _IDRESPONSE._serialized_start=108
  _IDRESPONSE._serialized_end=149
  _MEDIA._serialized_start=151
  _MEDIA._serialized_end=230
  _MEDIARESPONSE._serialized_start=232
  _MEDIARESPONSE._serialized_end=298
  _GETMEDIAIDFROMURIREQUEST._serialized_start=300
  _GETMEDIAIDFROMURIREQUEST._serialized_end=339
  _ADDMEDIAREQUEST._serialized_start=341
  _ADDMEDIAREQUEST._serialized_end=392
  _ADDMEDIASTREAMRESPONSE._serialized_start=394
  _ADDMEDIASTREAMRESPONSE._serialized_end=450
  _TAGSET._serialized_start=452
  _TAGSET._serialized_end=505
  _GETTAGSETREQUESTBYNAME._serialized_start=507
  _GETTAGSETREQUESTBYNAME._serialized_end=545
  _TAGSETRESPONSE._serialized_start=547
  _TAGSETRESPONSE._serialized_end=616
  _CREATETAGSETREQUEST._serialized_start=618
  _CREATETAGSETREQUEST._serialized_end=672
  _ALPHANUMERICALVALUE._serialized_start=674
  _ALPHANUMERICALVALUE._serialized_end=710
  _NUMERICALVALUE._serialized_start=712
  _NUMERICALVALUE._serialized_end=743
  _DATEVALUE._serialized_start=745
  _DATEVALUE._serialized_end=771
  _TIMEVALUE._serialized_start=773
  _TIMEVALUE._serialized_end=799
  _TIMESTAMPVALUE._serialized_start=801
  _TIMESTAMPVALUE._serialized_end=832
  _TAG._serialized_start=835
  _TAG._serialized_end=1133
  _TAGRESPONSE._serialized_start=1135
  _TAGRESPONSE._serialized_end=1195
  _CREATETAGREQUEST._serialized_start=1198
  _CREATETAGREQUEST._serialized_end=1497
  _TAGGING._serialized_start=1499
  _TAGGING._serialized_end=1540
  _TAGGINGRESPONSE._serialized_start=1542
  _TAGGINGRESPONSE._serialized_end=1614
  _CREATETAGGINGREQUEST._serialized_start=1616
  _CREATETAGGINGREQUEST._serialized_end=1670
  _HIERARCHY._serialized_start=1672
  _HIERARCHY._serialized_end=1747
  _GETHIERARCHYREQUEST._serialized_start=1749
  _GETHIERARCHYREQUEST._serialized_end=1785
  _HIERARCHYRESPONSE._serialized_start=1787
  _HIERARCHYRESPONSE._serialized_end=1865
  _CREATEHIERARCHYREQUEST._serialized_start=1867
  _CREATEHIERARCHYREQUEST._serialized_end=1943
  _CREATENODEREQUEST._serialized_start=1945
  _CREATENODEREQUEST._serialized_end=2022
  _NODE._serialized_start=2024
  _NODE._serialized_end=2100
  _NODERESPONSE._serialized_start=2102
  _NODERESPONSE._serialized_end=2133
  _DATALOADER._serialized_start=2136
  _DATALOADER._serialized_end=3987
# @@protoc_insertion_point(module_scope)
