# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/playeronline/v1/playeronline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bilibili/app/playeronline/v1/playeronline.proto\x12\x1c\x62ilibili.app.playeronline.v1\"\t\n\x07NoReply\"\xa3\x01\n\x11PlayerOnlineReply\x12\x12\n\ntotal_text\x18\x01 \x01(\t\x12\x10\n\x08sec_next\x18\x02 \x01(\x03\x12\x13\n\x0b\x62ottom_show\x18\x03 \x01(\x08\x12\x10\n\x08sdm_show\x18\x04 \x01(\x08\x12\x10\n\x08sdm_text\x18\x05 \x01(\t\x12\x14\n\x0ctotal_number\x18\x06 \x01(\x03\x12\x19\n\x11total_number_text\x18\x07 \x01(\t\">\n\x0fPlayerOnlineReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\x11\n\tplay_open\x18\x03 \x01(\x08\"Y\n\x11PremiereInfoReply\x12\x1a\n\x12premiere_over_text\x18\x01 \x01(\t\x12\x13\n\x0bparticipant\x18\x02 \x01(\x03\x12\x13\n\x0binteraction\x18\x03 \x01(\x03\"\x1e\n\x0fPremiereInfoReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\"9\n\x0eReportWatchReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x62iz\x18\x02 \x01(\t\x12\r\n\x05\x62uvid\x18\x03 \x01(\t2\xd2\x02\n\x0cPlayerOnline\x12n\n\x0cPlayerOnline\x12-.bilibili.app.playeronline.v1.PlayerOnlineReq\x1a/.bilibili.app.playeronline.v1.PlayerOnlineReply\x12n\n\x0cPremiereInfo\x12-.bilibili.app.playeronline.v1.PremiereInfoReq\x1a/.bilibili.app.playeronline.v1.PremiereInfoReply\x12\x62\n\x0bReportWatch\x12,.bilibili.app.playeronline.v1.ReportWatchReq\x1a%.bilibili.app.playeronline.v1.NoReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.playeronline.v1.playeronline_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_NOREPLY']._serialized_start=81
  _globals['_NOREPLY']._serialized_end=90
  _globals['_PLAYERONLINEREPLY']._serialized_start=93
  _globals['_PLAYERONLINEREPLY']._serialized_end=256
  _globals['_PLAYERONLINEREQ']._serialized_start=258
  _globals['_PLAYERONLINEREQ']._serialized_end=320
  _globals['_PREMIEREINFOREPLY']._serialized_start=322
  _globals['_PREMIEREINFOREPLY']._serialized_end=411
  _globals['_PREMIEREINFOREQ']._serialized_start=413
  _globals['_PREMIEREINFOREQ']._serialized_end=443
  _globals['_REPORTWATCHREQ']._serialized_start=445
  _globals['_REPORTWATCHREQ']._serialized_end=502
  _globals['_PLAYERONLINE']._serialized_start=505
  _globals['_PLAYERONLINE']._serialized_end=843
# @@protoc_insertion_point(module_scope)
