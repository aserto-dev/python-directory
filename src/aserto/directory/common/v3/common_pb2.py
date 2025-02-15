# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/common/v3/common.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'aserto/directory/common/v3/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/common/v3/common.proto\x12\x1a\x61serto.directory.common.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1b\x62uf/validate/validate.proto\"\x83\x05\n\x06Object\x12\xf6\x01\n\x04type\x18\x01 \x01(\tB\xe1\x01\xe0\x41\x02\xbaH\xda\x01r\x02\x18@\xba\x01\xcf\x01\n\x0bobject.type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\x04type\x12\x80\x01\n\x02id\x18\x02 \x01(\tBp\xe0\x41\x02\xbaHjr\x03\x18\x80\x02\xba\x01_\n\tobject.id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\x02id\x12&\n\x0c\x64isplay_name\x18\x03 \x01(\tB\x03\xe0\x41\x01R\x0b\x64isplayName\x12<\n\nproperties\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x01R\nproperties\x12>\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\tcreatedAt\x12>\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\tupdatedAt\x12\x17\n\x04\x65tag\x18\x17 \x01(\tB\x03\xe0\x41\x01R\x04\x65tag\"\x9e\x0c\n\x08Relation\x12\x8c\x02\n\x0bobject_type\x18\x01 \x01(\tB\xea\x01\xe0\x41\x02\xbaH\xe3\x01r\x02\x18@\xba\x01\xd8\x01\n\x14relation.object_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\nobjectType\x12\x96\x01\n\tobject_id\x18\x02 \x01(\tBy\xe0\x41\x02\xbaHsr\x03\x18\x80\x02\xba\x01h\n\x12relation.object_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\x08objectId\x12\x84\x02\n\x08relation\x18\x03 \x01(\tB\xe7\x01\xe0\x41\x02\xbaH\xe0\x01r\x02\x18@\xba\x01\xd5\x01\n\x11relation.relation\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\x08relation\x12\x8f\x02\n\x0csubject_type\x18\x04 \x01(\tB\xeb\x01\xe0\x41\x02\xbaH\xe4\x01r\x02\x18@\xba\x01\xd9\x01\n\x15relation.subject_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\x0bsubjectType\x12\x99\x01\n\nsubject_id\x18\x05 \x01(\tBz\xe0\x41\x02\xbaHtr\x03\x18\x80\x02\xba\x01i\n\x13relation.subject_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\tsubjectId\x12\x9b\x02\n\x10subject_relation\x18\x06 \x01(\tB\xef\x01\xe0\x41\x01\xbaH\xe8\x01r\x02\x18@\xba\x01\xdd\x01\n\x19relation.subject_relation\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xd0\x01\x01R\x0fsubjectRelation\x12>\n\ncreated_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\tcreatedAt\x12>\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\tupdatedAt\x12\x17\n\x04\x65tag\x18\x17 \x01(\tB\x03\xe0\x41\x01R\x04\x65tag\"\xcd\x03\n\x10ObjectIdentifier\x12\x95\x02\n\x0bobject_type\x18\x01 \x01(\tB\xf3\x01\xe0\x41\x02\xbaH\xec\x01r\x02\x18@\xba\x01\xe1\x01\n\x1dobject_identifier.object_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xc8\x01\x01R\nobjectType\x12\xa0\x01\n\tobject_id\x18\x02 \x01(\tB\x82\x01\xe0\x41\x02\xbaH|r\x03\x18\x80\x02\xba\x01q\n\x1bobject_identifier.object_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xc8\x01\x01R\x08objectId\"\xd3\x0b\n\x12RelationIdentifier\x12\x97\x02\n\x0bobject_type\x18\x01 \x01(\tB\xf5\x01\xe0\x41\x02\xbaH\xee\x01r\x02\x18@\xba\x01\xe3\x01\n\x1frelation_identifier.object_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xd0\x01\x01R\nobjectType\x12\xa2\x01\n\tobject_id\x18\x02 \x01(\tB\x84\x01\xe0\x41\x02\xbaH~r\x03\x18\x80\x02\xba\x01s\n\x1drelation_identifier.object_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xd0\x01\x01R\x08objectId\x12\x8f\x02\n\x08relation\x18\x03 \x01(\tB\xf2\x01\xe0\x41\x02\xbaH\xeb\x01r\x02\x18@\xba\x01\xe0\x01\n\x1crelation_identifier.relation\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xd0\x01\x01R\x08relation\x12\x9a\x02\n\x0csubject_type\x18\x04 \x01(\tB\xf6\x01\xe0\x41\x02\xbaH\xef\x01r\x02\x18@\xba\x01\xe4\x01\n relation_identifier.subject_type\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xd0\x01\x01R\x0bsubjectType\x12\xa5\x01\n\nsubject_id\x18\x05 \x01(\tB\x85\x01\xe0\x41\x02\xbaH\x7fr\x03\x18\x80\x02\xba\x01t\n\x1erelation_identifier.subject_id\x12\x38\x63\x61nnot contain any spaces or other whitespace characters\x1a\x18this.matches(\'^[\\\\S]+$\')\xd0\x01\x01R\tsubjectId\x12\xa6\x02\n\x10subject_relation\x18\x06 \x01(\tB\xfa\x01\xe0\x41\x01\xbaH\xf3\x01r\x02\x18@\xba\x01\xe8\x01\n$relation_identifier.subject_relation\x12\x8b\x01must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\x1a\x32this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\xd0\x01\x01R\x0fsubjectRelation\"P\n\x11PaginationRequest\x12 \n\x04size\x18\x01 \x01(\x05\x42\x0c\xe0\x41\x01\xbaH\x06\x1a\x04\x18\x64(\x01R\x04size\x12\x19\n\x05token\x18\x02 \x01(\tB\x03\xe0\x41\x01R\x05token\"8\n\x12PaginationResponse\x12\"\n\nnext_token\x18\x01 \x01(\tB\x03\xe0\x41\x03R\tnextTokenB\x80\x02\n\x1e\x63om.aserto.directory.common.v3B\x0b\x43ommonProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/common/v3;common\xa2\x02\x03\x41\x44\x43\xaa\x02\x1a\x41serto.Directory.Common.V3\xca\x02\x1b\x41serto\\Directory_\\Common\\V3\xe2\x02\'Aserto\\Directory_\\Common\\V3\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Common::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.common.v3.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.common.v3B\013CommonProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/common/v3;common\242\002\003ADC\252\002\032Aserto.Directory.Common.V3\312\002\033Aserto\\Directory_\\Common\\V3\342\002\'Aserto\\Directory_\\Common\\V3\\GPBMetadata\352\002\035Aserto::Directory::Common::V3'
  _globals['_OBJECT'].fields_by_name['type']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['type']._serialized_options = b'\340A\002\272H\332\001r\002\030@\272\001\317\001\n\013object.type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_OBJECT'].fields_by_name['id']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['id']._serialized_options = b'\340A\002\272Hjr\003\030\200\002\272\001_\n\tobject.id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_OBJECT'].fields_by_name['display_name']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['display_name']._serialized_options = b'\340A\001'
  _globals['_OBJECT'].fields_by_name['properties']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['properties']._serialized_options = b'\340A\001'
  _globals['_OBJECT'].fields_by_name['created_at']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['created_at']._serialized_options = b'\340A\003'
  _globals['_OBJECT'].fields_by_name['updated_at']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['updated_at']._serialized_options = b'\340A\003'
  _globals['_OBJECT'].fields_by_name['etag']._loaded_options = None
  _globals['_OBJECT'].fields_by_name['etag']._serialized_options = b'\340A\001'
  _globals['_RELATION'].fields_by_name['object_type']._loaded_options = None
  _globals['_RELATION'].fields_by_name['object_type']._serialized_options = b'\340A\002\272H\343\001r\002\030@\272\001\330\001\n\024relation.object_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_RELATION'].fields_by_name['object_id']._loaded_options = None
  _globals['_RELATION'].fields_by_name['object_id']._serialized_options = b'\340A\002\272Hsr\003\030\200\002\272\001h\n\022relation.object_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_RELATION'].fields_by_name['relation']._loaded_options = None
  _globals['_RELATION'].fields_by_name['relation']._serialized_options = b'\340A\002\272H\340\001r\002\030@\272\001\325\001\n\021relation.relation\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_RELATION'].fields_by_name['subject_type']._loaded_options = None
  _globals['_RELATION'].fields_by_name['subject_type']._serialized_options = b'\340A\002\272H\344\001r\002\030@\272\001\331\001\n\025relation.subject_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_RELATION'].fields_by_name['subject_id']._loaded_options = None
  _globals['_RELATION'].fields_by_name['subject_id']._serialized_options = b'\340A\002\272Htr\003\030\200\002\272\001i\n\023relation.subject_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_RELATION'].fields_by_name['subject_relation']._loaded_options = None
  _globals['_RELATION'].fields_by_name['subject_relation']._serialized_options = b'\340A\001\272H\350\001r\002\030@\272\001\335\001\n\031relation.subject_relation\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\320\001\001'
  _globals['_RELATION'].fields_by_name['created_at']._loaded_options = None
  _globals['_RELATION'].fields_by_name['created_at']._serialized_options = b'\340A\003'
  _globals['_RELATION'].fields_by_name['updated_at']._loaded_options = None
  _globals['_RELATION'].fields_by_name['updated_at']._serialized_options = b'\340A\003'
  _globals['_RELATION'].fields_by_name['etag']._loaded_options = None
  _globals['_RELATION'].fields_by_name['etag']._serialized_options = b'\340A\001'
  _globals['_OBJECTIDENTIFIER'].fields_by_name['object_type']._loaded_options = None
  _globals['_OBJECTIDENTIFIER'].fields_by_name['object_type']._serialized_options = b'\340A\002\272H\354\001r\002\030@\272\001\341\001\n\035object_identifier.object_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\310\001\001'
  _globals['_OBJECTIDENTIFIER'].fields_by_name['object_id']._loaded_options = None
  _globals['_OBJECTIDENTIFIER'].fields_by_name['object_id']._serialized_options = b'\340A\002\272H|r\003\030\200\002\272\001q\n\033object_identifier.object_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\310\001\001'
  _globals['_RELATIONIDENTIFIER'].fields_by_name['object_type']._loaded_options = None
  _globals['_RELATIONIDENTIFIER'].fields_by_name['object_type']._serialized_options = b'\340A\002\272H\356\001r\002\030@\272\001\343\001\n\037relation_identifier.object_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\320\001\001'
  _globals['_RELATIONIDENTIFIER'].fields_by_name['object_id']._loaded_options = None
  _globals['_RELATIONIDENTIFIER'].fields_by_name['object_id']._serialized_options = b'\340A\002\272H~r\003\030\200\002\272\001s\n\035relation_identifier.object_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\320\001\001'
  _globals['_RELATIONIDENTIFIER'].fields_by_name['relation']._loaded_options = None
  _globals['_RELATIONIDENTIFIER'].fields_by_name['relation']._serialized_options = b'\340A\002\272H\353\001r\002\030@\272\001\340\001\n\034relation_identifier.relation\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\320\001\001'
  _globals['_RELATIONIDENTIFIER'].fields_by_name['subject_type']._loaded_options = None
  _globals['_RELATIONIDENTIFIER'].fields_by_name['subject_type']._serialized_options = b'\340A\002\272H\357\001r\002\030@\272\001\344\001\n relation_identifier.subject_type\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\320\001\001'
  _globals['_RELATIONIDENTIFIER'].fields_by_name['subject_id']._loaded_options = None
  _globals['_RELATIONIDENTIFIER'].fields_by_name['subject_id']._serialized_options = b'\340A\002\272H\177r\003\030\200\002\272\001t\n\036relation_identifier.subject_id\0228cannot contain any spaces or other whitespace characters\032\030this.matches(\'^[\\\\S]+$\')\320\001\001'
  _globals['_RELATIONIDENTIFIER'].fields_by_name['subject_relation']._loaded_options = None
  _globals['_RELATIONIDENTIFIER'].fields_by_name['subject_relation']._serialized_options = b'\340A\001\272H\363\001r\002\030@\272\001\350\001\n$relation_identifier.subject_relation\022\213\001must be all lowercase, start with a letter, can contain letters, digits, dots, underscores, and dashes, and must end with a letter or digit\0322this.matches(\'^[a-z][a-z0-9\\\\._-]{1,62}[a-z0-9]$\')\320\001\001'
  _globals['_PAGINATIONREQUEST'].fields_by_name['size']._loaded_options = None
  _globals['_PAGINATIONREQUEST'].fields_by_name['size']._serialized_options = b'\340A\001\272H\006\032\004\030d(\001'
  _globals['_PAGINATIONREQUEST'].fields_by_name['token']._loaded_options = None
  _globals['_PAGINATIONREQUEST'].fields_by_name['token']._serialized_options = b'\340A\001'
  _globals['_PAGINATIONRESPONSE'].fields_by_name['next_token']._loaded_options = None
  _globals['_PAGINATIONRESPONSE'].fields_by_name['next_token']._serialized_options = b'\340A\003'
  _globals['_OBJECT']._serialized_start=197
  _globals['_OBJECT']._serialized_end=840
  _globals['_RELATION']._serialized_start=843
  _globals['_RELATION']._serialized_end=2409
  _globals['_OBJECTIDENTIFIER']._serialized_start=2412
  _globals['_OBJECTIDENTIFIER']._serialized_end=2873
  _globals['_RELATIONIDENTIFIER']._serialized_start=2876
  _globals['_RELATIONIDENTIFIER']._serialized_end=4367
  _globals['_PAGINATIONREQUEST']._serialized_start=4369
  _globals['_PAGINATIONREQUEST']._serialized_end=4449
  _globals['_PAGINATIONRESPONSE']._serialized_start=4451
  _globals['_PAGINATIONRESPONSE']._serialized_end=4507
# @@protoc_insertion_point(module_scope)
