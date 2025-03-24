"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import aserto.directory.common.v3.common_pb2
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

class _Opcode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OpcodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Opcode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OPCODE_UNKNOWN: _Opcode.ValueType  # 0
    OPCODE_SET: _Opcode.ValueType  # 1
    OPCODE_DELETE: _Opcode.ValueType  # 2
    OPCODE_DELETE_WITH_RELATIONS: _Opcode.ValueType  # 3

class Opcode(_Opcode, metaclass=_OpcodeEnumTypeWrapper): ...

OPCODE_UNKNOWN: Opcode.ValueType  # 0
OPCODE_SET: Opcode.ValueType  # 1
OPCODE_DELETE: Opcode.ValueType  # 2
OPCODE_DELETE_WITH_RELATIONS: Opcode.ValueType  # 3
global___Opcode = Opcode

@typing.final
class ImportRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OP_CODE_FIELD_NUMBER: builtins.int
    OBJECT_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    op_code: global___Opcode.ValueType
    """operation Opcode enum value"""
    @property
    def object(self) -> aserto.directory.common.v3.common_pb2.Object:
        """object import message"""

    @property
    def relation(self) -> aserto.directory.common.v3.common_pb2.Relation:
        """relation import message"""

    def __init__(
        self,
        *,
        op_code: global___Opcode.ValueType = ...,
        object: aserto.directory.common.v3.common_pb2.Object | None = ...,
        relation: aserto.directory.common.v3.common_pb2.Relation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["msg", b"msg", "object", b"object", "relation", b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["msg", b"msg", "object", b"object", "op_code", b"op_code", "relation", b"relation"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["msg", b"msg"]) -> typing.Literal["object", "relation"] | None: ...

global___ImportRequest = ImportRequest

@typing.final
class ImportResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    COUNTER_FIELD_NUMBER: builtins.int
    @property
    def object(self) -> global___ImportCounter:
        """object import counter"""

    @property
    def relation(self) -> global___ImportCounter:
        """relation import counter"""

    @property
    def status(self) -> global___ImportStatus:
        """import status message"""

    @property
    def counter(self) -> global___ImportCounter:
        """import counter per type"""

    def __init__(
        self,
        *,
        object: global___ImportCounter | None = ...,
        relation: global___ImportCounter | None = ...,
        status: global___ImportStatus | None = ...,
        counter: global___ImportCounter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["counter", b"counter", "msg", b"msg", "object", b"object", "relation", b"relation", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["counter", b"counter", "msg", b"msg", "object", b"object", "relation", b"relation", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["msg", b"msg"]) -> typing.Literal["status", "counter"] | None: ...

global___ImportResponse = ImportResponse

@typing.final
class ImportCounter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECV_FIELD_NUMBER: builtins.int
    SET_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    recv: builtins.int
    """number of messages received"""
    set: builtins.int
    """number of messages with OPCODE_SET"""
    delete: builtins.int
    """number of messages with OPCODE_DELETE"""
    error: builtins.int
    """number of messages resulting in error"""
    type: builtins.str
    """counter of type (object|relation)"""
    def __init__(
        self,
        *,
        recv: builtins.int = ...,
        set: builtins.int = ...,
        delete: builtins.int = ...,
        error: builtins.int = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["delete", b"delete", "error", b"error", "recv", b"recv", "set", b"set", "type", b"type"]) -> None: ...

global___ImportCounter = ImportCounter

@typing.final
class ImportStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    REQ_FIELD_NUMBER: builtins.int
    code: builtins.int
    """gRPC status code (google.golang.org/grpc/codes)"""
    msg: builtins.str
    """gRPC status message (google.golang.org/grpc/status)"""
    @property
    def req(self) -> global___ImportRequest:
        """req contains the original import request message"""

    def __init__(
        self,
        *,
        code: builtins.int = ...,
        msg: builtins.str = ...,
        req: global___ImportRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["req", b"req"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["code", b"code", "msg", b"msg", "req", b"req"]) -> None: ...

global___ImportStatus = ImportStatus
