# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aserto/directory/exporter/v3/exporter.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aserto.directory.common.v3 import common_pb2 as aserto_dot_directory_dot_common_dot_v3_dot_common__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+aserto/directory/exporter/v3/exporter.proto\x12\x1c\x61serto.directory.exporter.v3\x1a\'aserto/directory/common/v3/common.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"d\n\rExportRequest\x12\x18\n\x07options\x18\x01 \x01(\rR\x07options\x12\x39\n\nstart_from\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartFrom\"\xca\x01\n\x0e\x45xportResponse\x12<\n\x06object\x18\x02 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectH\x00R\x06object\x12\x42\n\x08relation\x18\x04 \x01(\x0b\x32$.aserto.directory.common.v3.RelationH\x00R\x08relation\x12/\n\x05stats\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructH\x00R\x05statsB\x05\n\x03msg*s\n\x06Option\x12\x12\n\x0eOPTION_UNKNOWN\x10\x00\x12\x17\n\x13OPTION_DATA_OBJECTS\x10\x08\x12\x19\n\x15OPTION_DATA_RELATIONS\x10\x10\x12\x0f\n\x0bOPTION_DATA\x10\x18\x12\x10\n\x0cOPTION_STATS\x10@2s\n\x08\x45xporter\x12g\n\x06\x45xport\x12+.aserto.directory.exporter.v3.ExportRequest\x1a,.aserto.directory.exporter.v3.ExportResponse\"\x00\x30\x01\x42\x90\x02\n com.aserto.directory.exporter.v3B\rExporterProtoP\x01ZHgithub.com/aserto-dev/go-directory/aserto/directory/exporter/v3;exporter\xa2\x02\x03\x41\x44\x45\xaa\x02\x1c\x41serto.Directory.Exporter.V3\xca\x02\x1d\x41serto\\Directory_\\Exporter\\V3\xe2\x02)Aserto\\Directory_\\Exporter\\V3\\GPBMetadata\xea\x02\x1f\x41serto::Directory::Exporter::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.exporter.v3.exporter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.aserto.directory.exporter.v3B\rExporterProtoP\001ZHgithub.com/aserto-dev/go-directory/aserto/directory/exporter/v3;exporter\242\002\003ADE\252\002\034Aserto.Directory.Exporter.V3\312\002\035Aserto\\Directory_\\Exporter\\V3\342\002)Aserto\\Directory_\\Exporter\\V3\\GPBMetadata\352\002\037Aserto::Directory::Exporter::V3'
  _globals['_OPTION']._serialized_start=488
  _globals['_OPTION']._serialized_end=603
  _globals['_EXPORTREQUEST']._serialized_start=181
  _globals['_EXPORTREQUEST']._serialized_end=281
  _globals['_EXPORTRESPONSE']._serialized_start=284
  _globals['_EXPORTRESPONSE']._serialized_end=486
  _globals['_EXPORTER']._serialized_start=605
  _globals['_EXPORTER']._serialized_end=720
# @@protoc_insertion_point(module_scope)
