# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/playerunite/ugcanymodel/ugcanymodel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6bilibili/app/playerunite/ugcanymodel/ugcanymodel.proto\x12$bilibili.app.playerunite.ugcanymodel\"T\n\x0b\x42uttonStyle\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12\x10\n\x08\x62g_color\x18\x03 \x01(\t\x12\x11\n\tjump_link\x18\x04 \x01(\t\"\xb7\x01\n\tPlayLimit\x12\x41\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x33.bilibili.app.playerunite.ugcanymodel.PlayLimitCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0bsub_message\x18\x03 \x01(\t\x12\x41\n\x06\x62utton\x18\x04 \x01(\x0b\x32\x31.bilibili.app.playerunite.ugcanymodel.ButtonStyle\"R\n\x0bUGCAnyModel\x12\x43\n\nplay_limit\x18\x01 \x01(\x0b\x32/.bilibili.app.playerunite.ugcanymodel.PlayLimit*2\n\rPlayLimitCode\x12\x0f\n\x0bPLC_UNKNOWN\x10\x00\x12\x10\n\x0cPLC_NOTPAYED\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.playerunite.ugcanymodel.ugcanymodel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PLAYLIMITCODE']._serialized_start=452
  _globals['_PLAYLIMITCODE']._serialized_end=502
  _globals['_BUTTONSTYLE']._serialized_start=96
  _globals['_BUTTONSTYLE']._serialized_end=180
  _globals['_PLAYLIMIT']._serialized_start=183
  _globals['_PLAYLIMIT']._serialized_end=366
  _globals['_UGCANYMODEL']._serialized_start=368
  _globals['_UGCANYMODEL']._serialized_end=450
# @@protoc_insertion_point(module_scope)
