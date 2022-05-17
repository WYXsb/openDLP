# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensitive.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsensitive.proto\x12*yunanbao.wf.sensitive_data_analyzer.api.v1\"f\n\x10SensitiveRequest\x12\x1c\n\x14to_analyze_file_path\x18\x01 \x01(\t\x12 \n\x18user_define_pattern_file\x18\x02 \x01(\t\x12\x12\n\nthresholds\x18\x03 \x01(\t\"g\n\x11SensitiveResponse\x12\x42\n\x06status\x18\x01 \x01(\x0b\x32\x32.yunanbao.wf.sensitive_data_analyzer.api.v1.Status\x12\x0e\n\x06result\x18\x02 \x01(\t\"[\n\x06Status\x12\x44\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x36.yunanbao.wf.sensitive_data_analyzer.api.v1.StatusCode\x12\x0b\n\x03msg\x18\x02 \x01(\t*}\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\x14\n\x0fPARAMETER_ERROR\x10\x90N\x12\x14\n\x0f\x46ILE_READ_ERROR\x10\x91N\x12\x1a\n\x15JSON_FILE_PARSE_ERROR\x10\x92N\x12\x1f\n\x1a\x41NY_COLUMN_RECOGNIZE_ERROR\x10\x93N2\xb2\x01\n\x1cSensitiveDataAnalyzerService\x12\x91\x01\n\x10SensitiveAnalyze\x12<.yunanbao.wf.sensitive_data_analyzer.api.v1.SensitiveRequest\x1a=.yunanbao.wf.sensitive_data_analyzer.api.v1.SensitiveResponse\"\x00\x42N\n.com.yunanbao.wf.sensitive_data_analyzer.api.v1B\x1aSensitiveDataAnalyzerProtoP\x01\x62\x06proto3')

_STATUSCODE = DESCRIPTOR.enum_types_by_name['StatusCode']
StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
OK = 0
PARAMETER_ERROR = 10000
FILE_READ_ERROR = 10001
JSON_FILE_PARSE_ERROR = 10002
ANY_COLUMN_RECOGNIZE_ERROR = 10003


_SENSITIVEREQUEST = DESCRIPTOR.message_types_by_name['SensitiveRequest']
_SENSITIVERESPONSE = DESCRIPTOR.message_types_by_name['SensitiveResponse']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
SensitiveRequest = _reflection.GeneratedProtocolMessageType('SensitiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENSITIVEREQUEST,
  '__module__' : 'sensitive_pb2'
  # @@protoc_insertion_point(class_scope:yunanbao.wf.sensitive_data_analyzer.api.v1.SensitiveRequest)
  })
_sym_db.RegisterMessage(SensitiveRequest)

SensitiveResponse = _reflection.GeneratedProtocolMessageType('SensitiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENSITIVERESPONSE,
  '__module__' : 'sensitive_pb2'
  # @@protoc_insertion_point(class_scope:yunanbao.wf.sensitive_data_analyzer.api.v1.SensitiveResponse)
  })
_sym_db.RegisterMessage(SensitiveResponse)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'sensitive_pb2'
  # @@protoc_insertion_point(class_scope:yunanbao.wf.sensitive_data_analyzer.api.v1.Status)
  })
_sym_db.RegisterMessage(Status)

_SENSITIVEDATAANALYZERSERVICE = DESCRIPTOR.services_by_name['SensitiveDataAnalyzerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n.com.yunanbao.wf.sensitive_data_analyzer.api.v1B\032SensitiveDataAnalyzerProtoP\001'
  _STATUSCODE._serialized_start=365
  _STATUSCODE._serialized_end=490
  _SENSITIVEREQUEST._serialized_start=63
  _SENSITIVEREQUEST._serialized_end=165
  _SENSITIVERESPONSE._serialized_start=167
  _SENSITIVERESPONSE._serialized_end=270
  _STATUS._serialized_start=272
  _STATUS._serialized_end=363
  _SENSITIVEDATAANALYZERSERVICE._serialized_start=493
  _SENSITIVEDATAANALYZERSERVICE._serialized_end=671
# @@protoc_insertion_point(module_scope)
