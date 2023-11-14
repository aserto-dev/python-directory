# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aserto/directory/writer/v2/writer.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from aserto.directory.common.v2 import common_pb2 as aserto_dot_directory_dot_common_dot_v2_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/writer/v2/writer.proto\x12\x1a\x61serto.directory.writer.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\'aserto/directory/common/v2/common.proto\"_\n\x14SetObjectTypeRequest\x12G\n\x0bobject_type\x18\x01 \x01(\x0b\x32&.aserto.directory.common.v2.ObjectTypeR\nobjectType\"W\n\x15SetObjectTypeResponse\x12>\n\x06result\x18\x01 \x01(\x0b\x32&.aserto.directory.common.v2.ObjectTypeR\x06result\"a\n\x17\x44\x65leteObjectTypeRequest\x12\x46\n\x05param\x18\x01 \x01(\x0b\x32\x30.aserto.directory.common.v2.ObjectTypeIdentifierR\x05param\"J\n\x18\x44\x65leteObjectTypeResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"g\n\x16SetRelationTypeRequest\x12M\n\rrelation_type\x18\x01 \x01(\x0b\x32(.aserto.directory.common.v2.RelationTypeR\x0crelationType\"[\n\x17SetRelationTypeResponse\x12@\n\x06result\x18\x01 \x01(\x0b\x32(.aserto.directory.common.v2.RelationTypeR\x06result\"e\n\x19\x44\x65leteRelationTypeRequest\x12H\n\x05param\x18\x01 \x01(\x0b\x32\x32.aserto.directory.common.v2.RelationTypeIdentifierR\x05param\"L\n\x1a\x44\x65leteRelationTypeResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"^\n\x14SetPermissionRequest\x12\x46\n\npermission\x18\x01 \x01(\x0b\x32&.aserto.directory.common.v2.PermissionR\npermission\"W\n\x15SetPermissionResponse\x12>\n\x06result\x18\x01 \x01(\x0b\x32&.aserto.directory.common.v2.PermissionR\x06result\"a\n\x17\x44\x65letePermissionRequest\x12\x46\n\x05param\x18\x01 \x01(\x0b\x32\x30.aserto.directory.common.v2.PermissionIdentifierR\x05param\"J\n\x18\x44\x65letePermissionResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"N\n\x10SetObjectRequest\x12:\n\x06object\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v2.ObjectR\x06object\"O\n\x11SetObjectResponse\x12:\n\x06result\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v2.ObjectR\x06result\"\x98\x01\n\x13\x44\x65leteObjectRequest\x12\x42\n\x05param\x18\x01 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x05param\x12*\n\x0ewith_relations\x18\x02 \x01(\x08H\x00R\rwithRelations\x88\x01\x01\x42\x11\n\x0f_with_relations\"F\n\x14\x44\x65leteObjectResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"V\n\x12SetRelationRequest\x12@\n\x08relation\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v2.RelationR\x08relation\"S\n\x13SetRelationResponse\x12<\n\x06result\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v2.RelationR\x06result\"]\n\x15\x44\x65leteRelationRequest\x12\x44\n\x05param\x18\x01 \x01(\x0b\x32..aserto.directory.common.v2.RelationIdentifierR\x05param\"H\n\x16\x44\x65leteRelationResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result2\xce\t\n\x06Writer\x12v\n\rSetObjectType\x12\x30.aserto.directory.writer.v2.SetObjectTypeRequest\x1a\x31.aserto.directory.writer.v2.SetObjectTypeResponse\"\x00\x12\x7f\n\x10\x44\x65leteObjectType\x12\x33.aserto.directory.writer.v2.DeleteObjectTypeRequest\x1a\x34.aserto.directory.writer.v2.DeleteObjectTypeResponse\"\x00\x12|\n\x0fSetRelationType\x12\x32.aserto.directory.writer.v2.SetRelationTypeRequest\x1a\x33.aserto.directory.writer.v2.SetRelationTypeResponse\"\x00\x12\x85\x01\n\x12\x44\x65leteRelationType\x12\x35.aserto.directory.writer.v2.DeleteRelationTypeRequest\x1a\x36.aserto.directory.writer.v2.DeleteRelationTypeResponse\"\x00\x12v\n\rSetPermission\x12\x30.aserto.directory.writer.v2.SetPermissionRequest\x1a\x31.aserto.directory.writer.v2.SetPermissionResponse\"\x00\x12\x7f\n\x10\x44\x65letePermission\x12\x33.aserto.directory.writer.v2.DeletePermissionRequest\x1a\x34.aserto.directory.writer.v2.DeletePermissionResponse\"\x00\x12j\n\tSetObject\x12,.aserto.directory.writer.v2.SetObjectRequest\x1a-.aserto.directory.writer.v2.SetObjectResponse\"\x00\x12s\n\x0c\x44\x65leteObject\x12/.aserto.directory.writer.v2.DeleteObjectRequest\x1a\x30.aserto.directory.writer.v2.DeleteObjectResponse\"\x00\x12p\n\x0bSetRelation\x12..aserto.directory.writer.v2.SetRelationRequest\x1a/.aserto.directory.writer.v2.SetRelationResponse\"\x00\x12y\n\x0e\x44\x65leteRelation\x12\x31.aserto.directory.writer.v2.DeleteRelationRequest\x1a\x32.aserto.directory.writer.v2.DeleteRelationResponse\"\x00\x42\x80\x02\n\x1e\x63om.aserto.directory.writer.v2B\x0bWriterProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/writer/v2;writer\xa2\x02\x03\x41\x44W\xaa\x02\x1a\x41serto.Directory.Writer.V2\xca\x02\x1b\x41serto\\Directory_\\Writer\\V2\xe2\x02\'Aserto\\Directory_\\Writer\\V2\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Writer::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.writer.v2.writer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.writer.v2B\013WriterProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/writer/v2;writer\242\002\003ADW\252\002\032Aserto.Directory.Writer.V2\312\002\033Aserto\\Directory_\\Writer\\V2\342\002\'Aserto\\Directory_\\Writer\\V2\\GPBMetadata\352\002\035Aserto::Directory::Writer::V2'
  _globals['_SETOBJECTTYPEREQUEST']._serialized_start=141
  _globals['_SETOBJECTTYPEREQUEST']._serialized_end=236
  _globals['_SETOBJECTTYPERESPONSE']._serialized_start=238
  _globals['_SETOBJECTTYPERESPONSE']._serialized_end=325
  _globals['_DELETEOBJECTTYPEREQUEST']._serialized_start=327
  _globals['_DELETEOBJECTTYPEREQUEST']._serialized_end=424
  _globals['_DELETEOBJECTTYPERESPONSE']._serialized_start=426
  _globals['_DELETEOBJECTTYPERESPONSE']._serialized_end=500
  _globals['_SETRELATIONTYPEREQUEST']._serialized_start=502
  _globals['_SETRELATIONTYPEREQUEST']._serialized_end=605
  _globals['_SETRELATIONTYPERESPONSE']._serialized_start=607
  _globals['_SETRELATIONTYPERESPONSE']._serialized_end=698
  _globals['_DELETERELATIONTYPEREQUEST']._serialized_start=700
  _globals['_DELETERELATIONTYPEREQUEST']._serialized_end=801
  _globals['_DELETERELATIONTYPERESPONSE']._serialized_start=803
  _globals['_DELETERELATIONTYPERESPONSE']._serialized_end=879
  _globals['_SETPERMISSIONREQUEST']._serialized_start=881
  _globals['_SETPERMISSIONREQUEST']._serialized_end=975
  _globals['_SETPERMISSIONRESPONSE']._serialized_start=977
  _globals['_SETPERMISSIONRESPONSE']._serialized_end=1064
  _globals['_DELETEPERMISSIONREQUEST']._serialized_start=1066
  _globals['_DELETEPERMISSIONREQUEST']._serialized_end=1163
  _globals['_DELETEPERMISSIONRESPONSE']._serialized_start=1165
  _globals['_DELETEPERMISSIONRESPONSE']._serialized_end=1239
  _globals['_SETOBJECTREQUEST']._serialized_start=1241
  _globals['_SETOBJECTREQUEST']._serialized_end=1319
  _globals['_SETOBJECTRESPONSE']._serialized_start=1321
  _globals['_SETOBJECTRESPONSE']._serialized_end=1400
  _globals['_DELETEOBJECTREQUEST']._serialized_start=1403
  _globals['_DELETEOBJECTREQUEST']._serialized_end=1555
  _globals['_DELETEOBJECTRESPONSE']._serialized_start=1557
  _globals['_DELETEOBJECTRESPONSE']._serialized_end=1627
  _globals['_SETRELATIONREQUEST']._serialized_start=1629
  _globals['_SETRELATIONREQUEST']._serialized_end=1715
  _globals['_SETRELATIONRESPONSE']._serialized_start=1717
  _globals['_SETRELATIONRESPONSE']._serialized_end=1800
  _globals['_DELETERELATIONREQUEST']._serialized_start=1802
  _globals['_DELETERELATIONREQUEST']._serialized_end=1895
  _globals['_DELETERELATIONRESPONSE']._serialized_start=1897
  _globals['_DELETERELATIONRESPONSE']._serialized_end=1969
  _globals['_WRITER']._serialized_start=1972
  _globals['_WRITER']._serialized_end=3202
# @@protoc_insertion_point(module_scope)
