# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/broadcast/v1/mod.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x62ilibili/broadcast/v1/mod.proto\x12\x15\x62ilibili.broadcast.v1\x1a\x1bgoogle/protobuf/empty.proto\"\x88\x01\n\x0fModResourceResp\x12\x0e\n\x06\x61tcion\x18\x01 \x01(\x05\x12\x0f\n\x07\x61pp_key\x18\x02 \x01(\t\x12\x11\n\tpool_name\x18\x03 \x01(\t\x12\x13\n\x0bmodule_name\x18\x04 \x01(\t\x12\x16\n\x0emodule_version\x18\x05 \x01(\x03\x12\x14\n\x0clist_version\x18\x06 \x01(\x03\x32_\n\nModManager\x12Q\n\rWatchResource\x12\x16.google.protobuf.Empty\x1a&.bilibili.broadcast.v1.ModResourceResp0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.broadcast.v1.mod_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MODRESOURCERESP']._serialized_start=88
  _globals['_MODRESOURCERESP']._serialized_end=224
  _globals['_MODMANAGER']._serialized_start=226
  _globals['_MODMANAGER']._serialized_end=321
# @@protoc_insertion_point(module_scope)
