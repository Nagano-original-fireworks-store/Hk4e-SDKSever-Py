# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QueryCurrRegionHttpRsp_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import data.proto.cbt.ForceUpdateInfo_v1_pb2 as ForceUpdateInfo__v1__pb2
import data.proto.cbt.StopServerInfo_v1_pb2 as StopServerInfo__v1__pb2
import data.proto.cbt.RegionInfo_v1_pb2 as RegionInfo__v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fQueryCurrRegionHttpRsp_v1.proto\x12\tproto.cbt\x1a\x18\x46orceUpdateInfo_v1.proto\x1a\x17StopServerInfo_v1.proto\x1a\x13RegionInfo_v1.proto\"\xe0\x01\n\x19QueryCurrRegionHttpRsp_v1\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x35\n\x0c\x66orce_udpate\x18\x03 \x01(\x0b\x32\x1d.proto.cbt.ForceUpdateInfo_v1H\x00\x12\x33\n\x0bstop_server\x18\x04 \x01(\x0b\x32\x1c.proto.cbt.StopServerInfo_v1H\x00\x12/\n\x0bregion_info\x18\x05 \x01(\x0b\x32\x18.proto.cbt.RegionInfo_v1H\x00\x42\x08\n\x06\x64\x65tailb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'QueryCurrRegionHttpRsp_v1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_QUERYCURRREGIONHTTPRSP_V1']._serialized_start=119
  _globals['_QUERYCURRREGIONHTTPRSP_V1']._serialized_end=343
# @@protoc_insertion_point(module_scope)
