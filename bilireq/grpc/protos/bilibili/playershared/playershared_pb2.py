# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/playershared/playershared.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(bilibili/playershared/playershared.proto\x12\x15\x62ilibili.playershared\"\x84\x01\n\x07\x41rcConf\x12\x12\n\nis_support\x18\x01 \x01(\x08\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12:\n\rextra_content\x18\x03 \x01(\x0b\x32#.bilibili.playershared.ExtraContent\x12\x17\n\x0funsupport_scene\x18\x04 \x03(\x05\"\xa1\x01\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\x12\x46\n\rreport_params\x18\x03 \x03(\x0b\x32/.bilibili.playershared.Button.ReportParamsEntry\x1a\x33\n\x11ReportParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"B\n\tConfValue\x12\x14\n\nswitch_val\x18\x01 \x01(\x05H\x00\x12\x16\n\x0cselected_val\x18\x02 \x01(\x05H\x00\x42\x07\n\x05value\"\xa6\x01\n\x08\x44\x61shItem\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08\x62\x61se_url\x18\x02 \x01(\t\x12\x12\n\nbackup_url\x18\x03 \x03(\t\x12\x11\n\tbandwidth\x18\x04 \x01(\r\x12\x0f\n\x07\x63odecid\x18\x05 \x01(\r\x12\x0b\n\x03md5\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\x04\x12\x12\n\nframe_rate\x18\x08 \x01(\t\x12\x15\n\rwidevine_pssh\x18\t \x01(\t\"\xe0\x01\n\tDashVideo\x12\x10\n\x08\x62\x61se_url\x18\x01 \x01(\t\x12\x12\n\nbackup_url\x18\x02 \x03(\t\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x63odecid\x18\x04 \x01(\r\x12\x0b\n\x03md5\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\x04\x12\x10\n\x08\x61udio_id\x18\x07 \x01(\r\x12\x12\n\nno_rexcode\x18\x08 \x01(\x08\x12\x12\n\nframe_rate\x18\t \x01(\t\x12\r\n\x05width\x18\n \x01(\x05\x12\x0e\n\x06height\x18\x0b \x01(\x05\x12\x15\n\rwidevine_pssh\x18\x0c \x01(\t\"B\n\nDeviceConf\x12\x34\n\nconf_value\x18\x01 \x01(\x0b\x32 .bilibili.playershared.ConfValue\":\n\tDimension\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x0e\n\x06rotate\x18\x03 \x01(\x05\"\x99\x01\n\tDolbyItem\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.bilibili.playershared.DolbyItem.Type\x12.\n\x05\x61udio\x18\x02 \x03(\x0b\x32\x1f.bilibili.playershared.DashItem\"\'\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x43OMMON\x10\x01\x12\t\n\x05\x41TMOS\x10\x02\"4\n\x05\x45vent\x12+\n\x05shake\x18\x01 \x01(\x0b\x32\x1c.bilibili.playershared.Shake\"<\n\x0c\x45xtraContent\x12\x16\n\x0e\x64isable_reason\x18\x01 \x01(\t\x12\x14\n\x0c\x64isable_code\x18\x02 \x01(\x03\"\x7f\n\x07History\x12\x39\n\rcurrent_video\x18\x01 \x01(\x0b\x32\".bilibili.playershared.HistoryInfo\x12\x39\n\rrelated_video\x18\x02 \x01(\x0b\x32\".bilibili.playershared.HistoryInfo\"\xb4\x01\n\x0bHistoryInfo\x12\x10\n\x08progress\x18\x01 \x01(\x03\x12\x15\n\rlast_play_cid\x18\x02 \x01(\x03\x12+\n\x05toast\x18\x03 \x01(\x0b\x32\x1c.bilibili.playershared.Toast\x12\x38\n\x12toast_without_time\x18\x04 \x01(\x0b\x32\x1c.bilibili.playershared.Toast\x12\x15\n\rlast_play_aid\x18\x05 \x01(\x03\"r\n\x0bInteraction\x12\x31\n\x0chistory_node\x18\x01 \x01(\x0b\x32\x1b.bilibili.playershared.Node\x12\x15\n\rgraph_version\x18\x02 \x01(\x03\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x0c\n\x04mark\x18\x04 \x01(\x03\"k\n\x0cLossLessItem\x12\x19\n\x11is_lossless_audio\x18\x01 \x01(\x08\x12.\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1f.bilibili.playershared.DashItem\x12\x10\n\x08need_vip\x18\x03 \x01(\x08\"3\n\x04Node\x12\x0f\n\x07node_id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03\x63id\x18\x03 \x01(\x03\"\xb4\x02\n\x07PlayArc\x12\x34\n\nvideo_type\x18\x01 \x01(\x0e\x32 .bilibili.playershared.VideoType\x12\x0b\n\x03\x61id\x18\x02 \x01(\x04\x12\x0b\n\x03\x63id\x18\x03 \x01(\x04\x12\x39\n\rdrm_tech_type\x18\x04 \x01(\x0e\x32\".bilibili.playershared.DrmTechType\x12\x30\n\x08\x61rc_type\x18\x05 \x01(\x0e\x32\x1e.bilibili.playershared.ArcType\x12\x37\n\x0binteraction\x18\x06 \x01(\x0b\x32\".bilibili.playershared.Interaction\x12\x33\n\tdimension\x18\x07 \x01(\x0b\x32 .bilibili.playershared.Dimension\"\xa3\x01\n\x0bPlayArcConf\x12\x43\n\tarc_confs\x18\x01 \x03(\x0b\x32\x30.bilibili.playershared.PlayArcConf.ArcConfsEntry\x1aO\n\rArcConfsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.bilibili.playershared.ArcConf:\x02\x38\x01\"\xb5\x01\n\x0ePlayDeviceConf\x12L\n\x0c\x64\x65vice_confs\x18\x01 \x03(\x0b\x32\x36.bilibili.playershared.PlayDeviceConf.DeviceConfsEntry\x1aU\n\x10\x44\x65viceConfsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.bilibili.playershared.DeviceConf:\x02\x38\x01\"\xff\x01\n\x0bQnTrialInfo\x12\x12\n\ntrial_able\x18\x01 \x01(\x08\x12\x17\n\x0fremaining_times\x18\x02 \x01(\x05\x12\r\n\x05start\x18\x03 \x01(\x05\x12\x13\n\x0btime_length\x18\x04 \x01(\x05\x12\x31\n\x0bstart_toast\x18\x05 \x01(\x0b\x32\x1c.bilibili.playershared.Toast\x12/\n\tend_toast\x18\x06 \x01(\x0b\x32\x1c.bilibili.playershared.Toast\x12;\n\x14quality_open_tip_btn\x18\x08 \x01(\x0b\x32\x1d.bilibili.playershared.Button\"n\n\x0cResponseDash\x12.\n\x05video\x18\x01 \x03(\x0b\x32\x1f.bilibili.playershared.DashItem\x12.\n\x05\x61udio\x18\x02 \x03(\x0b\x32\x1f.bilibili.playershared.DashItem\"h\n\x0bResponseUrl\x12\r\n\x05order\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x12\n\nbackup_url\x18\x05 \x03(\t\x12\x0b\n\x03md5\x18\x06 \x01(\t\"\x81\x01\n\x06Scheme\x12=\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32(.bilibili.playershared.Scheme.ActionType\x12\r\n\x05toast\x18\x02 \x01(\t\")\n\nActionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nSHOW_TOAST\x10\x01\"C\n\x0cSegmentVideo\x12\x33\n\x07segment\x18\x01 \x03(\x0b\x32\".bilibili.playershared.ResponseUrl\"\x15\n\x05Shake\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"\xc1\x01\n\x06Stream\x12\x36\n\x0bstream_info\x18\x01 \x01(\x0b\x32!.bilibili.playershared.StreamInfo\x12\x36\n\ndash_video\x18\x02 \x01(\x0b\x32 .bilibili.playershared.DashVideoH\x00\x12<\n\rsegment_video\x18\x03 \x01(\x0b\x32#.bilibili.playershared.SegmentVideoH\x00\x42\t\n\x07\x63ontent\"\x90\x03\n\nStreamInfo\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x65rr_code\x18\x04 \x01(\r\x12\x31\n\x05limit\x18\x05 \x01(\x0b\x32\".bilibili.playershared.StreamLimit\x12\x10\n\x08need_vip\x18\x06 \x01(\x08\x12\x12\n\nneed_login\x18\x07 \x01(\x08\x12\x0e\n\x06intact\x18\x08 \x01(\x08\x12\x12\n\nno_rexcode\x18\t \x01(\x08\x12\x11\n\tattribute\x18\n \x01(\x03\x12\x17\n\x0fnew_description\x18\x0b \x01(\t\x12\x14\n\x0c\x64isplay_desc\x18\x0c \x01(\t\x12\x13\n\x0bsuperscript\x18\r \x01(\t\x12\x10\n\x08vip_free\x18\x0e \x01(\x08\x12\x10\n\x08subtitle\x18\x0f \x01(\t\x12-\n\x06scheme\x18\x10 \x01(\x0b\x32\x1d.bilibili.playershared.Scheme\x12\x13\n\x0bsupport_drm\x18\x11 \x01(\x08\"6\n\x0bStreamLimit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"D\n\x05Toast\x12\x0c\n\x04text\x18\x01 \x01(\t\x12-\n\x06\x62utton\x18\x02 \x01(\x0b\x32\x1d.bilibili.playershared.Button\"\xd6\x01\n\x08VideoVod\x12\x0b\n\x03\x61id\x18\x01 \x01(\x05\x12\x0b\n\x03\x63id\x18\x02 \x01(\x05\x12\n\n\x02qn\x18\x03 \x01(\x04\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x12\n\nforce_host\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12:\n\x11prefer_codec_type\x18\t \x01(\x0e\x32\x1f.bilibili.playershared.CodeType\x12\x15\n\rvoice_balance\x18\n \x01(\x04\"\xf8\x02\n\x07VodInfo\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x12\n\ntimelength\x18\x03 \x01(\x04\x12\x15\n\rvideo_codecid\x18\x04 \x01(\r\x12\x32\n\x0bstream_list\x18\x05 \x03(\x0b\x32\x1d.bilibili.playershared.Stream\x12\x33\n\ndash_audio\x18\x06 \x03(\x0b\x32\x1f.bilibili.playershared.DashItem\x12/\n\x05\x64olby\x18\x07 \x01(\x0b\x32 .bilibili.playershared.DolbyItem\x12\x31\n\x06volume\x18\x08 \x01(\x0b\x32!.bilibili.playershared.VolumeInfo\x12;\n\x0eloss_less_item\x18\t \x01(\x0b\x32#.bilibili.playershared.LossLessItem\x12\x17\n\x0fsupport_project\x18\n \x01(\x08\"\xa3\x01\n\nVolumeInfo\x12\x12\n\nmeasured_i\x18\x01 \x01(\x01\x12\x14\n\x0cmeasured_lra\x18\x02 \x01(\x01\x12\x13\n\x0bmeasured_tp\x18\x03 \x01(\x01\x12\x1a\n\x12measured_threshold\x18\x04 \x01(\x01\x12\x15\n\rtarget_offset\x18\x05 \x01(\x01\x12\x10\n\x08target_i\x18\x06 \x01(\x01\x12\x11\n\ttarget_tp\x18\x07 \x01(\x01*5\n\x07\x41rcType\x12\x13\n\x0f\x41RC_TYPE_NORMAL\x10\x00\x12\x15\n\x11\x41RC_TYPE_INTERACT\x10\x01*=\n\x08\x43odeType\x12\n\n\x06NOCODE\x10\x00\x12\x0b\n\x07\x43ODE264\x10\x01\x12\x0b\n\x07\x43ODE265\x10\x02\x12\x0b\n\x07\x43ODEAV1\x10\x03*\x9a\x04\n\x08\x43onfType\x12\n\n\x06NoType\x10\x00\x12\x0c\n\x08\x46LIPCONF\x10\x01\x12\x0c\n\x08\x43\x41STCONF\x10\x02\x12\x0c\n\x08\x46\x45\x45\x44\x42\x41\x43K\x10\x03\x12\x0c\n\x08SUBTITLE\x10\x04\x12\x10\n\x0cPLAYBACKRATE\x10\x05\x12\n\n\x06TIMEUP\x10\x06\x12\x10\n\x0cPLAYBACKMODE\x10\x07\x12\r\n\tSCALEMODE\x10\x08\x12\x12\n\x0e\x42\x41\x43KGROUNDPLAY\x10\t\x12\x08\n\x04LIKE\x10\n\x12\x0b\n\x07\x44ISLIKE\x10\x0b\x12\x08\n\x04\x43OIN\x10\x0c\x12\x08\n\x04\x45LEC\x10\r\x12\t\n\x05SHARE\x10\x0e\x12\x0e\n\nSCREENSHOT\x10\x0f\x12\x0e\n\nLOCKSCREEN\x10\x10\x12\r\n\tRECOMMEND\x10\x11\x12\x11\n\rPLAYBACKSPEED\x10\x12\x12\x0e\n\nDEFINITION\x10\x13\x12\x0e\n\nSELECTIONS\x10\x14\x12\x08\n\x04NEXT\x10\x15\x12\n\n\x06\x45\x44ITDM\x10\x16\x12\x0f\n\x0bSMALLWINDOW\x10\x17\x12\t\n\x05SHAKE\x10\x18\x12\x0b\n\x07OUTERDM\x10\x19\x12\x0b\n\x07INNERDM\x10\x1a\x12\x0c\n\x08PANORAMA\x10\x1b\x12\t\n\x05\x44OLBY\x10\x1c\x12\x0f\n\x0b\x43OLORFILTER\x10\x1d\x12\x0c\n\x08LOSSLESS\x10\x1e\x12\x0e\n\nFREYAENTER\x10\x1f\x12\x12\n\x0e\x46REYAFULLENTER\x10 \x12\x0c\n\x08SKIPOPED\x10!\x12\x10\n\x0cRECORDSCREEN\x10\"\x12\x0b\n\x07\x44UBBING\x10#\x12\n\n\x06LISTEN\x10$*J\n\x0b\x44rmTechType\x12\x0f\n\x0bUNKNOWN_DRM\x10\x00\x12\r\n\tFAIR_PLAY\x10\x01\x12\r\n\tWIDE_VINE\x10\x02\x12\x0c\n\x08\x42ILI_DRM\x10\x03*1\n\x07PlayErr\x12\t\n\x05NoErr\x10\x00\x12\x1b\n\x17WithMultiDeviceLoginErr\x10\x01*1\n\x0eUnsupportScene\x12\x11\n\rUNKNOWN_SCENE\x10\x00\x12\x0c\n\x08PREMIERE\x10\x01**\n\tVideoType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03UGC\x10\x01\x12\x07\n\x03PGC\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.playershared.playershared_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUTTON_REPORTPARAMSENTRY._options = None
  _BUTTON_REPORTPARAMSENTRY._serialized_options = b'8\001'
  _PLAYARCCONF_ARCCONFSENTRY._options = None
  _PLAYARCCONF_ARCCONFSENTRY._serialized_options = b'8\001'
  _PLAYDEVICECONF_DEVICECONFSENTRY._options = None
  _PLAYDEVICECONF_DEVICECONFSENTRY._serialized_options = b'8\001'
  _globals['_ARCTYPE']._serialized_start=4668
  _globals['_ARCTYPE']._serialized_end=4721
  _globals['_CODETYPE']._serialized_start=4723
  _globals['_CODETYPE']._serialized_end=4784
  _globals['_CONFTYPE']._serialized_start=4787
  _globals['_CONFTYPE']._serialized_end=5325
  _globals['_DRMTECHTYPE']._serialized_start=5327
  _globals['_DRMTECHTYPE']._serialized_end=5401
  _globals['_PLAYERR']._serialized_start=5403
  _globals['_PLAYERR']._serialized_end=5452
  _globals['_UNSUPPORTSCENE']._serialized_start=5454
  _globals['_UNSUPPORTSCENE']._serialized_end=5503
  _globals['_VIDEOTYPE']._serialized_start=5505
  _globals['_VIDEOTYPE']._serialized_end=5547
  _globals['_ARCCONF']._serialized_start=68
  _globals['_ARCCONF']._serialized_end=200
  _globals['_BUTTON']._serialized_start=203
  _globals['_BUTTON']._serialized_end=364
  _globals['_BUTTON_REPORTPARAMSENTRY']._serialized_start=313
  _globals['_BUTTON_REPORTPARAMSENTRY']._serialized_end=364
  _globals['_CONFVALUE']._serialized_start=366
  _globals['_CONFVALUE']._serialized_end=432
  _globals['_DASHITEM']._serialized_start=435
  _globals['_DASHITEM']._serialized_end=601
  _globals['_DASHVIDEO']._serialized_start=604
  _globals['_DASHVIDEO']._serialized_end=828
  _globals['_DEVICECONF']._serialized_start=830
  _globals['_DEVICECONF']._serialized_end=896
  _globals['_DIMENSION']._serialized_start=898
  _globals['_DIMENSION']._serialized_end=956
  _globals['_DOLBYITEM']._serialized_start=959
  _globals['_DOLBYITEM']._serialized_end=1112
  _globals['_DOLBYITEM_TYPE']._serialized_start=1073
  _globals['_DOLBYITEM_TYPE']._serialized_end=1112
  _globals['_EVENT']._serialized_start=1114
  _globals['_EVENT']._serialized_end=1166
  _globals['_EXTRACONTENT']._serialized_start=1168
  _globals['_EXTRACONTENT']._serialized_end=1228
  _globals['_HISTORY']._serialized_start=1230
  _globals['_HISTORY']._serialized_end=1357
  _globals['_HISTORYINFO']._serialized_start=1360
  _globals['_HISTORYINFO']._serialized_end=1540
  _globals['_INTERACTION']._serialized_start=1542
  _globals['_INTERACTION']._serialized_end=1656
  _globals['_LOSSLESSITEM']._serialized_start=1658
  _globals['_LOSSLESSITEM']._serialized_end=1765
  _globals['_NODE']._serialized_start=1767
  _globals['_NODE']._serialized_end=1818
  _globals['_PLAYARC']._serialized_start=1821
  _globals['_PLAYARC']._serialized_end=2129
  _globals['_PLAYARCCONF']._serialized_start=2132
  _globals['_PLAYARCCONF']._serialized_end=2295
  _globals['_PLAYARCCONF_ARCCONFSENTRY']._serialized_start=2216
  _globals['_PLAYARCCONF_ARCCONFSENTRY']._serialized_end=2295
  _globals['_PLAYDEVICECONF']._serialized_start=2298
  _globals['_PLAYDEVICECONF']._serialized_end=2479
  _globals['_PLAYDEVICECONF_DEVICECONFSENTRY']._serialized_start=2394
  _globals['_PLAYDEVICECONF_DEVICECONFSENTRY']._serialized_end=2479
  _globals['_QNTRIALINFO']._serialized_start=2482
  _globals['_QNTRIALINFO']._serialized_end=2737
  _globals['_RESPONSEDASH']._serialized_start=2739
  _globals['_RESPONSEDASH']._serialized_end=2849
  _globals['_RESPONSEURL']._serialized_start=2851
  _globals['_RESPONSEURL']._serialized_end=2955
  _globals['_SCHEME']._serialized_start=2958
  _globals['_SCHEME']._serialized_end=3087
  _globals['_SCHEME_ACTIONTYPE']._serialized_start=3046
  _globals['_SCHEME_ACTIONTYPE']._serialized_end=3087
  _globals['_SEGMENTVIDEO']._serialized_start=3089
  _globals['_SEGMENTVIDEO']._serialized_end=3156
  _globals['_SHAKE']._serialized_start=3158
  _globals['_SHAKE']._serialized_end=3179
  _globals['_STREAM']._serialized_start=3182
  _globals['_STREAM']._serialized_end=3375
  _globals['_STREAMINFO']._serialized_start=3378
  _globals['_STREAMINFO']._serialized_end=3778
  _globals['_STREAMLIMIT']._serialized_start=3780
  _globals['_STREAMLIMIT']._serialized_end=3834
  _globals['_TOAST']._serialized_start=3836
  _globals['_TOAST']._serialized_end=3904
  _globals['_VIDEOVOD']._serialized_start=3907
  _globals['_VIDEOVOD']._serialized_end=4121
  _globals['_VODINFO']._serialized_start=4124
  _globals['_VODINFO']._serialized_end=4500
  _globals['_VOLUMEINFO']._serialized_start=4503
  _globals['_VOLUMEINFO']._serialized_end=4666
# @@protoc_insertion_point(module_scope)
