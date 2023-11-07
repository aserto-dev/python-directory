"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _IdentityKind:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IdentityKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IdentityKind.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    IDENTITY_KIND_UNKNOWN: _IdentityKind.ValueType  # 0
    """undefined state"""
    IDENTITY_KIND_PID: _IdentityKind.ValueType  # 1
    """provider unique identifier"""
    IDENTITY_KIND_EMAIL: _IdentityKind.ValueType  # 2
    """email address"""
    IDENTITY_KIND_USERNAME: _IdentityKind.ValueType  # 3
    """username"""
    IDENTITY_KIND_DN: _IdentityKind.ValueType  # 4
    """distinguished name format RFC1779"""
    IDENTITY_KIND_PHONE: _IdentityKind.ValueType  # 5
    """phone number using the format described in RFC3966, using the E.164 recommendation"""
    IDENTITY_KIND_EMPID: _IdentityKind.ValueType  # 6
    """employee identifier"""

class IdentityKind(_IdentityKind, metaclass=_IdentityKindEnumTypeWrapper): ...

IDENTITY_KIND_UNKNOWN: IdentityKind.ValueType  # 0
"""undefined state"""
IDENTITY_KIND_PID: IdentityKind.ValueType  # 1
"""provider unique identifier"""
IDENTITY_KIND_EMAIL: IdentityKind.ValueType  # 2
"""email address"""
IDENTITY_KIND_USERNAME: IdentityKind.ValueType  # 3
"""username"""
IDENTITY_KIND_DN: IdentityKind.ValueType  # 4
"""distinguished name format RFC1779"""
IDENTITY_KIND_PHONE: IdentityKind.ValueType  # 5
"""phone number using the format described in RFC3966, using the E.164 recommendation"""
IDENTITY_KIND_EMPID: IdentityKind.ValueType  # 6
"""employee identifier"""
global___IdentityKind = IdentityKind

@typing_extensions.final
class IdentityProperties(google.protobuf.message.Message):
    """Properties of "identity" objects."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KIND_FIELD_NUMBER: builtins.int
    PROVIDER_FIELD_NUMBER: builtins.int
    VERIFIED_FIELD_NUMBER: builtins.int
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    kind: global___IdentityKind.ValueType
    """identity kind [email|username|uid|pid|dn|phone]"""
    provider: builtins.str
    """identity provider name"""
    verified: builtins.bool
    """identity has been verified (false when not explicitly specified)"""
    connection_id: builtins.str
    """IDP connection id which owns the object instance"""
    def __init__(
        self,
        *,
        kind: global___IdentityKind.ValueType = ...,
        provider: builtins.str = ...,
        verified: builtins.bool = ...,
        connection_id: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_connection_id", b"_connection_id", "connection_id", b"connection_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_connection_id", b"_connection_id", "connection_id", b"connection_id", "kind", b"kind", "provider", b"provider", "verified", b"verified"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_connection_id", b"_connection_id"]) -> typing_extensions.Literal["connection_id"] | None: ...

global___IdentityProperties = IdentityProperties
