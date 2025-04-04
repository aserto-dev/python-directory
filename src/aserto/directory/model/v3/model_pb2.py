# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/model/v3/model.proto
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
    'aserto/directory/model/v3/model.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%aserto/directory/model/v3/model.proto\x12\x19\x61serto.directory.model.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"B\n\x12GetManifestRequest\x12,\n\x05\x65mpty\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x05\x65mpty\"\xc7\x01\n\x13GetManifestResponse\x12\x41\n\x08metadata\x18\x01 \x01(\x0b\x32#.aserto.directory.model.v3.MetadataH\x00R\x08metadata\x12\x35\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x1f.aserto.directory.model.v3.BodyH\x00R\x04\x62ody\x12/\n\x05model\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructH\x00R\x05modelB\x05\n\x03msg\"R\n\x12SetManifestRequest\x12\x35\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x1f.aserto.directory.model.v3.BodyH\x00R\x04\x62odyB\x05\n\x03msg\"E\n\x13SetManifestResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"E\n\x15\x44\x65leteManifestRequest\x12,\n\x05\x65mpty\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x05\x65mpty\"H\n\x16\x44\x65leteManifestResponse\x12.\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyR\x06result\"c\n\x08Metadata\x12>\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\tupdatedAt\x12\x17\n\x04\x65tag\x18\x17 \x01(\tB\x03\xe0\x41\x01R\x04\x65tag\"\x1a\n\x04\x42ody\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta2\x8e\x04\n\x05Model\x12v\n\x0bGetManifest\x12-.aserto.directory.model.v3.GetManifestRequest\x1a..aserto.directory.model.v3.GetManifestResponse\"\x06\x82\xd3\xe4\x93\x02\x00\x30\x01\x12v\n\x0bSetManifest\x12-.aserto.directory.model.v3.SetManifestRequest\x1a..aserto.directory.model.v3.SetManifestResponse\"\x06\x82\xd3\xe4\x93\x02\x00(\x01\x12\x94\x02\n\x0e\x44\x65leteManifest\x12\x30.aserto.directory.model.v3.DeleteManifestRequest\x1a\x31.aserto.directory.model.v3.DeleteManifestResponse\"\x9c\x01\x92\x41w\n\tdirectory\x12\x0f\x44\x65lete manifest\x1a\x10\x44\x65lete manifest.*\"directory.model.v3.manifest.deleteb#\n\x13\n\x0f\x44irectoryAPIKey\x12\x00\n\x0c\n\x08TenantID\x12\x00\x82\xd3\xe4\x93\x02\x1c*\x1a/api/v3/directory/manifestBDZBgithub.com/aserto-dev/go-directory/aserto/directory/model/v3;modelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.model.v3.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/aserto-dev/go-directory/aserto/directory/model/v3;model'
  _globals['_METADATA'].fields_by_name['updated_at']._loaded_options = None
  _globals['_METADATA'].fields_by_name['updated_at']._serialized_options = b'\340A\003'
  _globals['_METADATA'].fields_by_name['etag']._loaded_options = None
  _globals['_METADATA'].fields_by_name['etag']._serialized_options = b'\340A\001'
  _globals['_MODEL'].methods_by_name['GetManifest']._loaded_options = None
  _globals['_MODEL'].methods_by_name['GetManifest']._serialized_options = b'\202\323\344\223\002\000'
  _globals['_MODEL'].methods_by_name['SetManifest']._loaded_options = None
  _globals['_MODEL'].methods_by_name['SetManifest']._serialized_options = b'\202\323\344\223\002\000'
  _globals['_MODEL'].methods_by_name['DeleteManifest']._loaded_options = None
  _globals['_MODEL'].methods_by_name['DeleteManifest']._serialized_options = b'\222Aw\n\tdirectory\022\017Delete manifest\032\020Delete manifest.*\"directory.model.v3.manifest.deleteb#\n\023\n\017DirectoryAPIKey\022\000\n\014\n\010TenantID\022\000\202\323\344\223\002\034*\032/api/v3/directory/manifest'
  _globals['_GETMANIFESTREQUEST']._serialized_start=271
  _globals['_GETMANIFESTREQUEST']._serialized_end=337
  _globals['_GETMANIFESTRESPONSE']._serialized_start=340
  _globals['_GETMANIFESTRESPONSE']._serialized_end=539
  _globals['_SETMANIFESTREQUEST']._serialized_start=541
  _globals['_SETMANIFESTREQUEST']._serialized_end=623
  _globals['_SETMANIFESTRESPONSE']._serialized_start=625
  _globals['_SETMANIFESTRESPONSE']._serialized_end=694
  _globals['_DELETEMANIFESTREQUEST']._serialized_start=696
  _globals['_DELETEMANIFESTREQUEST']._serialized_end=765
  _globals['_DELETEMANIFESTRESPONSE']._serialized_start=767
  _globals['_DELETEMANIFESTRESPONSE']._serialized_end=839
  _globals['_METADATA']._serialized_start=841
  _globals['_METADATA']._serialized_end=940
  _globals['_BODY']._serialized_start=942
  _globals['_BODY']._serialized_end=968
  _globals['_MODEL']._serialized_start=971
  _globals['_MODEL']._serialized_end=1497
# @@protoc_insertion_point(module_scope)
