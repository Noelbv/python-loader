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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x61taloader.proto\x12\ndataloader\"\x0e\n\x0c\x45mptyRequest\"\'\n\x0eStatusResponse\x12\x15\n\rerror_message\x18\x01 \x01(\t\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"/\n\nIdResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x15\n\rerror_message\x18\x02 \x01(\t\"8\n\x12RepeatedIdResponse\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12\x15\n\rerror_message\x18\x02 \x01(\t\"O\n\x05Media\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x66ile_uri\x18\x02 \x01(\t\x12\x11\n\tfile_type\x18\x03 \x01(\x03\x12\x15\n\rthumbnail_uri\x18\x04 \x01(\t\"%\n\x10GetMediasRequest\x12\x11\n\tfile_type\x18\x01 \x01(\x03\"(\n\x14GetMediaByURIRequest\x12\x10\n\x08\x66ile_uri\x18\x01 \x01(\t\"6\n\x12\x43reateMediaRequest\x12 \n\x05media\x18\x01 \x01(\x0b\x32\x11.dataloader.Media\"H\n\rMediaResponse\x12 \n\x05media\x18\x01 \x01(\x0b\x32\x11.dataloader.Media\x12\x15\n\rerror_message\x18\x02 \x01(\t\"A\n\x19\x43reateMediaStreamResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x15\n\rerror_message\x18\x02 \x01(\t\"5\n\x06TagSet\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\ttagTypeId\x18\x03 \x01(\x03\"&\n\x11GetTagSetsRequest\x12\x11\n\ttagTypeId\x18\x01 \x01(\x03\"&\n\x16GetTagSetRequestByName\x12\x0c\n\x04name\x18\x01 \x01(\t\"6\n\x13\x43reateTagSetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttagTypeId\x18\x02 \x01(\x03\"K\n\x0eTagSetResponse\x12\"\n\x06tagset\x18\x01 \x01(\x0b\x32\x12.dataloader.TagSet\x12\x15\n\rerror_message\x18\x02 \x01(\t\"\xaa\x02\n\x03Tag\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08tagSetId\x18\x02 \x01(\x03\x12\x11\n\ttagTypeId\x18\x03 \x01(\x03\x12\x39\n\x0e\x61lphanumerical\x18\x04 \x01(\x0b\x32\x1f.dataloader.AlphanumericalValueH\x00\x12/\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.dataloader.TimeStampValueH\x00\x12%\n\x04time\x18\x06 \x01(\x0b\x32\x15.dataloader.TimeValueH\x00\x12%\n\x04\x64\x61te\x18\x07 \x01(\x0b\x32\x15.dataloader.DateValueH\x00\x12/\n\tnumerical\x18\x08 \x01(\x0b\x32\x1a.dataloader.NumericalValueH\x00\x42\x07\n\x05value\"$\n\x13\x41lphanumericalValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1f\n\x0eNumericalValue\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1a\n\tDateValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1a\n\tTimeValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1f\n\x0eTimeStampValue\x12\r\n\x05value\x18\x01 \x01(\t\"5\n\x0eGetTagsRequest\x12\x10\n\x08tagSetId\x18\x01 \x01(\x03\x12\x11\n\ttagTypeId\x18\x02 \x01(\x03\"\xab\x02\n\x10\x43reateTagRequest\x12\x10\n\x08tagSetId\x18\x02 \x01(\x03\x12\x11\n\ttagTypeId\x18\x03 \x01(\x03\x12\x39\n\x0e\x61lphanumerical\x18\x04 \x01(\x0b\x32\x1f.dataloader.AlphanumericalValueH\x00\x12/\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.dataloader.TimeStampValueH\x00\x12%\n\x04time\x18\x06 \x01(\x0b\x32\x15.dataloader.TimeValueH\x00\x12%\n\x04\x64\x61te\x18\x07 \x01(\x0b\x32\x15.dataloader.DateValueH\x00\x12/\n\tnumerical\x18\x08 \x01(\x0b\x32\x1a.dataloader.NumericalValueH\x00\x42\x07\n\x05value\"B\n\x0bTagResponse\x12\x1c\n\x03tag\x18\x01 \x01(\x0b\x32\x0f.dataloader.Tag\x12\x15\n\rerror_message\x18\x02 \x01(\t\"\x87\x01\n\x17\x43reateTagStreamResponse\x12>\n\x06id_map\x18\x01 \x03(\x0b\x32..dataloader.CreateTagStreamResponse.IdMapEntry\x1a,\n\nIdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\")\n\x07Tagging\x12\x0f\n\x07mediaId\x18\x01 \x01(\x03\x12\r\n\x05tagId\x18\x02 \x01(\x03\"6\n\x14\x43reateTaggingRequest\x12\x0f\n\x07mediaId\x18\x01 \x01(\x03\x12\r\n\x05tagId\x18\x02 \x01(\x03\"N\n\x0fTaggingResponse\x12$\n\x07tagging\x18\x01 \x01(\x0b\x32\x13.dataloader.Tagging\x12\x15\n\rerror_message\x18\x02 \x01(\t\"C\n\x1b\x43reateTaggingStreamResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x15\n\rerror_message\x18\x02 \x01(\t\"K\n\tHierarchy\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08tagSetId\x18\x03 \x01(\x03\x12\x12\n\nrootNodeId\x18\x04 \x01(\x03\")\n\x15GetHierarchiesRequest\x12\x10\n\x08tagSetId\x18\x01 \x01(\x03\"8\n\x16\x43reateHierarchyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08tagSetId\x18\x02 \x01(\x03\"T\n\x11HierarchyResponse\x12(\n\thierarchy\x18\x01 \x01(\x0b\x32\x15.dataloader.Hierarchy\x12\x15\n\rerror_message\x18\x02 \x01(\t\"L\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05tagId\x18\x02 \x01(\x03\x12\x13\n\x0bhierarchyId\x18\x03 \x01(\x03\x12\x14\n\x0cparentNodeId\x18\x04 \x01(\x03\"M\n\x11\x43reateNodeRequest\x12\r\n\x05tagId\x18\x01 \x01(\x03\x12\x13\n\x0bhierarchyId\x18\x02 \x01(\x03\x12\x14\n\x0cparentNodeId\x18\x03 \x01(\x03\"K\n\x0fGetNodesRequest\x12\r\n\x05tagId\x18\x01 \x01(\x03\x12\x13\n\x0bhierarchyId\x18\x02 \x01(\x03\x12\x14\n\x0cparentNodeId\x18\x03 \x01(\x03\"E\n\x0cNodeResponse\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.dataloader.Node\x12\x15\n\rerror_message\x18\x02 \x01(\t2\xef\x10\n\nDataLoader\x12H\n\tgetMedias\x12\x1c.dataloader.GetMediasRequest\x1a\x19.dataloader.MediaResponse\"\x00\x30\x01\x12\x42\n\x0cgetMediaById\x12\x15.dataloader.IdRequest\x1a\x19.dataloader.MediaResponse\"\x00\x12N\n\rgetMediaByURI\x12 .dataloader.GetMediaByURIRequest\x1a\x19.dataloader.MediaResponse\"\x00\x12J\n\x0b\x63reateMedia\x12\x1e.dataloader.CreateMediaRequest\x1a\x19.dataloader.MediaResponse\"\x00\x12[\n\x0c\x63reateMedias\x12\x1e.dataloader.CreateMediaRequest\x1a%.dataloader.CreateMediaStreamResponse\"\x00(\x01\x30\x01\x12\x42\n\x0b\x64\x65leteMedia\x12\x15.dataloader.IdRequest\x1a\x1a.dataloader.StatusResponse\"\x00\x12K\n\ngetTagSets\x12\x1d.dataloader.GetTagSetsRequest\x1a\x1a.dataloader.TagSetResponse\"\x00\x30\x01\x12\x44\n\rgetTagSetById\x12\x15.dataloader.IdRequest\x1a\x1a.dataloader.TagSetResponse\"\x00\x12S\n\x0fgetTagSetByName\x12\".dataloader.GetTagSetRequestByName\x1a\x1a.dataloader.TagSetResponse\"\x00\x12M\n\x0c\x63reateTagSet\x12\x1f.dataloader.CreateTagSetRequest\x1a\x1a.dataloader.TagSetResponse\"\x00\x12\x42\n\x07getTags\x12\x1a.dataloader.GetTagsRequest\x1a\x17.dataloader.TagResponse\"\x00\x30\x01\x12:\n\x06getTag\x12\x15.dataloader.IdRequest\x1a\x17.dataloader.TagResponse\"\x00\x12\x44\n\tcreateTag\x12\x1c.dataloader.CreateTagRequest\x1a\x17.dataloader.TagResponse\"\x00\x12Z\n\x0f\x63reateTagStream\x12\x1c.dataloader.CreateTagRequest\x1a#.dataloader.CreateTagStreamResponse\"\x00(\x01\x30\x01\x12H\n\x0bgetTaggings\x12\x18.dataloader.EmptyRequest\x1a\x1b.dataloader.TaggingResponse\"\x00\x30\x01\x12K\n\x10getMediasWithTag\x12\x15.dataloader.IdRequest\x1a\x1e.dataloader.RepeatedIdResponse\"\x00\x12G\n\x0cgetMediaTags\x12\x15.dataloader.IdRequest\x1a\x1e.dataloader.RepeatedIdResponse\"\x00\x12P\n\rcreateTagging\x12 .dataloader.CreateTaggingRequest\x1a\x1b.dataloader.TaggingResponse\"\x00\x12\x66\n\x13\x63reateTaggingStream\x12 .dataloader.CreateTaggingRequest\x1a\'.dataloader.CreateTaggingStreamResponse\"\x00(\x01\x30\x01\x12V\n\x0egetHierarchies\x12!.dataloader.GetHierarchiesRequest\x1a\x1d.dataloader.HierarchyResponse\"\x00\x30\x01\x12\x46\n\x0cgetHierarchy\x12\x15.dataloader.IdRequest\x1a\x1d.dataloader.HierarchyResponse\"\x00\x12V\n\x0f\x63reateHierarchy\x12\".dataloader.CreateHierarchyRequest\x1a\x1d.dataloader.HierarchyResponse\"\x00\x12<\n\x07getNode\x12\x15.dataloader.IdRequest\x1a\x18.dataloader.NodeResponse\"\x00\x12\x45\n\x08getNodes\x12\x1b.dataloader.GetNodesRequest\x1a\x18.dataloader.NodeResponse\"\x00\x30\x01\x12G\n\ncreateNode\x12\x1d.dataloader.CreateNodeRequest\x1a\x18.dataloader.NodeResponse\"\x00\x12Q\n\x10\x63reateNodeStream\x12\x1d.dataloader.CreateNodeRequest\x1a\x18.dataloader.NodeResponse\"\x00(\x01\x30\x01\x12\x41\n\ndeleteNode\x12\x15.dataloader.IdRequest\x1a\x1a.dataloader.StatusResponse\"\x00\x12G\n\rresetDatabase\x12\x18.dataloader.EmptyRequest\x1a\x1a.dataloader.StatusResponse\"\x00\x42\x1aZ\x18m3.dataloader/dataloaderb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataloader_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\030m3.dataloader/dataloader'
  _CREATETAGSTREAMRESPONSE_IDMAPENTRY._options = None
  _CREATETAGSTREAMRESPONSE_IDMAPENTRY._serialized_options = b'8\001'
  _EMPTYREQUEST._serialized_start=32
  _EMPTYREQUEST._serialized_end=46
  _STATUSRESPONSE._serialized_start=48
  _STATUSRESPONSE._serialized_end=87
  _IDREQUEST._serialized_start=89
  _IDREQUEST._serialized_end=112
  _IDRESPONSE._serialized_start=114
  _IDRESPONSE._serialized_end=161
  _REPEATEDIDRESPONSE._serialized_start=163
  _REPEATEDIDRESPONSE._serialized_end=219
  _MEDIA._serialized_start=221
  _MEDIA._serialized_end=300
  _GETMEDIASREQUEST._serialized_start=302
  _GETMEDIASREQUEST._serialized_end=339
  _GETMEDIABYURIREQUEST._serialized_start=341
  _GETMEDIABYURIREQUEST._serialized_end=381
  _CREATEMEDIAREQUEST._serialized_start=383
  _CREATEMEDIAREQUEST._serialized_end=437
  _MEDIARESPONSE._serialized_start=439
  _MEDIARESPONSE._serialized_end=511
  _CREATEMEDIASTREAMRESPONSE._serialized_start=513
  _CREATEMEDIASTREAMRESPONSE._serialized_end=578
  _TAGSET._serialized_start=580
  _TAGSET._serialized_end=633
  _GETTAGSETSREQUEST._serialized_start=635
  _GETTAGSETSREQUEST._serialized_end=673
  _GETTAGSETREQUESTBYNAME._serialized_start=675
  _GETTAGSETREQUESTBYNAME._serialized_end=713
  _CREATETAGSETREQUEST._serialized_start=715
  _CREATETAGSETREQUEST._serialized_end=769
  _TAGSETRESPONSE._serialized_start=771
  _TAGSETRESPONSE._serialized_end=846
  _TAG._serialized_start=849
  _TAG._serialized_end=1147
  _ALPHANUMERICALVALUE._serialized_start=1149
  _ALPHANUMERICALVALUE._serialized_end=1185
  _NUMERICALVALUE._serialized_start=1187
  _NUMERICALVALUE._serialized_end=1218
  _DATEVALUE._serialized_start=1220
  _DATEVALUE._serialized_end=1246
  _TIMEVALUE._serialized_start=1248
  _TIMEVALUE._serialized_end=1274
  _TIMESTAMPVALUE._serialized_start=1276
  _TIMESTAMPVALUE._serialized_end=1307
  _GETTAGSREQUEST._serialized_start=1309
  _GETTAGSREQUEST._serialized_end=1362
  _CREATETAGREQUEST._serialized_start=1365
  _CREATETAGREQUEST._serialized_end=1664
  _TAGRESPONSE._serialized_start=1666
  _TAGRESPONSE._serialized_end=1732
  _CREATETAGSTREAMRESPONSE._serialized_start=1735
  _CREATETAGSTREAMRESPONSE._serialized_end=1870
  _CREATETAGSTREAMRESPONSE_IDMAPENTRY._serialized_start=1826
  _CREATETAGSTREAMRESPONSE_IDMAPENTRY._serialized_end=1870
  _TAGGING._serialized_start=1872
  _TAGGING._serialized_end=1913
  _CREATETAGGINGREQUEST._serialized_start=1915
  _CREATETAGGINGREQUEST._serialized_end=1969
  _TAGGINGRESPONSE._serialized_start=1971
  _TAGGINGRESPONSE._serialized_end=2049
  _CREATETAGGINGSTREAMRESPONSE._serialized_start=2051
  _CREATETAGGINGSTREAMRESPONSE._serialized_end=2118
  _HIERARCHY._serialized_start=2120
  _HIERARCHY._serialized_end=2195
  _GETHIERARCHIESREQUEST._serialized_start=2197
  _GETHIERARCHIESREQUEST._serialized_end=2238
  _CREATEHIERARCHYREQUEST._serialized_start=2240
  _CREATEHIERARCHYREQUEST._serialized_end=2296
  _HIERARCHYRESPONSE._serialized_start=2298
  _HIERARCHYRESPONSE._serialized_end=2382
  _NODE._serialized_start=2384
  _NODE._serialized_end=2460
  _CREATENODEREQUEST._serialized_start=2462
  _CREATENODEREQUEST._serialized_end=2539
  _GETNODESREQUEST._serialized_start=2541
  _GETNODESREQUEST._serialized_end=2616
  _NODERESPONSE._serialized_start=2618
  _NODERESPONSE._serialized_end=2687
  _DATALOADER._serialized_start=2690
  _DATALOADER._serialized_end=4849
# @@protoc_insertion_point(module_scope)
