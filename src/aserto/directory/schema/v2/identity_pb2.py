# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aserto/directory/schema/v2/identity.proto
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
    'aserto/directory/schema/v2/identity.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)aserto/directory/schema/v2/identity.proto\x12\x1a\x61serto.directory.schema.v2\"\xc6\x01\n\x12IdentityProperties\x12<\n\x04kind\x18\x01 \x01(\x0e\x32(.aserto.directory.schema.v2.IdentityKindR\x04kind\x12\x1a\n\x08provider\x18\x02 \x01(\tR\x08provider\x12\x1a\n\x08verified\x18\x03 \x01(\x08R\x08verified\x12(\n\rconnection_id\x18\x04 \x01(\tH\x00R\x0c\x63onnectionId\x88\x01\x01\x42\x10\n\x0e_connection_id*\xbd\x01\n\x0cIdentityKind\x12\x19\n\x15IDENTITY_KIND_UNKNOWN\x10\x00\x12\x15\n\x11IDENTITY_KIND_PID\x10\x01\x12\x17\n\x13IDENTITY_KIND_EMAIL\x10\x02\x12\x1a\n\x16IDENTITY_KIND_USERNAME\x10\x03\x12\x14\n\x10IDENTITY_KIND_DN\x10\x04\x12\x17\n\x13IDENTITY_KIND_PHONE\x10\x05\x12\x17\n\x13IDENTITY_KIND_EMPID\x10\x06\x42\x82\x02\n\x1e\x63om.aserto.directory.schema.v2B\rIdentityProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/schema/v2;schema\xa2\x02\x03\x41\x44S\xaa\x02\x1a\x41serto.Directory.Schema.V2\xca\x02\x1b\x41serto\\Directory_\\Schema\\V2\xe2\x02\'Aserto\\Directory_\\Schema\\V2\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Schema::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.schema.v2.identity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.schema.v2B\rIdentityProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/schema/v2;schema\242\002\003ADS\252\002\032Aserto.Directory.Schema.V2\312\002\033Aserto\\Directory_\\Schema\\V2\342\002\'Aserto\\Directory_\\Schema\\V2\\GPBMetadata\352\002\035Aserto::Directory::Schema::V2'
  _globals['_IDENTITYKIND']._serialized_start=275
  _globals['_IDENTITYKIND']._serialized_end=464
  _globals['_IDENTITYPROPERTIES']._serialized_start=74
  _globals['_IDENTITYPROPERTIES']._serialized_end=272
# @@protoc_insertion_point(module_scope)
