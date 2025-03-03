# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/reader/v3/reader.proto
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
    'aserto/directory/reader/v3/reader.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from aserto.directory.common.v3 import common_pb2 as aserto_dot_directory_dot_common_dot_v3_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/reader/v3/reader.proto\x12\x1a\x61serto.directory.reader.v3\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\'aserto/directory/common/v3/common.proto\"\xce\x01\n\x10GetObjectRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12*\n\x0ewith_relations\x18\x03 \x01(\x08\x42\x03\xe0\x41\x01R\rwithRelations\x12\x46\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v3.PaginationRequestB\x03\xe0\x41\x01R\x04page\"\xd7\x01\n\x11GetObjectResponse\x12:\n\x06result\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectR\x06result\x12\x42\n\trelations\x18\x04 \x03(\x0b\x32$.aserto.directory.common.v3.RelationR\trelations\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v3.PaginationResponseR\x04page\"_\n\x14GetObjectManyRequest\x12G\n\x05param\x18\x01 \x03(\x0b\x32,.aserto.directory.common.v3.ObjectIdentifierB\x03\xe0\x41\x02R\x05param\"U\n\x15GetObjectManyResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32\".aserto.directory.common.v3.ObjectR\x07results\"\x81\x01\n\x11GetObjectsRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x01R\nobjectType\x12\x46\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v3.PaginationRequestB\x03\xe0\x41\x01R\x04page\"\x96\x01\n\x12GetObjectsResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32\".aserto.directory.common.v3.ObjectR\x07results\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v3.PaginationResponseR\x04page\"\xa1\x02\n\x12GetRelationRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12\x1f\n\x08relation\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x08relation\x12&\n\x0csubject_type\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x0bsubjectType\x12\"\n\nsubject_id\x18\x05 \x01(\tB\x03\xe0\x41\x02R\tsubjectId\x12.\n\x10subject_relation\x18\x06 \x01(\tB\x03\xe0\x41\x01R\x0fsubjectRelation\x12&\n\x0cwith_objects\x18\x07 \x01(\x08\x42\x03\xe0\x41\x01R\x0bwithObjects\"\x8b\x02\n\x13GetRelationResponse\x12<\n\x06result\x18\x01 \x01(\x0b\x32$.aserto.directory.common.v3.RelationR\x06result\x12V\n\x07objects\x18\x02 \x03(\x0b\x32<.aserto.directory.reader.v3.GetRelationResponse.ObjectsEntryR\x07objects\x1a^\n\x0cObjectsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectR\x05value:\x02\x38\x01\"\xae\x03\n\x13GetRelationsRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x01R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x01R\x08objectId\x12\x1f\n\x08relation\x18\x03 \x01(\tB\x03\xe0\x41\x01R\x08relation\x12&\n\x0csubject_type\x18\x04 \x01(\tB\x03\xe0\x41\x01R\x0bsubjectType\x12\"\n\nsubject_id\x18\x05 \x01(\tB\x03\xe0\x41\x01R\tsubjectId\x12.\n\x10subject_relation\x18\x06 \x01(\tB\x03\xe0\x41\x01R\x0fsubjectRelation\x12&\n\x0cwith_objects\x18\x07 \x01(\x08\x42\x03\xe0\x41\x01R\x0bwithObjects\x12\x42\n\x1bwith_empty_subject_relation\x18\x08 \x01(\x08\x42\x03\xe0\x41\x01R\x18withEmptySubjectRelation\x12\x46\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v3.PaginationRequestB\x03\xe0\x41\x01R\x04page\"\xd3\x02\n\x14GetRelationsResponse\x12>\n\x07results\x18\x01 \x03(\x0b\x32$.aserto.directory.common.v3.RelationR\x07results\x12W\n\x07objects\x18\x02 \x03(\x0b\x32=.aserto.directory.reader.v3.GetRelationsResponse.ObjectsEntryR\x07objects\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v3.PaginationResponseR\x04page\x1a^\n\x0cObjectsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32\".aserto.directory.common.v3.ObjectR\x05value:\x02\x38\x01\"\xde\x01\n\x0c\x43heckRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12\x1f\n\x08relation\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x08relation\x12&\n\x0csubject_type\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x0bsubjectType\x12\"\n\nsubject_id\x18\x05 \x01(\tB\x03\xe0\x41\x02R\tsubjectId\x12\x19\n\x05trace\x18\x07 \x01(\x08\x42\x03\xe0\x41\x01R\x05trace\"n\n\rCheckResponse\x12\x14\n\x05\x63heck\x18\x01 \x01(\x08R\x05\x63heck\x12\x14\n\x05trace\x18\x02 \x03(\tR\x05trace\x12\x31\n\x07\x63ontext\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructR\x07\x63ontext\"\x95\x01\n\rChecksRequest\x12\x42\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x0b\x32(.aserto.directory.reader.v3.CheckRequestR\x07\x64\x65\x66\x61ult\x12@\n\x06\x63hecks\x18\x02 \x03(\x0b\x32(.aserto.directory.reader.v3.CheckRequestR\x06\x63hecks\"S\n\x0e\x43hecksResponse\x12\x41\n\x06\x63hecks\x18\x01 \x03(\x0b\x32).aserto.directory.reader.v3.CheckResponseR\x06\x63hecks\"\xec\x01\n\x16\x43heckPermissionRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12#\n\npermission\x18\x03 \x01(\tB\x03\xe0\x41\x02R\npermission\x12&\n\x0csubject_type\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x0bsubjectType\x12\"\n\nsubject_id\x18\x05 \x01(\tB\x03\xe0\x41\x02R\tsubjectId\x12\x19\n\x05trace\x18\x07 \x01(\x08\x42\x03\xe0\x41\x01R\x05trace\"E\n\x17\x43heckPermissionResponse\x12\x14\n\x05\x63heck\x18\x01 \x01(\x08R\x05\x63heck\x12\x14\n\x05trace\x18\x02 \x03(\tR\x05trace\"\xe6\x01\n\x14\x43heckRelationRequest\x12$\n\x0bobject_type\x18\x01 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08objectId\x12\x1f\n\x08relation\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x08relation\x12&\n\x0csubject_type\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x0bsubjectType\x12\"\n\nsubject_id\x18\x05 \x01(\tB\x03\xe0\x41\x02R\tsubjectId\x12\x19\n\x05trace\x18\x07 \x01(\x08\x42\x03\xe0\x41\x01R\x05trace\"C\n\x15\x43heckRelationResponse\x12\x14\n\x05\x63heck\x18\x01 \x01(\x08R\x05\x63heck\x12\x14\n\x05trace\x18\x02 \x03(\tR\x05trace\"\xd4\x02\n\x0fGetGraphRequest\x12$\n\x0bobject_type\x18\x03 \x01(\tB\x03\xe0\x41\x02R\nobjectType\x12 \n\tobject_id\x18\x04 \x01(\tB\x03\xe0\x41\x01R\x08objectId\x12\x1f\n\x08relation\x18\x05 \x01(\tB\x03\xe0\x41\x02R\x08relation\x12&\n\x0csubject_type\x18\x06 \x01(\tB\x03\xe0\x41\x02R\x0bsubjectType\x12\"\n\nsubject_id\x18\x07 \x01(\tB\x03\xe0\x41\x01R\tsubjectId\x12.\n\x10subject_relation\x18\x08 \x01(\tB\x03\xe0\x41\x01R\x0fsubjectRelation\x12\x1d\n\x07\x65xplain\x18\t \x01(\x08\x42\x03\xe0\x41\x01R\x07\x65xplain\x12\x19\n\x05trace\x18\n \x01(\x08\x42\x03\xe0\x41\x01R\x05traceJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\x0b\x61nchor_typeR\tanchor_id\"\xb1\x01\n\x10GetGraphResponse\x12\x46\n\x07results\x18\x02 \x03(\x0b\x32,.aserto.directory.common.v3.ObjectIdentifierR\x07results\x12\x39\n\x0b\x65xplanation\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructR\x0b\x65xplanation\x12\x14\n\x05trace\x18\x04 \x03(\tR\x05traceJ\x04\x08\x01\x10\x02\x32\xc5\x16\n\x06Reader\x12\xe9\x02\n\tGetObject\x12,.aserto.directory.reader.v3.GetObjectRequest\x1a-.aserto.directory.reader.v3.GetObjectResponse\"\xfe\x01\x92\x41\xc0\x01\n\tdirectory\x12\x13Get object instance\x1a:Returns single object instance, optionally with relations.*\x1e\x64irectory.reader.v3.object.getJ\x1d\n\x03\x33\x30\x34\x12\x16\n\x14Object not modified.b#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x34\x12\x32/api/v3/directory/object/{object_type}/{object_id}\x12v\n\rGetObjectMany\x12\x30.aserto.directory.reader.v3.GetObjectManyRequest\x1a\x31.aserto.directory.reader.v3.GetObjectManyResponse\"\x00\x12\x9f\x02\n\nGetObjects\x12-.aserto.directory.reader.v3.GetObjectsRequest\x1a..aserto.directory.reader.v3.GetObjectsResponse\"\xb1\x01\x92\x41\x8c\x01\n\tdirectory\x12\x15List object instances\x1a!Returns list of object instances.* directory.reader.v3.objects.listb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1b\x12\x19/api/v3/directory/objects\x12\xdd\x02\n\x0bGetRelation\x12..aserto.directory.reader.v3.GetRelationRequest\x1a/.aserto.directory.reader.v3.GetRelationResponse\"\xec\x01\x92\x41\xc6\x01\n\tdirectory\x12\x15Get relation instance\x1a:Returns single relation instance, optionally with objects.* directory.reader.v3.relation.getJ\x1f\n\x03\x33\x30\x34\x12\x18\n\x16Relation not modified.b#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/v3/directory/relation\x12\xae\x02\n\x0cGetRelations\x12/.aserto.directory.reader.v3.GetRelationsRequest\x1a\x30.aserto.directory.reader.v3.GetRelationsResponse\"\xba\x01\x92\x41\x93\x01\n\tdirectory\x12\x18List relations instances\x1a#Returns list of relation instances.*\"directory.reader.v3.relations.listb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/v3/directory/relations\x12\xee\x01\n\x05\x43heck\x12(.aserto.directory.reader.v3.CheckRequest\x1a).aserto.directory.reader.v3.CheckResponse\"\x8f\x01\x92\x41j\n\tdirectory\x12\x05\x43heck\x1a\x16Returns check outcome.*\x19\x64irectory.reader.v3.checkb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1c\"\x17/api/v3/directory/check:\x01*\x12\xfe\x01\n\x06\x43hecks\x12).aserto.directory.reader.v3.ChecksRequest\x1a*.aserto.directory.reader.v3.ChecksResponse\"\x9c\x01\x92\x41v\n\tdirectory\x12\x06\x43hecks\x1a Returns multiple check outcomes.*\x1a\x64irectory.reader.v3.checksb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1d\"\x18/api/v3/directory/checks:\x01*\x12\xbc\x02\n\x0f\x43heckPermission\x12\x32.aserto.directory.reader.v3.CheckPermissionRequest\x1a\x33.aserto.directory.reader.v3.CheckPermissionResponse\"\xbf\x01\x88\x02\x01\x92\x41\x8b\x01\n\tdirectory\x12\x10\x43heck permission\x1a!Returns check permission outcome.*$directory.reader.v3.check.permissionb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\'\"\"/api/v3/directory/check/permission:\x01*\x12\xae\x02\n\rCheckRelation\x12\x30.aserto.directory.reader.v3.CheckRelationRequest\x1a\x31.aserto.directory.reader.v3.CheckRelationResponse\"\xb7\x01\x88\x02\x01\x92\x41\x85\x01\n\tdirectory\x12\x0e\x43heck relation\x1a\x1fReturns check relation outcome.*\"directory.reader.v3.check.relationb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02%\" /api/v3/directory/check/relation:\x01*\x12\xc1\x02\n\x08GetGraph\x12+.aserto.directory.reader.v3.GetGraphRequest\x1a,.aserto.directory.reader.v3.GetGraphResponse\"\xd9\x01\x92\x41\x8e\x01\n\tdirectory\x12\tGet graph\x1a\x36Returns object graph from anchor to subject or object.*\x19\x64irectory.reader.v3.graphb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x41\x12?/api/v3/directory/graph/{object_type}/{relation}/{subject_type}B\x80\x02\n\x1e\x63om.aserto.directory.reader.v3B\x0bReaderProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/reader/v3;reader\xa2\x02\x03\x41\x44R\xaa\x02\x1a\x41serto.Directory.Reader.V3\xca\x02\x1b\x41serto\\Directory_\\Reader\\V3\xe2\x02\'Aserto\\Directory_\\Reader\\V3\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Reader::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.reader.v3.reader_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.reader.v3B\013ReaderProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/reader/v3;reader\242\002\003ADR\252\002\032Aserto.Directory.Reader.V3\312\002\033Aserto\\Directory_\\Reader\\V3\342\002\'Aserto\\Directory_\\Reader\\V3\\GPBMetadata\352\002\035Aserto::Directory::Reader::V3'
  _globals['_GETOBJECTREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_GETOBJECTREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_GETOBJECTREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_GETOBJECTREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_GETOBJECTREQUEST'].fields_by_name['with_relations']._loaded_options = None
  _globals['_GETOBJECTREQUEST'].fields_by_name['with_relations']._serialized_options = b'\340A\001'
  _globals['_GETOBJECTREQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_GETOBJECTREQUEST'].fields_by_name['page']._serialized_options = b'\340A\001'
  _globals['_GETOBJECTMANYREQUEST'].fields_by_name['param']._loaded_options = None
  _globals['_GETOBJECTMANYREQUEST'].fields_by_name['param']._serialized_options = b'\340A\002'
  _globals['_GETOBJECTSREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_GETOBJECTSREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\001'
  _globals['_GETOBJECTSREQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_GETOBJECTSREQUEST'].fields_by_name['page']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_GETRELATIONREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_GETRELATIONREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\002'
  _globals['_GETRELATIONREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\002'
  _globals['_GETRELATIONREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\002'
  _globals['_GETRELATIONREQUEST'].fields_by_name['subject_relation']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['subject_relation']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONREQUEST'].fields_by_name['with_objects']._loaded_options = None
  _globals['_GETRELATIONREQUEST'].fields_by_name['with_objects']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._loaded_options = None
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._serialized_options = b'8\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['subject_relation']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['subject_relation']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['with_objects']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['with_objects']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['with_empty_subject_relation']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['with_empty_subject_relation']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSREQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_GETRELATIONSREQUEST'].fields_by_name['page']._serialized_options = b'\340A\001'
  _globals['_GETRELATIONSRESPONSE_OBJECTSENTRY']._loaded_options = None
  _globals['_GETRELATIONSRESPONSE_OBJECTSENTRY']._serialized_options = b'8\001'
  _globals['_CHECKREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_CHECKREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_CHECKREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_CHECKREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_CHECKREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_CHECKREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\002'
  _globals['_CHECKREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_CHECKREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\002'
  _globals['_CHECKREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_CHECKREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\002'
  _globals['_CHECKREQUEST'].fields_by_name['trace']._loaded_options = None
  _globals['_CHECKREQUEST'].fields_by_name['trace']._serialized_options = b'\340A\001'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['permission']._serialized_options = b'\340A\002'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\002'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\002'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['trace']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['trace']._serialized_options = b'\340A\001'
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\002'
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\002'
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\002'
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\002'
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['trace']._loaded_options = None
  _globals['_CHECKRELATIONREQUEST'].fields_by_name['trace']._serialized_options = b'\340A\001'
  _globals['_GETGRAPHREQUEST'].fields_by_name['object_type']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['object_type']._serialized_options = b'\340A\002'
  _globals['_GETGRAPHREQUEST'].fields_by_name['object_id']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['object_id']._serialized_options = b'\340A\001'
  _globals['_GETGRAPHREQUEST'].fields_by_name['relation']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['relation']._serialized_options = b'\340A\002'
  _globals['_GETGRAPHREQUEST'].fields_by_name['subject_type']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['subject_type']._serialized_options = b'\340A\002'
  _globals['_GETGRAPHREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['subject_id']._serialized_options = b'\340A\001'
  _globals['_GETGRAPHREQUEST'].fields_by_name['subject_relation']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['subject_relation']._serialized_options = b'\340A\001'
  _globals['_GETGRAPHREQUEST'].fields_by_name['explain']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['explain']._serialized_options = b'\340A\001'
  _globals['_GETGRAPHREQUEST'].fields_by_name['trace']._loaded_options = None
  _globals['_GETGRAPHREQUEST'].fields_by_name['trace']._serialized_options = b'\340A\001'
  _globals['_READER'].methods_by_name['GetObject']._loaded_options = None
  _globals['_READER'].methods_by_name['GetObject']._serialized_options = b'\222A\300\001\n\tdirectory\022\023Get object instance\032:Returns single object instance, optionally with relations.*\036directory.reader.v3.object.getJ\035\n\003304\022\026\n\024Object not modified.b#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\0024\0222/api/v3/directory/object/{object_type}/{object_id}'
  _globals['_READER'].methods_by_name['GetObjects']._loaded_options = None
  _globals['_READER'].methods_by_name['GetObjects']._serialized_options = b'\222A\214\001\n\tdirectory\022\025List object instances\032!Returns list of object instances.* directory.reader.v3.objects.listb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\033\022\031/api/v3/directory/objects'
  _globals['_READER'].methods_by_name['GetRelation']._loaded_options = None
  _globals['_READER'].methods_by_name['GetRelation']._serialized_options = b'\222A\306\001\n\tdirectory\022\025Get relation instance\032:Returns single relation instance, optionally with objects.* directory.reader.v3.relation.getJ\037\n\003304\022\030\n\026Relation not modified.b#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\034\022\032/api/v3/directory/relation'
  _globals['_READER'].methods_by_name['GetRelations']._loaded_options = None
  _globals['_READER'].methods_by_name['GetRelations']._serialized_options = b'\222A\223\001\n\tdirectory\022\030List relations instances\032#Returns list of relation instances.*\"directory.reader.v3.relations.listb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\035\022\033/api/v3/directory/relations'
  _globals['_READER'].methods_by_name['Check']._loaded_options = None
  _globals['_READER'].methods_by_name['Check']._serialized_options = b'\222Aj\n\tdirectory\022\005Check\032\026Returns check outcome.*\031directory.reader.v3.checkb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\034\"\027/api/v3/directory/check:\001*'
  _globals['_READER'].methods_by_name['Checks']._loaded_options = None
  _globals['_READER'].methods_by_name['Checks']._serialized_options = b'\222Av\n\tdirectory\022\006Checks\032 Returns multiple check outcomes.*\032directory.reader.v3.checksb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\035\"\030/api/v3/directory/checks:\001*'
  _globals['_READER'].methods_by_name['CheckPermission']._loaded_options = None
  _globals['_READER'].methods_by_name['CheckPermission']._serialized_options = b'\210\002\001\222A\213\001\n\tdirectory\022\020Check permission\032!Returns check permission outcome.*$directory.reader.v3.check.permissionb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\'\"\"/api/v3/directory/check/permission:\001*'
  _globals['_READER'].methods_by_name['CheckRelation']._loaded_options = None
  _globals['_READER'].methods_by_name['CheckRelation']._serialized_options = b'\210\002\001\222A\205\001\n\tdirectory\022\016Check relation\032\037Returns check relation outcome.*\"directory.reader.v3.check.relationb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002%\" /api/v3/directory/check/relation:\001*'
  _globals['_READER'].methods_by_name['GetGraph']._loaded_options = None
  _globals['_READER'].methods_by_name['GetGraph']._serialized_options = b'\222A\216\001\n\tdirectory\022\tGet graph\0326Returns object graph from anchor to subject or object.*\031directory.reader.v3.graphb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002A\022?/api/v3/directory/graph/{object_type}/{relation}/{subject_type}'
  _globals['_GETOBJECTREQUEST']._serialized_start=254
  _globals['_GETOBJECTREQUEST']._serialized_end=460
  _globals['_GETOBJECTRESPONSE']._serialized_start=463
  _globals['_GETOBJECTRESPONSE']._serialized_end=678
  _globals['_GETOBJECTMANYREQUEST']._serialized_start=680
  _globals['_GETOBJECTMANYREQUEST']._serialized_end=775
  _globals['_GETOBJECTMANYRESPONSE']._serialized_start=777
  _globals['_GETOBJECTMANYRESPONSE']._serialized_end=862
  _globals['_GETOBJECTSREQUEST']._serialized_start=865
  _globals['_GETOBJECTSREQUEST']._serialized_end=994
  _globals['_GETOBJECTSRESPONSE']._serialized_start=997
  _globals['_GETOBJECTSRESPONSE']._serialized_end=1147
  _globals['_GETRELATIONREQUEST']._serialized_start=1150
  _globals['_GETRELATIONREQUEST']._serialized_end=1439
  _globals['_GETRELATIONRESPONSE']._serialized_start=1442
  _globals['_GETRELATIONRESPONSE']._serialized_end=1709
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._serialized_start=1615
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._serialized_end=1709
  _globals['_GETRELATIONSREQUEST']._serialized_start=1712
  _globals['_GETRELATIONSREQUEST']._serialized_end=2142
  _globals['_GETRELATIONSRESPONSE']._serialized_start=2145
  _globals['_GETRELATIONSRESPONSE']._serialized_end=2484
  _globals['_GETRELATIONSRESPONSE_OBJECTSENTRY']._serialized_start=1615
  _globals['_GETRELATIONSRESPONSE_OBJECTSENTRY']._serialized_end=1709
  _globals['_CHECKREQUEST']._serialized_start=2487
  _globals['_CHECKREQUEST']._serialized_end=2709
  _globals['_CHECKRESPONSE']._serialized_start=2711
  _globals['_CHECKRESPONSE']._serialized_end=2821
  _globals['_CHECKSREQUEST']._serialized_start=2824
  _globals['_CHECKSREQUEST']._serialized_end=2973
  _globals['_CHECKSRESPONSE']._serialized_start=2975
  _globals['_CHECKSRESPONSE']._serialized_end=3058
  _globals['_CHECKPERMISSIONREQUEST']._serialized_start=3061
  _globals['_CHECKPERMISSIONREQUEST']._serialized_end=3297
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_start=3299
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_end=3368
  _globals['_CHECKRELATIONREQUEST']._serialized_start=3371
  _globals['_CHECKRELATIONREQUEST']._serialized_end=3601
  _globals['_CHECKRELATIONRESPONSE']._serialized_start=3603
  _globals['_CHECKRELATIONRESPONSE']._serialized_end=3670
  _globals['_GETGRAPHREQUEST']._serialized_start=3673
  _globals['_GETGRAPHREQUEST']._serialized_end=4013
  _globals['_GETGRAPHRESPONSE']._serialized_start=4016
  _globals['_GETGRAPHRESPONSE']._serialized_end=4193
  _globals['_READER']._serialized_start=4196
  _globals['_READER']._serialized_end=7081
# @@protoc_insertion_point(module_scope)
