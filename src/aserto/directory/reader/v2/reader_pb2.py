# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/reader/v2/reader.proto
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
    'aserto/directory/reader/v2/reader.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aserto.directory.common.v2 import common_pb2 as aserto_dot_directory_dot_common_dot_v2_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/reader/v2/reader.proto\x12\x1a\x61serto.directory.reader.v2\x1a\'aserto/directory/common/v2/common.proto\"^\n\x14GetObjectTypeRequest\x12\x46\n\x05param\x18\x01 \x01(\x0b\x32\x30.aserto.directory.common.v2.ObjectTypeIdentifierR\x05param\"W\n\x15GetObjectTypeResponse\x12>\n\x06result\x18\x01 \x01(\x0b\x32&.aserto.directory.common.v2.ObjectTypeR\x06result\"Z\n\x15GetObjectTypesRequest\x12\x41\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v2.PaginationRequestR\x04page\"\x9e\x01\n\x16GetObjectTypesResponse\x12@\n\x07results\x18\x01 \x03(\x0b\x32&.aserto.directory.common.v2.ObjectTypeR\x07results\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v2.PaginationResponseR\x04page\"b\n\x16GetRelationTypeRequest\x12H\n\x05param\x18\x01 \x01(\x0b\x32\x32.aserto.directory.common.v2.RelationTypeIdentifierR\x05param\"[\n\x17GetRelationTypeResponse\x12@\n\x06result\x18\x01 \x01(\x0b\x32(.aserto.directory.common.v2.RelationTypeR\x06result\"\xa4\x01\n\x17GetRelationTypesRequest\x12\x46\n\x05param\x18\x01 \x01(\x0b\x32\x30.aserto.directory.common.v2.ObjectTypeIdentifierR\x05param\x12\x41\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v2.PaginationRequestR\x04page\"\xa2\x01\n\x18GetRelationTypesResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32(.aserto.directory.common.v2.RelationTypeR\x07results\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v2.PaginationResponseR\x04page\"\xd8\x01\n\x10GetObjectRequest\x12\x42\n\x05param\x18\x01 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x05param\x12*\n\x0ewith_relations\x18\x02 \x01(\x08H\x00R\rwithRelations\x88\x01\x01\x12\x41\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v2.PaginationRequestR\x04pageB\x11\n\x0f_with_relations\"\xf7\x01\n\x11GetObjectResponse\x12:\n\x06result\x18\x01 \x01(\x0b\x32\".aserto.directory.common.v2.ObjectR\x06result\x12\x42\n\trelations\x18\x04 \x03(\x0b\x32$.aserto.directory.common.v2.RelationR\trelations\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v2.PaginationResponseR\x04pageJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04R\x08incomingR\x08outgoing\"Z\n\x14GetObjectManyRequest\x12\x42\n\x05param\x18\x01 \x03(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x05param\"U\n\x15GetObjectManyResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32\".aserto.directory.common.v2.ObjectR\x07results\"\x9e\x01\n\x11GetObjectsRequest\x12\x46\n\x05param\x18\x01 \x01(\x0b\x32\x30.aserto.directory.common.v2.ObjectTypeIdentifierR\x05param\x12\x41\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v2.PaginationRequestR\x04page\"\x96\x01\n\x12GetObjectsResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32\".aserto.directory.common.v2.ObjectR\x07results\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v2.PaginationResponseR\x04page\"\x93\x01\n\x12GetRelationRequest\x12\x44\n\x05param\x18\x01 \x01(\x0b\x32..aserto.directory.common.v2.RelationIdentifierR\x05param\x12&\n\x0cwith_objects\x18\x02 \x01(\x08H\x00R\x0bwithObjects\x88\x01\x01\x42\x0f\n\r_with_objects\"\x8d\x02\n\x13GetRelationResponse\x12>\n\x07results\x18\x01 \x03(\x0b\x32$.aserto.directory.common.v2.RelationR\x07results\x12V\n\x07objects\x18\x02 \x03(\x0b\x32<.aserto.directory.reader.v2.GetRelationResponse.ObjectsEntryR\x07objects\x1a^\n\x0cObjectsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32\".aserto.directory.common.v2.ObjectR\x05value:\x02\x38\x01\"\x9e\x01\n\x13GetRelationsRequest\x12\x44\n\x05param\x18\x01 \x01(\x0b\x32..aserto.directory.common.v2.RelationIdentifierR\x05param\x12\x41\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v2.PaginationRequestR\x04page\"\x9a\x01\n\x14GetRelationsResponse\x12>\n\x07results\x18\x01 \x03(\x0b\x32$.aserto.directory.common.v2.RelationR\x07results\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v2.PaginationResponseR\x04page\"^\n\x14GetPermissionRequest\x12\x46\n\x05param\x18\x01 \x01(\x0b\x32\x30.aserto.directory.common.v2.PermissionIdentifierR\x05param\"W\n\x15GetPermissionResponse\x12>\n\x06result\x18\x01 \x01(\x0b\x32&.aserto.directory.common.v2.PermissionR\x06result\"Z\n\x15GetPermissionsRequest\x12\x41\n\x04page\x18\t \x01(\x0b\x32-.aserto.directory.common.v2.PaginationRequestR\x04page\"\x9e\x01\n\x16GetPermissionsResponse\x12@\n\x07results\x18\x01 \x03(\x0b\x32&.aserto.directory.common.v2.PermissionR\x07results\x12\x42\n\x04page\x18\t \x01(\x0b\x32..aserto.directory.common.v2.PaginationResponseR\x04page\"\x8e\x02\n\x16\x43heckPermissionRequest\x12\x46\n\x07subject\x18\x01 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x07subject\x12P\n\npermission\x18\x02 \x01(\x0b\x32\x30.aserto.directory.common.v2.PermissionIdentifierR\npermission\x12\x44\n\x06object\x18\x03 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x06object\x12\x14\n\x05trace\x18\x07 \x01(\x08R\x05trace\"E\n\x17\x43heckPermissionResponse\x12\x14\n\x05\x63heck\x18\x01 \x01(\x08R\x05\x63heck\x12\x14\n\x05trace\x18\x02 \x03(\tR\x05trace\"\x8a\x02\n\x14\x43heckRelationRequest\x12\x46\n\x07subject\x18\x01 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x07subject\x12N\n\x08relation\x18\x02 \x01(\x0b\x32\x32.aserto.directory.common.v2.RelationTypeIdentifierR\x08relation\x12\x44\n\x06object\x18\x03 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x06object\x12\x14\n\x05trace\x18\x07 \x01(\x08R\x05trace\"C\n\x15\x43heckRelationResponse\x12\x14\n\x05\x63heck\x18\x01 \x01(\x08R\x05\x63heck\x12\x14\n\x05trace\x18\x02 \x03(\tR\x05trace\";\n\rCheckResponse\x12\x14\n\x05\x63heck\x18\x01 \x01(\x08R\x05\x63heck\x12\x14\n\x05trace\x18\x02 \x03(\tR\x05trace\"\xb5\x02\n\x0fGetGraphRequest\x12\x44\n\x06\x61nchor\x18\x01 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x06\x61nchor\x12\x46\n\x07subject\x18\x02 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x07subject\x12N\n\x08relation\x18\x03 \x01(\x0b\x32\x32.aserto.directory.common.v2.RelationTypeIdentifierR\x08relation\x12\x44\n\x06object\x18\x04 \x01(\x0b\x32,.aserto.directory.common.v2.ObjectIdentifierR\x06object\"Z\n\x10GetGraphResponse\x12\x46\n\x07results\x18\x01 \x03(\x0b\x32,.aserto.directory.common.v2.ObjectDependencyR\x07results2\x86\r\n\x06Reader\x12v\n\rGetObjectType\x12\x30.aserto.directory.reader.v2.GetObjectTypeRequest\x1a\x31.aserto.directory.reader.v2.GetObjectTypeResponse\"\x00\x12y\n\x0eGetObjectTypes\x12\x31.aserto.directory.reader.v2.GetObjectTypesRequest\x1a\x32.aserto.directory.reader.v2.GetObjectTypesResponse\"\x00\x12|\n\x0fGetRelationType\x12\x32.aserto.directory.reader.v2.GetRelationTypeRequest\x1a\x33.aserto.directory.reader.v2.GetRelationTypeResponse\"\x00\x12\x7f\n\x10GetRelationTypes\x12\x33.aserto.directory.reader.v2.GetRelationTypesRequest\x1a\x34.aserto.directory.reader.v2.GetRelationTypesResponse\"\x00\x12v\n\rGetPermission\x12\x30.aserto.directory.reader.v2.GetPermissionRequest\x1a\x31.aserto.directory.reader.v2.GetPermissionResponse\"\x00\x12y\n\x0eGetPermissions\x12\x31.aserto.directory.reader.v2.GetPermissionsRequest\x1a\x32.aserto.directory.reader.v2.GetPermissionsResponse\"\x00\x12j\n\tGetObject\x12,.aserto.directory.reader.v2.GetObjectRequest\x1a-.aserto.directory.reader.v2.GetObjectResponse\"\x00\x12v\n\rGetObjectMany\x12\x30.aserto.directory.reader.v2.GetObjectManyRequest\x1a\x31.aserto.directory.reader.v2.GetObjectManyResponse\"\x00\x12m\n\nGetObjects\x12-.aserto.directory.reader.v2.GetObjectsRequest\x1a..aserto.directory.reader.v2.GetObjectsResponse\"\x00\x12p\n\x0bGetRelation\x12..aserto.directory.reader.v2.GetRelationRequest\x1a/.aserto.directory.reader.v2.GetRelationResponse\"\x00\x12s\n\x0cGetRelations\x12/.aserto.directory.reader.v2.GetRelationsRequest\x1a\x30.aserto.directory.reader.v2.GetRelationsResponse\"\x00\x12|\n\x0f\x43heckPermission\x12\x32.aserto.directory.reader.v2.CheckPermissionRequest\x1a\x33.aserto.directory.reader.v2.CheckPermissionResponse\"\x00\x12v\n\rCheckRelation\x12\x30.aserto.directory.reader.v2.CheckRelationRequest\x1a\x31.aserto.directory.reader.v2.CheckRelationResponse\"\x00\x12g\n\x08GetGraph\x12+.aserto.directory.reader.v2.GetGraphRequest\x1a,.aserto.directory.reader.v2.GetGraphResponse\"\x00\x42\x80\x02\n\x1e\x63om.aserto.directory.reader.v2B\x0bReaderProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/reader/v2;reader\xa2\x02\x03\x41\x44R\xaa\x02\x1a\x41serto.Directory.Reader.V2\xca\x02\x1b\x41serto\\Directory_\\Reader\\V2\xe2\x02\'Aserto\\Directory_\\Reader\\V2\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Reader::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.reader.v2.reader_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.reader.v2B\013ReaderProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/reader/v2;reader\242\002\003ADR\252\002\032Aserto.Directory.Reader.V2\312\002\033Aserto\\Directory_\\Reader\\V2\342\002\'Aserto\\Directory_\\Reader\\V2\\GPBMetadata\352\002\035Aserto::Directory::Reader::V2'
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._loaded_options = None
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._serialized_options = b'8\001'
  _globals['_GETOBJECTTYPEREQUEST']._serialized_start=112
  _globals['_GETOBJECTTYPEREQUEST']._serialized_end=206
  _globals['_GETOBJECTTYPERESPONSE']._serialized_start=208
  _globals['_GETOBJECTTYPERESPONSE']._serialized_end=295
  _globals['_GETOBJECTTYPESREQUEST']._serialized_start=297
  _globals['_GETOBJECTTYPESREQUEST']._serialized_end=387
  _globals['_GETOBJECTTYPESRESPONSE']._serialized_start=390
  _globals['_GETOBJECTTYPESRESPONSE']._serialized_end=548
  _globals['_GETRELATIONTYPEREQUEST']._serialized_start=550
  _globals['_GETRELATIONTYPEREQUEST']._serialized_end=648
  _globals['_GETRELATIONTYPERESPONSE']._serialized_start=650
  _globals['_GETRELATIONTYPERESPONSE']._serialized_end=741
  _globals['_GETRELATIONTYPESREQUEST']._serialized_start=744
  _globals['_GETRELATIONTYPESREQUEST']._serialized_end=908
  _globals['_GETRELATIONTYPESRESPONSE']._serialized_start=911
  _globals['_GETRELATIONTYPESRESPONSE']._serialized_end=1073
  _globals['_GETOBJECTREQUEST']._serialized_start=1076
  _globals['_GETOBJECTREQUEST']._serialized_end=1292
  _globals['_GETOBJECTRESPONSE']._serialized_start=1295
  _globals['_GETOBJECTRESPONSE']._serialized_end=1542
  _globals['_GETOBJECTMANYREQUEST']._serialized_start=1544
  _globals['_GETOBJECTMANYREQUEST']._serialized_end=1634
  _globals['_GETOBJECTMANYRESPONSE']._serialized_start=1636
  _globals['_GETOBJECTMANYRESPONSE']._serialized_end=1721
  _globals['_GETOBJECTSREQUEST']._serialized_start=1724
  _globals['_GETOBJECTSREQUEST']._serialized_end=1882
  _globals['_GETOBJECTSRESPONSE']._serialized_start=1885
  _globals['_GETOBJECTSRESPONSE']._serialized_end=2035
  _globals['_GETRELATIONREQUEST']._serialized_start=2038
  _globals['_GETRELATIONREQUEST']._serialized_end=2185
  _globals['_GETRELATIONRESPONSE']._serialized_start=2188
  _globals['_GETRELATIONRESPONSE']._serialized_end=2457
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._serialized_start=2363
  _globals['_GETRELATIONRESPONSE_OBJECTSENTRY']._serialized_end=2457
  _globals['_GETRELATIONSREQUEST']._serialized_start=2460
  _globals['_GETRELATIONSREQUEST']._serialized_end=2618
  _globals['_GETRELATIONSRESPONSE']._serialized_start=2621
  _globals['_GETRELATIONSRESPONSE']._serialized_end=2775
  _globals['_GETPERMISSIONREQUEST']._serialized_start=2777
  _globals['_GETPERMISSIONREQUEST']._serialized_end=2871
  _globals['_GETPERMISSIONRESPONSE']._serialized_start=2873
  _globals['_GETPERMISSIONRESPONSE']._serialized_end=2960
  _globals['_GETPERMISSIONSREQUEST']._serialized_start=2962
  _globals['_GETPERMISSIONSREQUEST']._serialized_end=3052
  _globals['_GETPERMISSIONSRESPONSE']._serialized_start=3055
  _globals['_GETPERMISSIONSRESPONSE']._serialized_end=3213
  _globals['_CHECKPERMISSIONREQUEST']._serialized_start=3216
  _globals['_CHECKPERMISSIONREQUEST']._serialized_end=3486
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_start=3488
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_end=3557
  _globals['_CHECKRELATIONREQUEST']._serialized_start=3560
  _globals['_CHECKRELATIONREQUEST']._serialized_end=3826
  _globals['_CHECKRELATIONRESPONSE']._serialized_start=3828
  _globals['_CHECKRELATIONRESPONSE']._serialized_end=3895
  _globals['_CHECKRESPONSE']._serialized_start=3897
  _globals['_CHECKRESPONSE']._serialized_end=3956
  _globals['_GETGRAPHREQUEST']._serialized_start=3959
  _globals['_GETGRAPHREQUEST']._serialized_end=4268
  _globals['_GETGRAPHRESPONSE']._serialized_start=4270
  _globals['_GETGRAPHRESPONSE']._serialized_end=4360
  _globals['_READER']._serialized_start=4363
  _globals['_READER']._serialized_end=6033
# @@protoc_insertion_point(module_scope)
