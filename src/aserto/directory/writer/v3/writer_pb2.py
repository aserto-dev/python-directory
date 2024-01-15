# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aserto/directory/writer/v3/writer.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from aserto.directory.common.v3 import common_pb2 as aserto_dot_directory_dot_common_dot_v3_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/writer/v3/writer.proto\x12\x1a\x61serto.directory.writer.v3\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\'aserto/directory/common/v3/common.proto\"Z\n\x10SetObjectRequest\x12\x46\n\x06object\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectB\n\xe2\x41\x01\x02\xbaH\x03\xc8\x01\x01R\x06object\"O\n\x11SetObjectResponse\x12:\n\x06result\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectR\x06result\"\xf6\x03\n\x13\x44\x65leteObjectRequest\x12\x92\x02\n\x0bobject_type\x18\x01 \x01(\tB\xf0\x01\xe2\x41\x01\x02\xbaH\xe8\x01r\x02\x18@\xba\x01\xdd\x01\n\x19\x64\x65lete_object.object_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\nobjectType\x12\x9c\x01\n\tobject_id\x18\x02 \x01(\tB\x7f\xe2\x41\x01\x02\xbaHxr\x03\x18\x80\x02\xba\x01m\n\x17\x64\x65lete_object.object_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\x08objectId\x12+\n\x0ewith_relations\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01R\rwithRelations\"F\n\x14\x44\x65leteObjectResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"b\n\x12SetRelationRequest\x12L\n\x08relation\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v3.RelationB\n\xe2\x41\x01\x02\xbaH\x03\xc8\x01\x01R\x08relation\"S\n\x13SetRelationResponse\x12<\n\x06result\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v3.RelationR\x06result\"\xc1\x0b\n\x15\x44\x65leteRelationRequest\x12\x91\x02\n\x0bobject_type\x18\x01 \x01(\tB\xef\x01\xe2\x41\x01\x02\xbaH\xe7\x01r\x02\x18@\xba\x01\xdf\x01\n\x1b\x64\x65lete_relation.object_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')R\nobjectType\x12\x9f\x01\n\tobject_id\x18\x02 \x01(\tB\x81\x01\xe2\x41\x01\x02\xbaHzr\x03\x18\x80\x02\xba\x01o\n\x19\x64\x65lete_relation.object_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\x08objectId\x12\x8c\x02\n\x08relation\x18\x03 \x01(\tB\xef\x01\xe2\x41\x01\x02\xbaH\xe7\x01r\x02\x18@\xba\x01\xdc\x01\n\x18\x64\x65lete_relation.relation\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\x08relation\x12\x97\x02\n\x0csubject_type\x18\x04 \x01(\tB\xf3\x01\xe2\x41\x01\x02\xbaH\xeb\x01r\x02\x18@\xba\x01\xe0\x01\n\x1c\x64\x65lete_relation.subject_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\x0bsubjectType\x12\xa2\x01\n\nsubject_id\x18\x05 \x01(\tB\x82\x01\xe2\x41\x01\x02\xbaH{r\x03\x18\x80\x02\xba\x01p\n\x1a\x64\x65lete_relation.subject_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\tsubjectId\x12\xa3\x02\n\x10subject_relation\x18\x06 \x01(\tB\xf7\x01\xe2\x41\x01\x01\xbaH\xef\x01r\x02\x18@\xba\x01\xe4\x01\n delete_relation.subject_relation\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xd0\x01\x01R\x0fsubjectRelation\"H\n\x16\x44\x65leteRelationResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result2\xb4\x08\n\x06Writer\x12\xf3\x01\n\tSetObject\x12,.aserto.directory.writer.v3.SetObjectRequest\x1a-.aserto.directory.writer.v3.SetObjectResponse\"\x88\x01\x92\x41\x62\n\tdirectory\x12\nSet object\x1a\x0bSet object.*\x17\x64irectory.v3.object.setb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1d\"\x18/api/v3/directory/object:\x01*\x12\x9c\x02\n\x0c\x44\x65leteObject\x12/.aserto.directory.writer.v3.DeleteObjectRequest\x1a\x30.aserto.directory.writer.v3.DeleteObjectResponse\"\xa8\x01\x92\x41k\n\tdirectory\x12\rDelete object\x1a\x0e\x44\x65lete object.*\x1a\x64irectory.v3.object.deleteb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x34*2/api/v3/directory/object/{object_type}/{object_id}\x12\x81\x02\n\x0bSetRelation\x12..aserto.directory.writer.v3.SetRelationRequest\x1a/.aserto.directory.writer.v3.SetRelationResponse\"\x90\x01\x92\x41h\n\tdirectory\x12\x0cSet relation\x1a\rSet relation.*\x19\x64irectory.v3.relation.setb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v3/directory/relation:\x01*\x12\x90\x02\n\x0e\x44\x65leteRelation\x12\x31.aserto.directory.writer.v3.DeleteRelationRequest\x1a\x32.aserto.directory.writer.v3.DeleteRelationResponse\"\x96\x01\x92\x41q\n\tdirectory\x12\x0f\x44\x65lete relation\x1a\x10\x44\x65lete relation.*\x1c\x64irectory.v3.relation.deleteb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1c*\x1a/api/v3/directory/relationB\x80\x02\n\x1e\x63om.aserto.directory.writer.v3B\x0bWriterProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/writer/v3;writer\xa2\x02\x03\x41\x44W\xaa\x02\x1a\x41serto.Directory.Writer.V3\xca\x02\x1b\x41serto\\Directory_\\Writer\\V3\xe2\x02\'Aserto\\Directory_\\Writer\\V3\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Writer::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.writer.v3.writer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.writer.v3B\013WriterProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/writer/v3;writer\242\002\003ADW\252\002\032Aserto.Directory.Writer.V3\312\002\033Aserto\\Directory_\\Writer\\V3\342\002\'Aserto\\Directory_\\Writer\\V3\\GPBMetadata\352\002\035Aserto::Directory::Writer::V3'
  _globals['_SETOBJECTREQUEST'].fields_by_name['object']._options = None
  _globals['_SETOBJECTREQUEST'].fields_by_name['object']._serialized_options = b'\342A\001\002\272H\003\310\001\001'
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_type']._options = None
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_type']._serialized_options = b'\342A\001\002\272H\350\001r\002\030@\272\001\335\001\n\031delete_object.object_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_id']._options = None
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['object_id']._serialized_options = b'\342A\001\002\272Hxr\003\030\200\002\272\001m\n\027delete_object.object_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['with_relations']._options = None
  _globals['_DELETEOBJECTREQUEST'].fields_by_name['with_relations']._serialized_options = b'\342A\001\001'
  _globals['_SETRELATIONREQUEST'].fields_by_name['relation']._options = None
  _globals['_SETRELATIONREQUEST'].fields_by_name['relation']._serialized_options = b'\342A\001\002\272H\003\310\001\001'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_type']._options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_type']._serialized_options = b'\342A\001\002\272H\347\001r\002\030@\272\001\337\001\n\033delete_relation.object_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_id']._options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['object_id']._serialized_options = b'\342A\001\002\272Hzr\003\030\200\002\272\001o\n\031delete_relation.object_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['relation']._options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['relation']._serialized_options = b'\342A\001\002\272H\347\001r\002\030@\272\001\334\001\n\030delete_relation.relation\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_type']._options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_type']._serialized_options = b'\342A\001\002\272H\353\001r\002\030@\272\001\340\001\n\034delete_relation.subject_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_id']._options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_id']._serialized_options = b'\342A\001\002\272H{r\003\030\200\002\272\001p\n\032delete_relation.subject_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_relation']._options = None
  _globals['_DELETERELATIONREQUEST'].fields_by_name['subject_relation']._serialized_options = b'\342A\001\001\272H\357\001r\002\030@\272\001\344\001\n delete_relation.subject_relation\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\320\001\001'
  _globals['_WRITER'].methods_by_name['SetObject']._options = None
  _globals['_WRITER'].methods_by_name['SetObject']._serialized_options = b'\222Ab\n\tdirectory\022\nSet object\032\013Set object.*\027directory.v3.object.setb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\035\"\030/api/v3/directory/object:\001*'
  _globals['_WRITER'].methods_by_name['DeleteObject']._options = None
  _globals['_WRITER'].methods_by_name['DeleteObject']._serialized_options = b'\222Ak\n\tdirectory\022\rDelete object\032\016Delete object.*\032directory.v3.object.deleteb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\0024*2/api/v3/directory/object/{object_type}/{object_id}'
  _globals['_WRITER'].methods_by_name['SetRelation']._options = None
  _globals['_WRITER'].methods_by_name['SetRelation']._serialized_options = b'\222Ah\n\tdirectory\022\014Set relation\032\rSet relation.*\031directory.v3.relation.setb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\037\"\032/api/v3/directory/relation:\001*'
  _globals['_WRITER'].methods_by_name['DeleteRelation']._options = None
  _globals['_WRITER'].methods_by_name['DeleteRelation']._serialized_options = b'\222Aq\n\tdirectory\022\017Delete relation\032\020Delete relation.*\034directory.v3.relation.deleteb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\034*\032/api/v3/directory/relation'
  _globals['_SETOBJECTREQUEST']._serialized_start=281
  _globals['_SETOBJECTREQUEST']._serialized_end=371
  _globals['_SETOBJECTRESPONSE']._serialized_start=373
  _globals['_SETOBJECTRESPONSE']._serialized_end=452
  _globals['_DELETEOBJECTREQUEST']._serialized_start=455
  _globals['_DELETEOBJECTREQUEST']._serialized_end=957
  _globals['_DELETEOBJECTRESPONSE']._serialized_start=959
  _globals['_DELETEOBJECTRESPONSE']._serialized_end=1029
  _globals['_SETRELATIONREQUEST']._serialized_start=1031
  _globals['_SETRELATIONREQUEST']._serialized_end=1129
  _globals['_SETRELATIONRESPONSE']._serialized_start=1131
  _globals['_SETRELATIONRESPONSE']._serialized_end=1214
  _globals['_DELETERELATIONREQUEST']._serialized_start=1217
  _globals['_DELETERELATIONREQUEST']._serialized_end=2690
  _globals['_DELETERELATIONRESPONSE']._serialized_start=2692
  _globals['_DELETERELATIONRESPONSE']._serialized_end=2764
  _globals['_WRITER']._serialized_start=2767
  _globals['_WRITER']._serialized_end=3843
# @@protoc_insertion_point(module_scope)
