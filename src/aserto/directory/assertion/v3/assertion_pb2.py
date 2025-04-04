# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/assertion/v3/assertion.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'aserto/directory/assertion/v3/assertion.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aserto.directory.common.v3 import common_pb2 as aserto_dot_directory_dot_common_dot_v3_dot_common__pb2
from aserto.directory.reader.v3 import reader_pb2 as aserto_dot_directory_dot_reader_dot_v3_dot_reader__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-aserto/directory/assertion/v3/assertion.proto\x12\x1d\x61serto.directory.assertion.v3\x1a\'aserto/directory/common/v3/common.proto\x1a\'aserto/directory/reader/v3/reader.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"*\n\x13GetAssertionRequest\x12\x13\n\x02id\x18\x01 \x01(\rB\x03\xe0\x41\x02R\x02id\"U\n\x14GetAssertionResponse\x12=\n\x06result\x18\x01 \x01(\x0b\x32%.aserto.directory.assertion.v3.AssertR\x06result\"_\n\x15ListAssertionsRequest\x12\x46\n\x04page\x18\x01 \x01(\x0b\x32-.aserto.directory.common.v3.PaginationRequestB\x03\xe0\x41\x01R\x04page\"\x9d\x01\n\x16ListAssertionsResponse\x12?\n\x07results\x18\x01 \x03(\x0b\x32%.aserto.directory.assertion.v3.AssertR\x07results\x12\x42\n\x04page\x18\x02 \x01(\x0b\x32..aserto.directory.common.v3.PaginationResponseR\x04page\"Y\n\x13SetAssertionRequest\x12\x42\n\x06\x61ssert\x18\x01 \x01(\x0b\x32%.aserto.directory.assertion.v3.AssertB\x03\xe0\x41\x02R\x06\x61ssert\"U\n\x14SetAssertionResponse\x12=\n\x06result\x18\x01 \x01(\x0b\x32%.aserto.directory.assertion.v3.AssertR\x06result\"-\n\x16\x44\x65leteAssertionRequest\x12\x13\n\x02id\x18\x01 \x01(\rB\x03\xe0\x41\x02R\x02id\"I\n\x17\x44\x65leteAssertionResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"\xe0\x02\n\x06\x41ssert\x12\x0e\n\x02id\x18\x01 \x01(\rR\x02id\x12\x1f\n\x08\x65xpected\x18\x02 \x01(\x08\x42\x03\xe0\x41\x02R\x08\x65xpected\x12@\n\x05\x63heck\x18\x03 \x01(\x0b\x32(.aserto.directory.reader.v3.CheckRequestH\x00R\x05\x63heck\x12Y\n\x0e\x63heck_relation\x18\x04 \x01(\x0b\x32\x30.aserto.directory.reader.v3.CheckRelationRequestH\x00R\rcheckRelation\x12_\n\x10\x63heck_permission\x18\x05 \x01(\x0b\x32\x32.aserto.directory.reader.v3.CheckPermissionRequestH\x00R\x0f\x63heckPermission\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scriptionB\x05\n\x03msg2\xca\t\n\tAssertion\x12\xb8\x02\n\x0cGetAssertion\x12\x32.aserto.directory.assertion.v3.GetAssertionRequest\x1a\x33.aserto.directory.assertion.v3.GetAssertionResponse\"\xbe\x01\x92\x41\x92\x01\n\tdirectory\x12\x16Get assertion instance\x1a\"Returns single assertion instance.*$directory.assertion.v3.assertion.getb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\"\x12 /api/v3/directory/assertion/{id}\x12\xb7\x02\n\x0eListAssertions\x12\x34.aserto.directory.assertion.v3.ListAssertionsRequest\x1a\x35.aserto.directory.assertion.v3.ListAssertionsResponse\"\xb7\x01\x92\x41\x8f\x01\n\tdirectory\x12\x0fList assertions\x1a$Returns list of assertion instances.*&directory.assertion.v3.assertions.listb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/v3/directory/assertions\x12\x98\x02\n\x0cSetAssertion\x12\x32.aserto.directory.assertion.v3.SetAssertionRequest\x1a\x33.aserto.directory.assertion.v3.SetAssertionResponse\"\x9e\x01\x92\x41u\n\tdirectory\x12\rSet assertion\x1a\x0eSet assertion.*$directory.assertion.v3.assertion.setb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02 \"\x1b/api/v3/directory/assertion:\x01*\x12\xac\x02\n\x0f\x44\x65leteAssertion\x12\x35.aserto.directory.assertion.v3.DeleteAssertionRequest\x1a\x36.aserto.directory.assertion.v3.DeleteAssertionResponse\"\xa9\x01\x92\x41~\n\tdirectory\x12\x10\x44\x65lete assertion\x1a\x11\x44\x65lete assertion.*\'directory.assertion.v3.assertion.deleteb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\"* /api/v3/directory/assertion/{id}BLZJgithub.com/aserto-dev/go-directory/aserto/directory/assertion/v3;assertionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.assertion.v3.assertion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZJgithub.com/aserto-dev/go-directory/aserto/directory/assertion/v3;assertion'
  _globals['_GETASSERTIONREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_GETASSERTIONREQUEST'].fields_by_name['id']._serialized_options = b'\340A\002'
  _globals['_LISTASSERTIONSREQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_LISTASSERTIONSREQUEST'].fields_by_name['page']._serialized_options = b'\340A\001'
  _globals['_SETASSERTIONREQUEST'].fields_by_name['assert']._loaded_options = None
  _globals['_SETASSERTIONREQUEST'].fields_by_name['assert']._serialized_options = b'\340A\002'
  _globals['_DELETEASSERTIONREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_DELETEASSERTIONREQUEST'].fields_by_name['id']._serialized_options = b'\340A\002'
  _globals['_ASSERT'].fields_by_name['expected']._loaded_options = None
  _globals['_ASSERT'].fields_by_name['expected']._serialized_options = b'\340A\002'
  _globals['_ASSERTION'].methods_by_name['GetAssertion']._loaded_options = None
  _globals['_ASSERTION'].methods_by_name['GetAssertion']._serialized_options = b'\222A\222\001\n\tdirectory\022\026Get assertion instance\032\"Returns single assertion instance.*$directory.assertion.v3.assertion.getb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\"\022 /api/v3/directory/assertion/{id}'
  _globals['_ASSERTION'].methods_by_name['ListAssertions']._loaded_options = None
  _globals['_ASSERTION'].methods_by_name['ListAssertions']._serialized_options = b'\222A\217\001\n\tdirectory\022\017List assertions\032$Returns list of assertion instances.*&directory.assertion.v3.assertions.listb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\036\022\034/api/v3/directory/assertions'
  _globals['_ASSERTION'].methods_by_name['SetAssertion']._loaded_options = None
  _globals['_ASSERTION'].methods_by_name['SetAssertion']._serialized_options = b'\222Au\n\tdirectory\022\rSet assertion\032\016Set assertion.*$directory.assertion.v3.assertion.setb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002 \"\033/api/v3/directory/assertion:\001*'
  _globals['_ASSERTION'].methods_by_name['DeleteAssertion']._loaded_options = None
  _globals['_ASSERTION'].methods_by_name['DeleteAssertion']._serialized_options = b'\222A~\n\tdirectory\022\020Delete assertion\032\021Delete assertion.*\'directory.assertion.v3.assertion.deleteb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\"* /api/v3/directory/assertion/{id}'
  _globals['_GETASSERTIONREQUEST']._serialized_start=302
  _globals['_GETASSERTIONREQUEST']._serialized_end=344
  _globals['_GETASSERTIONRESPONSE']._serialized_start=346
  _globals['_GETASSERTIONRESPONSE']._serialized_end=431
  _globals['_LISTASSERTIONSREQUEST']._serialized_start=433
  _globals['_LISTASSERTIONSREQUEST']._serialized_end=528
  _globals['_LISTASSERTIONSRESPONSE']._serialized_start=531
  _globals['_LISTASSERTIONSRESPONSE']._serialized_end=688
  _globals['_SETASSERTIONREQUEST']._serialized_start=690
  _globals['_SETASSERTIONREQUEST']._serialized_end=779
  _globals['_SETASSERTIONRESPONSE']._serialized_start=781
  _globals['_SETASSERTIONRESPONSE']._serialized_end=866
  _globals['_DELETEASSERTIONREQUEST']._serialized_start=868
  _globals['_DELETEASSERTIONREQUEST']._serialized_end=913
  _globals['_DELETEASSERTIONRESPONSE']._serialized_start=915
  _globals['_DELETEASSERTIONRESPONSE']._serialized_end=988
  _globals['_ASSERT']._serialized_start=991
  _globals['_ASSERT']._serialized_end=1343
  _globals['_ASSERTION']._serialized_start=1346
  _globals['_ASSERTION']._serialized_end=2572
# @@protoc_insertion_point(module_scope)
