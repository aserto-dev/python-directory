# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/writer/v3/writer.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'aserto/directory/writer/v3/writer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aserto.directory.common.v3 import common_pb2 as aserto_dot_directory_dot_common_dot_v3_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/writer/v3/writer.proto\x12\x1a\x61serto.directory.writer.v3\x1a\'aserto/directory/common/v3/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"S\n\x10SetObjectRequest\x12?\n\x06object\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectB\x03\xe0\x41\x02R\x06object\"O\n\x11SetObjectResponse\x12:\n\x06result\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectR\x06result\"\x89\x01\n\x13\x44\x65leteObjectRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12*\n\x0ewith_relations\x18\x03 \x01(\x08\x42\x03\xe0\x41\x01R\rwithRelations\"F\n\x14\x44\x65leteObjectResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"[\n\x12SetRelationRequest\x12\x45\n\x08relation\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v3.RelationB\x03\xe0\x41\x02R\x08relation\"S\n\x13SetRelationResponse\x12<\n\x06result\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v3.RelationR\x06result\"\xfc\x01\n\x15\x44\x65leteRelationRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12\x1f\n\x08relation\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x08relation\x12&\n\x0csubject_type\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x0bsubjectType\x12\"\n\nsubject_id\x18\x05 \x01(\tB\x03\xe0\x41\x02R\tsubjectId\x12.\n\x10subject_relation\x18\x06 \x01(\tB\x03\xe0\x41\x01R\x0fsubjectRelation\"H\n\x16\x44\x65leteRelationResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result2\xd0\x08\n\x06Writer\x12\xfa\x01\n\tSetObject\x12,.aserto.directory.writer.v3.SetObjectRequest\x1a-.aserto.directory.writer.v3.SetObjectResponse\"\x8f\x01\x92\x41i\n\tdirectory\x12\nSet object\x1a\x0bSet object.*\x1e\x64irectory.writer.v3.object.setb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1d\"\x18/api/v3/directory/object:\x01*\x12\xa3\x02\n\x0c\x44\x65leteObject\x12/.aserto.directory.writer.v3.DeleteObjectRequest\x1a\x30.aserto.directory.writer.v3.DeleteObjectResponse\"\xaf\x01\x92\x41r\n\tdirectory\x12\rDelete object\x1a\x0e\x44\x65lete object.*!directory.writer.v3.object.deleteb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x34*2/api/v3/directory/object/{object_type}/{object_id}\x12\x88\x02\n\x0bSetRelation\x12..aserto.directory.writer.v3.SetRelationRequest\x1a/.aserto.directory.writer.v3.SetRelationResponse\"\x97\x01\x92\x41o\n\tdirectory\x12\x0cSet relation\x1a\rSet relation.* directory.writer.v3.relation.setb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v3/directory/relation:\x01*\x12\x97\x02\n\x0e\x44\x65leteRelation\x12\x31.aserto.directory.writer.v3.DeleteRelationRequest\x1a\x32.aserto.directory.writer.v3.DeleteRelationResponse\"\x9d\x01\x92\x41x\n\tdirectory\x12\x0f\x44\x65lete relation\x1a\x10\x44\x65lete relation.*#directory.writer.v3.relation.deleteb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1c*\x1a/api/v3/directory/relationB\x80\x02\n\x1e\x63om.aserto.directory.writer.v3B\x0bWriterProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/writer/v3;writer\xa2\x02\x03\x41\x44W\xaa\x02\x1a\x41serto.Directory.Writer.V3\xca\x02\x1b\x41serto\\Directory_\\Writer\\V3\xe2\x02\'Aserto\\Directory_\\Writer\\V3\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Writer::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.writer.v3.writer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.writer.v3B\013WriterProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/writer/v3;writer\242\002\003ADW\252\002\032Aserto.Directory.Writer.V3\312\002\033Aserto\\Directory_\\Writer\\V3\342\002\'Aserto\\Directory_\\Writer\\V3\\GPBMetadata\352\002\035Aserto::Directory::Writer::V3'
  _globals['_SETOBJECTREQUEST'].fields_by_name['object']._loaded_options = None
  _globals['_SETOBJECTREQUEST'].fields_by_name['object']._serialized_options = b'\340A\002'
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['with_relations']._loaded_options = None
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['with_relations']._serialized_options = b'\340A\001'
  _globals['_SETRELATIONREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_SETRELATIONREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\002'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\002'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\002'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\002'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_relation']._loaded_options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_relation']._serialized_options = b'\340A\001'
  _globals['_WRITER'].methods_by_name['SetObject']._loaded_options = None
  _globals['_WRITER'].methods_by_name['SetObject']._serialized_options = b'\222Ai\n\tdirectory\022\nSet object\032\013Set object.*\036directory.writer.v3.object.setb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\035\"\030/api/v3/directory/object:\001*'
  _globals['_WRITER'].methods_by_name['DeleteObject']._loaded_options = None
  _globals['_WRITER'].methods_by_name['DeleteObject']._serialized_options = b'\222Ar\n\tdirectory\022\rDelete object\032\016Delete object.*!directory.writer.v3.object.deleteb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\0024*2/api/v3/directory/object/{object_type}/{object_id}'
  _globals['_WRITER'].methods_by_name['SetRelation']._loaded_options = None
  _globals['_WRITER'].methods_by_name['SetRelation']._serialized_options = b'\222Ao\n\tdirectory\022\014Set relation\032\rSet relation.* directory.writer.v3.relation.setb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\037\"\032/api/v3/directory/relation:\001*'
  _globals['_WRITER'].methods_by_name['DeleteRelation']._loaded_options = None
  _globals['_WRITER'].methods_by_name['DeleteRelation']._serialized_options = b'\222Ax\n\tdirectory\022\017Delete relation\032\020Delete relation.*#directory.writer.v3.relation.deleteb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\034*\032/api/v3/directory/relation'
  _globals['_SETOBJECTREQUEST']._serialized_start=252
  _globals['_SETOBJECTREQUEST']._serialized_end=335
  _globals['_SETOBJECTRESPONSE']._serialized_start=337
  _globals['_SETOBJECTRESPONSE']._serialized_end=416
  _globals['_DELETEOBJECTREQUEST']._serialized_start=419
  _globals['_DELETEOBJECTREQUEST']._serialized_end=556
  _globals['_DELETEOBJECTRESPONSE']._serialized_start=558
  _globals['_DELETEOBJECTRESPONSE']._serialized_end=628
  _globals['_SETRELATIONREQUEST']._serialized_start=630
  _globals['_SETRELATIONREQUEST']._serialized_end=721
  _globals['_SETRELATIONRESPONSE']._serialized_start=723
  _globals['_SETRELATIONRESPONSE']._serialized_end=806
  _globals['_DELETERELATIONREQUEST']._serialized_start=809
  _globals['_DELETERELATIONREQUEST']._serialized_end=1061
  _globals['_DELETERELATIONRESPONSE']._serialized_start=1063
  _globals['_DELETERELATIONRESPONSE']._serialized_end=1135
  _globals['_WRITER']._serialized_start=1138
  _globals['_WRITER']._serialized_end=2242
# @@protoc_insertion_point(module_scope)
