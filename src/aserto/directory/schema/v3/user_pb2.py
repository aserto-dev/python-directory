# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aserto/directory/schema/v3/user.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%aserto/directory/schema/v3/user.proto\x12\x1a\x61serto.directory.schema.v3\"\xbf\x01\n\x0eUserProperties\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12\x18\n\x07picture\x18\x02 \x01(\tR\x07picture\x12>\n\x06status\x18\x03 \x01(\x0e\x32&.aserto.directory.schema.v3.UserStatusR\x06status\x12\x18\n\x07\x65nabled\x18\x04 \x01(\x08R\x07\x65nabled\x12#\n\rconnection_id\x18\x05 \x01(\tR\x0c\x63onnectionId*\x84\x02\n\nUserStatus\x12\x17\n\x13USER_STATUS_UNKNOWN\x10\x00\x12\x16\n\x12USER_STATUS_STAGED\x10\x01\x12\x1b\n\x17USER_STATUS_PROVISIONED\x10\x02\x12\x16\n\x12USER_STATUS_ACTIVE\x10\x03\x12\x18\n\x14USER_STATUS_RECOVERY\x10\x04\x12 \n\x1cUSER_STATUS_PASSWORD_EXPIRED\x10\x05\x12\x1a\n\x16USER_STATUS_LOCKED_OUT\x10\x06\x12\x19\n\x15USER_STATUS_SUSPENDED\x10\x07\x12\x1d\n\x19USER_STATUS_DEPROVISIONED\x10\x08\x42\xfe\x01\n\x1e\x63om.aserto.directory.schema.v3B\tUserProtoP\x01ZDgithub.com/aserto-dev/go-directory/aserto/directory/schema/v3;schema\xa2\x02\x03\x41\x44S\xaa\x02\x1a\x41serto.Directory.Schema.V3\xca\x02\x1b\x41serto\\Directory_\\Schema\\V3\xe2\x02\'Aserto\\Directory_\\Schema\\V3\\GPBMetadata\xea\x02\x1d\x41serto::Directory::Schema::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.directory.schema.v3.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.aserto.directory.schema.v3B\tUserProtoP\001ZDgithub.com/aserto-dev/go-directory/aserto/directory/schema/v3;schema\242\002\003ADS\252\002\032Aserto.Directory.Schema.V3\312\002\033Aserto\\Directory_\\Schema\\V3\342\002\'Aserto\\Directory_\\Schema\\V3\\GPBMetadata\352\002\035Aserto::Directory::Schema::V3'
  _globals['_USERSTATUS']._serialized_start=264
  _globals['_USERSTATUS']._serialized_end=524
  _globals['_USERPROPERTIES']._serialized_start=70
  _globals['_USERPROPERTIES']._serialized_end=261
# @@protoc_insertion_point(module_scope)
