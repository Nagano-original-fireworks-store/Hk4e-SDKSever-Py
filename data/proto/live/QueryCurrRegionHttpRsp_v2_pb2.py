# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QueryCurrRegionHttpRsp_v2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import data.proto.live.RegionInfo_v2_pb2 as RegionInfo__v2__pb2
import data.proto.live.ForceUpdateInfo_v2_pb2 as ForceUpdateInfo__v2__pb2
import data.proto.live.StopServerInfo_v2_pb2 as StopServerInfo__v2__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fQueryCurrRegionHttpRsp_v2.proto\x12\nproto.live\x1a\x13RegionInfo_v2.proto\x1a\x18\x46orceUpdateInfo_v2.proto\x1a\x17StopServerInfo_v2.proto\"\xd3\x02\n\x19QueryCurrRegionHttpRsp_v2\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12.\n\x0bregion_info\x18\x03 \x01(\x0b\x32\x19.proto.live.RegionInfo_v2\x12\x19\n\x11\x63lient_secret_key\x18\x0b \x01(\x0c\x12&\n\x1eregion_custom_config_encrypted\x18\x0c \x01(\x0c\x12-\n%client_region_custom_config_encrypted\x18\r \x01(\x0c\x12\x36\n\x0c\x66orce_udpate\x18\x04 \x01(\x0b\x32\x1e.proto.live.ForceUpdateInfo_v2H\x00\x12\x34\n\x0bstop_server\x18\x05 \x01(\x0b\x32\x1d.proto.live.StopServerInfo_v2H\x00\x42\x08\n\x06\x64\x65tailb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'QueryCurrRegionHttpRsp_v2_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_QUERYCURRREGIONHTTPRSP_V2']._serialized_start=120
  _globals['_QUERYCURRREGIONHTTPRSP_V2']._serialized_end=459
# @@protoc_insertion_point(module_scope)
