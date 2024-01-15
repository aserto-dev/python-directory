# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aserto/directory/schema/v3/tenant.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'aserto/directory/schema/v3/tenant.proto\x12\x1a\x61serto.directory.schema.v3\x1a\x1cgoogle/protobuf/struct.proto\"\xf7\x01\n\x10TenantProperties\x12:\n\x04kind\x18\x01 \x01(\x0e\x32&.aserto.directory.schema.v3.TenantKindR\x04kind\x12!\n\x0c\x64irectory_v2\x18\x02 \x01(\x08R\x0b\x64irectoryV2\x12*\n\x11\x64irectory_v2_only\x18\x03 \x01(\x08R\x0f\x64irectoryV2Only\x12L\n\x07\x61\x63\x63ount\x18\x04 \x01(\x0b\x32-.aserto.directory.schema.v3.AccountPropertiesH\x00R\x07\x61\x63\x63ount\x88\x01\x01\x42\n\n\x08_account\"\xc4\x01\n\x11\x41\x63\x63ountProperties\x12\x19\n\x08max_orgs\x18\x01 \x01(\x05R\x07maxOrgs\x12T\n\x0fgetting_started\x18\x03 \x01(\x0b\x32&.aserto.directory.schema.v3.GuideStateH\x00R\x0egettingStarted\x88\x01\x01\x12*\n\x11\x64\x65\x66\x61ult_tenant_id\x18\x04 \x01(\tR\x0f\x64\x65\x66\x61ultTenantIdB\x12\n\x10_getting_started\"O\n\nGuideState\x12\x12\n\x04show\x18\x01 \x01(\x08R\x04show\x12-\n\x05steps\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructR\x05steps*\\\n\nTenantKind\x12\x17\n\x13TENANT_KIND_UNKNOWN\x10\x00\x12\x1c\n\x18TENANT_KIND_ORGANIZATION\x10\x01\x12\x17\n\x13TENANT_KIND_ACCOUNT\x10\x02\x42\x80\x02\n\x1e\x63om.aserto.directory.schema.v3B\x0bTenantProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/schema/v3;schema\xa2\x02\x03\x41\x44S\xaa\x02\x1a\x41serto.Directory.Schema.V3\xca\x02\x1b\x41serto\\Directory_\\Schema\\V3\xe2\x02\'Aserto\\Directory_\\Schema\\V3\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Schema::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.schema.v3.tenant_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.schema.v3B\013TenantProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/schema/v3;schema\242\002\003ADS\252\002\032Aserto.Directory.Schema.V3\312\002\033Aserto\\Directory_\\Schema\\V3\342\002\'Aserto\\Directory_\\Schema\\V3\\GPBMetadata\352\002\035Aserto::Directory::Schema::V3'
  _globals['_TENANTKIND']._serialized_start=631
  _globals['_TENANTKIND']._serialized_end=723
  _globals['_TENANTPROPERTIES']._serialized_start=102
  _globals['_TENANTPROPERTIES']._serialized_end=349
  _globals['_ACCOUNTPROPERTIES']._serialized_start=352
  _globals['_ACCOUNTPROPERTIES']._serialized_end=548
  _globals['_GUIDESTATE']._serialized_start=550
  _globals['_GUIDESTATE']._serialized_end=629
# @@protoc_insertion_point(module_scope)
