# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/exporter/v2/exporter.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'aserto/directory/exporter/v2/exporter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aserto.directory.common.v2 import common_pb2 as aserto_dot_directory_dot_common_dot_v2_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+aserto/directory/exporter/v2/exporter.proto\x12\x1c\x61serto.directory.exporter.v2\x1a\'aserto/directory/common/v2/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"h\n\rExportRequest\x12\x18\n\x07options\x18\x01 \x01(\rR\x07options\x12\x39\n\nstart_from\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartFrom:\x02\x18\x01\"\x83\x03\n\x0e\x45xportResponse\x12<\n\x06object\x18\x02 \x01(\x0b\x32\".aserto.directory.common.v2.ObjectH\x00R\x06object\x12I\n\x0bobject_type\x18\x03 \x01(\x0b\x32&.aserto.directory.common.v2.ObjectTypeH\x00R\nobjectType\x12\x42\n\x08relation\x18\x04 \x01(\x0b\x32$.aserto.directory.common.v2.RelationH\x00R\x08relation\x12O\n\rrelation_type\x18\x05 \x01(\x0b\x32(.aserto.directory.common.v2.RelationTypeH\x00R\x0crelationType\x12H\n\npermission\x18\x06 \x01(\x0b\x32&.aserto.directory.common.v2.PermissionH\x00R\npermission:\x02\x18\x01\x42\x05\n\x03msg*\xcb\x02\n\x06Option\x12\x12\n\x0eOPTION_UNKNOWN\x10\x00\x12 \n\x1cOPTION_METADATA_OBJECT_TYPES\x10\x01\x12\"\n\x1eOPTION_METADATA_RELATION_TYPES\x10\x02\x12\x1f\n\x1bOPTION_METADATA_PERMISSIONS\x10\x04\x12\x13\n\x0fOPTION_METADATA\x10\x07\x12\x17\n\x13OPTION_DATA_OBJECTS\x10\x08\x12\x19\n\x15OPTION_DATA_RELATIONS\x10\x10\x12#\n\x1fOPTION_DATA_RELATIONS_WITH_KEYS\x10 \x12\x0f\n\x0bOPTION_DATA\x10\x18\x12\x19\n\x15OPTION_DATA_WITH_KEYS\x10(\x12\x0e\n\nOPTION_ALL\x10\x1f\x12\x18\n\x14OPTION_ALL_WITH_KEYS\x10/\x1a\x02\x18\x01\x32v\n\x08\x45xporter\x12j\n\x06\x45xport\x12+.aserto.directory.exporter.v2.ExportRequest\x1a,.aserto.directory.exporter.v2.ExportResponse\"\x03\x88\x02\x01\x30\x01\x42\x90\x02\n com.aserto.directory.exporter.v2B\rExporterProtoP\x01ZHgithub.com/aserto-dev/go-directory/aserto/directory/exporter/v2;exporter\xa2\x02\x03\x41\x44\x45\xaa\x02\x1c\x41serto.Directory.Exporter.V2\xca\x02\x1d\x41serto\\Directory_\\Exporter\\V2\xe2\x02)Aserto\\Directory_\\Exporter\\V2\\GPBMetadata\xea\x02\x1f\x41serto::Directory::Exporter::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.exporter.v2.exporter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.aserto.directory.exporter.v2B\rExporterProtoP\001ZHgithub.com/aserto-dev/go-directory/aserto/directory/exporter/v2;exporter\242\002\003ADE\252\002\034Aserto.Directory.Exporter.V2\312\002\035Aserto\\Directory_\\Exporter\\V2\342\002)Aserto\\Directory_\\Exporter\\V2\\GPBMetadata\352\002\037Aserto::Directory::Exporter::V2'
  _globals['_OPTION']._loaded_options = None
  _globals['_OPTION']._serialized_options = b'\030\001'
  _globals['_EXPORTREQUEST']._loaded_options = None
  _globals['_EXPORTREQUEST']._serialized_options = b'\030\001'
  _globals['_EXPORTRESPONSE']._loaded_options = None
  _globals['_EXPORTRESPONSE']._serialized_options = b'\030\001'
  _globals['_EXPORTER'].methods_by_name['Export']._loaded_options = None
  _globals['_EXPORTER'].methods_by_name['Export']._serialized_options = b'\210\002\001'
  _globals['_OPTION']._serialized_start=648
  _globals['_OPTION']._serialized_end=979
  _globals['_EXPORTREQUEST']._serialized_start=151
  _globals['_EXPORTREQUEST']._serialized_end=255
  _globals['_EXPORTRESPONSE']._serialized_start=258
  _globals['_EXPORTRESPONSE']._serialized_end=645
  _globals['_EXPORTER']._serialized_start=981
  _globals['_EXPORTER']._serialized_end=1099
# @@protoc_insertion_point(module_scope)
