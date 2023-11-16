# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc-gen-openapiv2/options/openapiv2.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,protoc-gen-openapiv2/options/openapiv2.proto\x12)grpc.gateway.protoc_gen_openapiv2.options\x1a\x1cgoogle/protobuf/struct.proto\"\xb3\x08\n\x07Swagger\x12\x18\n\x07swagger\x18\x01 \x01(\tR\x07swagger\x12\x43\n\x04info\x18\x02 \x01(\x0b\x32/.grpc.gateway.protoc_gen_openapiv2.options.InfoR\x04info\x12\x12\n\x04host\x18\x03 \x01(\tR\x04host\x12\x1b\n\tbase_path\x18\x04 \x01(\tR\x08\x62\x61sePath\x12K\n\x07schemes\x18\x05 \x03(\x0e\x32\x31.grpc.gateway.protoc_gen_openapiv2.options.SchemeR\x07schemes\x12\x1a\n\x08\x63onsumes\x18\x06 \x03(\tR\x08\x63onsumes\x12\x1a\n\x08produces\x18\x07 \x03(\tR\x08produces\x12_\n\tresponses\x18\n \x03(\x0b\x32\x41.grpc.gateway.protoc_gen_openapiv2.options.Swagger.ResponsesEntryR\tresponses\x12q\n\x14security_definitions\x18\x0b \x01(\x0b\x32>.grpc.gateway.protoc_gen_openapiv2.options.SecurityDefinitionsR\x13securityDefinitions\x12Z\n\x08security\x18\x0c \x03(\x0b\x32>.grpc.gateway.protoc_gen_openapiv2.options.SecurityRequirementR\x08security\x12\x42\n\x04tags\x18\r \x03(\x0b\x32..grpc.gateway.protoc_gen_openapiv2.options.TagR\x04tags\x12\x65\n\rexternal_docs\x18\x0e \x01(\x0b\x32@.grpc.gateway.protoc_gen_openapiv2.options.ExternalDocumentationR\x0c\x65xternalDocs\x12\x62\n\nextensions\x18\x0f \x03(\x0b\x32\x42.grpc.gateway.protoc_gen_openapiv2.options.Swagger.ExtensionsEntryR\nextensions\x1aq\n\x0eResponsesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12I\n\x05value\x18\x02 \x01(\x0b\x32\x33.grpc.gateway.protoc_gen_openapiv2.options.ResponseR\x05value:\x02\x38\x01\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01J\x04\x08\x08\x10\tJ\x04\x08\t\x10\n\"\xd6\x07\n\tOperation\x12\x12\n\x04tags\x18\x01 \x03(\tR\x04tags\x12\x18\n\x07summary\x18\x02 \x01(\tR\x07summary\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x65\n\rexternal_docs\x18\x04 \x01(\x0b\x32@.grpc.gateway.protoc_gen_openapiv2.options.ExternalDocumentationR\x0c\x65xternalDocs\x12!\n\x0coperation_id\x18\x05 \x01(\tR\x0boperationId\x12\x1a\n\x08\x63onsumes\x18\x06 \x03(\tR\x08\x63onsumes\x12\x1a\n\x08produces\x18\x07 \x03(\tR\x08produces\x12\x61\n\tresponses\x18\t \x03(\x0b\x32\x43.grpc.gateway.protoc_gen_openapiv2.options.Operation.ResponsesEntryR\tresponses\x12K\n\x07schemes\x18\n \x03(\x0e\x32\x31.grpc.gateway.protoc_gen_openapiv2.options.SchemeR\x07schemes\x12\x1e\n\ndeprecated\x18\x0b \x01(\x08R\ndeprecated\x12Z\n\x08security\x18\x0c \x03(\x0b\x32>.grpc.gateway.protoc_gen_openapiv2.options.SecurityRequirementR\x08security\x12\x64\n\nextensions\x18\r \x03(\x0b\x32\x44.grpc.gateway.protoc_gen_openapiv2.options.Operation.ExtensionsEntryR\nextensions\x12U\n\nparameters\x18\x0e \x01(\x0b\x32\x35.grpc.gateway.protoc_gen_openapiv2.options.ParametersR\nparameters\x1aq\n\x0eResponsesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12I\n\x05value\x18\x02 \x01(\x0b\x32\x33.grpc.gateway.protoc_gen_openapiv2.options.ResponseR\x05value:\x02\x38\x01\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01J\x04\x08\x08\x10\t\"b\n\nParameters\x12T\n\x07headers\x18\x01 \x03(\x0b\x32:.grpc.gateway.protoc_gen_openapiv2.options.HeaderParameterR\x07headers\"\xa3\x02\n\x0fHeaderParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12S\n\x04type\x18\x03 \x01(\x0e\x32?.grpc.gateway.protoc_gen_openapiv2.options.HeaderParameter.TypeR\x04type\x12\x16\n\x06\x66ormat\x18\x04 \x01(\tR\x06\x66ormat\x12\x1a\n\x08required\x18\x05 \x01(\x08R\x08required\"E\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06STRING\x10\x01\x12\n\n\x06NUMBER\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\"\xd8\x01\n\x06Header\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x16\n\x06\x66ormat\x18\x03 \x01(\tR\x06\x66ormat\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\tR\x07\x64\x65\x66\x61ult\x12\x18\n\x07pattern\x18\r \x01(\tR\x07patternJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13\"\x9a\x05\n\x08Response\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12I\n\x06schema\x18\x02 \x01(\x0b\x32\x31.grpc.gateway.protoc_gen_openapiv2.options.SchemaR\x06schema\x12Z\n\x07headers\x18\x03 \x03(\x0b\x32@.grpc.gateway.protoc_gen_openapiv2.options.Response.HeadersEntryR\x07headers\x12]\n\x08\x65xamples\x18\x04 \x03(\x0b\x32\x41.grpc.gateway.protoc_gen_openapiv2.options.Response.ExamplesEntryR\x08\x65xamples\x12\x63\n\nextensions\x18\x05 \x03(\x0b\x32\x43.grpc.gateway.protoc_gen_openapiv2.options.Response.ExtensionsEntryR\nextensions\x1am\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.grpc.gateway.protoc_gen_openapiv2.options.HeaderR\x05value:\x02\x38\x01\x1a;\n\rExamplesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"\xd6\x03\n\x04Info\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12(\n\x10terms_of_service\x18\x03 \x01(\tR\x0etermsOfService\x12L\n\x07\x63ontact\x18\x04 \x01(\x0b\x32\x32.grpc.gateway.protoc_gen_openapiv2.options.ContactR\x07\x63ontact\x12L\n\x07license\x18\x05 \x01(\x0b\x32\x32.grpc.gateway.protoc_gen_openapiv2.options.LicenseR\x07license\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\x12_\n\nextensions\x18\x07 \x03(\x0b\x32?.grpc.gateway.protoc_gen_openapiv2.options.Info.ExtensionsEntryR\nextensions\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"E\n\x07\x43ontact\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x14\n\x05\x65mail\x18\x03 \x01(\tR\x05\x65mail\"/\n\x07License\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"K\n\x15\x45xternalDocumentation\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"\xaa\x02\n\x06Schema\x12V\n\x0bjson_schema\x18\x01 \x01(\x0b\x32\x35.grpc.gateway.protoc_gen_openapiv2.options.JSONSchemaR\njsonSchema\x12$\n\rdiscriminator\x18\x02 \x01(\tR\rdiscriminator\x12\x1b\n\tread_only\x18\x03 \x01(\x08R\x08readOnly\x12\x65\n\rexternal_docs\x18\x05 \x01(\x0b\x32@.grpc.gateway.protoc_gen_openapiv2.options.ExternalDocumentationR\x0c\x65xternalDocs\x12\x18\n\x07\x65xample\x18\x06 \x01(\tR\x07\x65xampleJ\x04\x08\x04\x10\x05\"\xd7\n\n\nJSONSchema\x12\x10\n\x03ref\x18\x03 \x01(\tR\x03ref\x12\x14\n\x05title\x18\x05 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x07 \x01(\tR\x07\x64\x65\x66\x61ult\x12\x1b\n\tread_only\x18\x08 \x01(\x08R\x08readOnly\x12\x18\n\x07\x65xample\x18\t \x01(\tR\x07\x65xample\x12\x1f\n\x0bmultiple_of\x18\n \x01(\x01R\nmultipleOf\x12\x18\n\x07maximum\x18\x0b \x01(\x01R\x07maximum\x12+\n\x11\x65xclusive_maximum\x18\x0c \x01(\x08R\x10\x65xclusiveMaximum\x12\x18\n\x07minimum\x18\r \x01(\x01R\x07minimum\x12+\n\x11\x65xclusive_minimum\x18\x0e \x01(\x08R\x10\x65xclusiveMinimum\x12\x1d\n\nmax_length\x18\x0f \x01(\x04R\tmaxLength\x12\x1d\n\nmin_length\x18\x10 \x01(\x04R\tminLength\x12\x18\n\x07pattern\x18\x11 \x01(\tR\x07pattern\x12\x1b\n\tmax_items\x18\x14 \x01(\x04R\x08maxItems\x12\x1b\n\tmin_items\x18\x15 \x01(\x04R\x08minItems\x12!\n\x0cunique_items\x18\x16 \x01(\x08R\x0buniqueItems\x12%\n\x0emax_properties\x18\x18 \x01(\x04R\rmaxProperties\x12%\n\x0emin_properties\x18\x19 \x01(\x04R\rminProperties\x12\x1a\n\x08required\x18\x1a \x03(\tR\x08required\x12\x14\n\x05\x61rray\x18\" \x03(\tR\x05\x61rray\x12_\n\x04type\x18# \x03(\x0e\x32K.grpc.gateway.protoc_gen_openapiv2.options.JSONSchema.JSONSchemaSimpleTypesR\x04type\x12\x16\n\x06\x66ormat\x18$ \x01(\tR\x06\x66ormat\x12\x12\n\x04\x65num\x18. \x03(\tR\x04\x65num\x12z\n\x13\x66ield_configuration\x18\xe9\x07 \x01(\x0b\x32H.grpc.gateway.protoc_gen_openapiv2.options.JSONSchema.FieldConfigurationR\x12\x66ieldConfiguration\x12\x65\n\nextensions\x18\x30 \x03(\x0b\x32\x45.grpc.gateway.protoc_gen_openapiv2.options.JSONSchema.ExtensionsEntryR\nextensions\x1a<\n\x12\x46ieldConfiguration\x12&\n\x0fpath_param_name\x18/ \x01(\tR\rpathParamName\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"w\n\x15JSONSchemaSimpleTypes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41RRAY\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x08\n\x04NULL\x10\x04\x12\n\n\x06NUMBER\x10\x05\x12\n\n\x06OBJECT\x10\x06\x12\n\n\x06STRING\x10\x07J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\x12\x10\x13J\x04\x08\x13\x10\x14J\x04\x08\x17\x10\x18J\x04\x08\x1b\x10\x1cJ\x04\x08\x1c\x10\x1dJ\x04\x08\x1d\x10\x1eJ\x04\x08\x1e\x10\"J\x04\x08%\x10*J\x04\x08*\x10+J\x04\x08+\x10.\"\xd9\x02\n\x03Tag\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x65\n\rexternal_docs\x18\x03 \x01(\x0b\x32@.grpc.gateway.protoc_gen_openapiv2.options.ExternalDocumentationR\x0c\x65xternalDocs\x12^\n\nextensions\x18\x04 \x03(\x0b\x32>.grpc.gateway.protoc_gen_openapiv2.options.Tag.ExtensionsEntryR\nextensions\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"\xf7\x01\n\x13SecurityDefinitions\x12h\n\x08security\x18\x01 \x03(\x0b\x32L.grpc.gateway.protoc_gen_openapiv2.options.SecurityDefinitions.SecurityEntryR\x08security\x1av\n\rSecurityEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12O\n\x05value\x18\x02 \x01(\x0b\x32\x39.grpc.gateway.protoc_gen_openapiv2.options.SecuritySchemeR\x05value:\x02\x38\x01\"\xff\x06\n\x0eSecurityScheme\x12R\n\x04type\x18\x01 \x01(\x0e\x32>.grpc.gateway.protoc_gen_openapiv2.options.SecurityScheme.TypeR\x04type\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12L\n\x02in\x18\x04 \x01(\x0e\x32<.grpc.gateway.protoc_gen_openapiv2.options.SecurityScheme.InR\x02in\x12R\n\x04\x66low\x18\x05 \x01(\x0e\x32>.grpc.gateway.protoc_gen_openapiv2.options.SecurityScheme.FlowR\x04\x66low\x12+\n\x11\x61uthorization_url\x18\x06 \x01(\tR\x10\x61uthorizationUrl\x12\x1b\n\ttoken_url\x18\x07 \x01(\tR\x08tokenUrl\x12I\n\x06scopes\x18\x08 \x01(\x0b\x32\x31.grpc.gateway.protoc_gen_openapiv2.options.ScopesR\x06scopes\x12i\n\nextensions\x18\t \x03(\x0b\x32I.grpc.gateway.protoc_gen_openapiv2.options.SecurityScheme.ExtensionsEntryR\nextensions\x1aU\n\x0f\x45xtensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"K\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x0e\n\nTYPE_BASIC\x10\x01\x12\x10\n\x0cTYPE_API_KEY\x10\x02\x12\x0f\n\x0bTYPE_OAUTH2\x10\x03\"1\n\x02In\x12\x0e\n\nIN_INVALID\x10\x00\x12\x0c\n\x08IN_QUERY\x10\x01\x12\r\n\tIN_HEADER\x10\x02\"j\n\x04\x46low\x12\x10\n\x0c\x46LOW_INVALID\x10\x00\x12\x11\n\rFLOW_IMPLICIT\x10\x01\x12\x11\n\rFLOW_PASSWORD\x10\x02\x12\x14\n\x10\x46LOW_APPLICATION\x10\x03\x12\x14\n\x10\x46LOW_ACCESS_CODE\x10\x04\"\xf6\x02\n\x13SecurityRequirement\x12\x8a\x01\n\x14security_requirement\x18\x01 \x03(\x0b\x32W.grpc.gateway.protoc_gen_openapiv2.options.SecurityRequirement.SecurityRequirementEntryR\x13securityRequirement\x1a\x30\n\x18SecurityRequirementValue\x12\x14\n\x05scope\x18\x01 \x03(\tR\x05scope\x1a\x9f\x01\n\x18SecurityRequirementEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12m\n\x05value\x18\x02 \x01(\x0b\x32W.grpc.gateway.protoc_gen_openapiv2.options.SecurityRequirement.SecurityRequirementValueR\x05value:\x02\x38\x01\"\x96\x01\n\x06Scopes\x12R\n\x05scope\x18\x01 \x03(\x0b\x32<.grpc.gateway.protoc_gen_openapiv2.options.Scopes.ScopeEntryR\x05scope\x1a\x38\n\nScopeEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01*;\n\x06Scheme\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02\x12\x06\n\x02WS\x10\x03\x12\x07\n\x03WSS\x10\x04\x42\xc7\x02\n-com.grpc.gateway.protoc_gen_openapiv2.optionsB\x0eOpenapiv2ProtoP\x01ZFgithub.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2/options\xa2\x02\x04GGPO\xaa\x02\'Grpc.Gateway.ProtocGenOpenapiv2.Options\xca\x02\'Grpc\\Gateway\\ProtocGenOpenapiv2\\Options\xe2\x02\x33Grpc\\Gateway\\ProtocGenOpenapiv2\\Options\\GPBMetadata\xea\x02*Grpc::Gateway::ProtocGenOpenapiv2::Optionsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protoc_gen_openapiv2.options.openapiv2_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-com.grpc.gateway.protoc_gen_openapiv2.optionsB\016Openapiv2ProtoP\001ZFgithub.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2/options\242\002\004GGPO\252\002\'Grpc.Gateway.ProtocGenOpenapiv2.Options\312\002\'Grpc\\Gateway\\ProtocGenOpenapiv2\\Options\342\0023Grpc\\Gateway\\ProtocGenOpenapiv2\\Options\\GPBMetadata\352\002*Grpc::Gateway::ProtocGenOpenapiv2::Options'
  _globals['_SWAGGER_RESPONSESENTRY']._options = None
  _globals['_SWAGGER_RESPONSESENTRY']._serialized_options = b'8\001'
  _globals['_SWAGGER_EXTENSIONSENTRY']._options = None
  _globals['_SWAGGER_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_OPERATION_RESPONSESENTRY']._options = None
  _globals['_OPERATION_RESPONSESENTRY']._serialized_options = b'8\001'
  _globals['_OPERATION_EXTENSIONSENTRY']._options = None
  _globals['_OPERATION_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_RESPONSE_HEADERSENTRY']._options = None
  _globals['_RESPONSE_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_RESPONSE_EXAMPLESENTRY']._options = None
  _globals['_RESPONSE_EXAMPLESENTRY']._serialized_options = b'8\001'
  _globals['_RESPONSE_EXTENSIONSENTRY']._options = None
  _globals['_RESPONSE_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_EXTENSIONSENTRY']._options = None
  _globals['_INFO_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_JSONSCHEMA_EXTENSIONSENTRY']._options = None
  _globals['_JSONSCHEMA_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_TAG_EXTENSIONSENTRY']._options = None
  _globals['_TAG_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_SECURITYDEFINITIONS_SECURITYENTRY']._options = None
  _globals['_SECURITYDEFINITIONS_SECURITYENTRY']._serialized_options = b'8\001'
  _globals['_SECURITYSCHEME_EXTENSIONSENTRY']._options = None
  _globals['_SECURITYSCHEME_EXTENSIONSENTRY']._serialized_options = b'8\001'
  _globals['_SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY']._options = None
  _globals['_SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY']._serialized_options = b'8\001'
  _globals['_SCOPES_SCOPEENTRY']._options = None
  _globals['_SCOPES_SCOPEENTRY']._serialized_options = b'8\001'
  _globals['_SCHEME']._serialized_start=7833
  _globals['_SCHEME']._serialized_end=7892
  _globals['_SWAGGER']._serialized_start=122
  _globals['_SWAGGER']._serialized_end=1197
  _globals['_SWAGGER_RESPONSESENTRY']._serialized_start=985
  _globals['_SWAGGER_RESPONSESENTRY']._serialized_end=1098
  _globals['_SWAGGER_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_SWAGGER_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_OPERATION']._serialized_start=1200
  _globals['_OPERATION']._serialized_end=2182
  _globals['_OPERATION_RESPONSESENTRY']._serialized_start=985
  _globals['_OPERATION_RESPONSESENTRY']._serialized_end=1098
  _globals['_OPERATION_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_OPERATION_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_PARAMETERS']._serialized_start=2184
  _globals['_PARAMETERS']._serialized_end=2282
  _globals['_HEADERPARAMETER']._serialized_start=2285
  _globals['_HEADERPARAMETER']._serialized_end=2576
  _globals['_HEADERPARAMETER_TYPE']._serialized_start=2495
  _globals['_HEADERPARAMETER_TYPE']._serialized_end=2564
  _globals['_HEADER']._serialized_start=2579
  _globals['_HEADER']._serialized_end=2795
  _globals['_RESPONSE']._serialized_start=2798
  _globals['_RESPONSE']._serialized_end=3464
  _globals['_RESPONSE_HEADERSENTRY']._serialized_start=3207
  _globals['_RESPONSE_HEADERSENTRY']._serialized_end=3316
  _globals['_RESPONSE_EXAMPLESENTRY']._serialized_start=3318
  _globals['_RESPONSE_EXAMPLESENTRY']._serialized_end=3377
  _globals['_RESPONSE_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_RESPONSE_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_INFO']._serialized_start=3467
  _globals['_INFO']._serialized_end=3937
  _globals['_INFO_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_INFO_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_CONTACT']._serialized_start=3939
  _globals['_CONTACT']._serialized_end=4008
  _globals['_LICENSE']._serialized_start=4010
  _globals['_LICENSE']._serialized_end=4057
  _globals['_EXTERNALDOCUMENTATION']._serialized_start=4059
  _globals['_EXTERNALDOCUMENTATION']._serialized_end=4134
  _globals['_SCHEMA']._serialized_start=4137
  _globals['_SCHEMA']._serialized_end=4435
  _globals['_JSONSCHEMA']._serialized_start=4438
  _globals['_JSONSCHEMA']._serialized_end=5805
  _globals['_JSONSCHEMA_FIELDCONFIGURATION']._serialized_start=5459
  _globals['_JSONSCHEMA_FIELDCONFIGURATION']._serialized_end=5519
  _globals['_JSONSCHEMA_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_JSONSCHEMA_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_JSONSCHEMA_JSONSCHEMASIMPLETYPES']._serialized_start=5608
  _globals['_JSONSCHEMA_JSONSCHEMASIMPLETYPES']._serialized_end=5727
  _globals['_TAG']._serialized_start=5808
  _globals['_TAG']._serialized_end=6153
  _globals['_TAG_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_TAG_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_SECURITYDEFINITIONS']._serialized_start=6156
  _globals['_SECURITYDEFINITIONS']._serialized_end=6403
  _globals['_SECURITYDEFINITIONS_SECURITYENTRY']._serialized_start=6285
  _globals['_SECURITYDEFINITIONS_SECURITYENTRY']._serialized_end=6403
  _globals['_SECURITYSCHEME']._serialized_start=6406
  _globals['_SECURITYSCHEME']._serialized_end=7301
  _globals['_SECURITYSCHEME_EXTENSIONSENTRY']._serialized_start=1100
  _globals['_SECURITYSCHEME_EXTENSIONSENTRY']._serialized_end=1185
  _globals['_SECURITYSCHEME_TYPE']._serialized_start=7067
  _globals['_SECURITYSCHEME_TYPE']._serialized_end=7142
  _globals['_SECURITYSCHEME_IN']._serialized_start=7144
  _globals['_SECURITYSCHEME_IN']._serialized_end=7193
  _globals['_SECURITYSCHEME_FLOW']._serialized_start=7195
  _globals['_SECURITYSCHEME_FLOW']._serialized_end=7301
  _globals['_SECURITYREQUIREMENT']._serialized_start=7304
  _globals['_SECURITYREQUIREMENT']._serialized_end=7678
  _globals['_SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE']._serialized_start=7468
  _globals['_SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE']._serialized_end=7516
  _globals['_SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY']._serialized_start=7519
  _globals['_SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY']._serialized_end=7678
  _globals['_SCOPES']._serialized_start=7681
  _globals['_SCOPES']._serialized_end=7831
  _globals['_SCOPES_SCOPEENTRY']._serialized_start=7775
  _globals['_SCOPES_SCOPEENTRY']._serialized_end=7831
# @@protoc_insertion_point(module_scope)
