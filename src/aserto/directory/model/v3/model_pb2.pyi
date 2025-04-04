"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetManifestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EMPTY_FIELD_NUMBER: builtins.int
    @property
    def empty(self) -> google.protobuf.empty_pb2.Empty:
        """empty request"""

    def __init__(
        self,
        *,
        empty: google.protobuf.empty_pb2.Empty | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["empty", b"empty"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["empty", b"empty"]) -> None: ...

global___GetManifestRequest = GetManifestRequest

@typing.final
class GetManifestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___Metadata:
        """Manifest metadata"""

    @property
    def body(self) -> global___Body:
        """Manifest content"""

    @property
    def model(self) -> google.protobuf.struct_pb2.Struct:
        """Model"""

    def __init__(
        self,
        *,
        metadata: global___Metadata | None = ...,
        body: global___Body | None = ...,
        model: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["body", b"body", "metadata", b"metadata", "model", b"model", "msg", b"msg"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["body", b"body", "metadata", b"metadata", "model", b"model", "msg", b"msg"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["msg", b"msg"]) -> typing.Literal["metadata", "body", "model"] | None: ...

global___GetManifestResponse = GetManifestResponse

@typing.final
class SetManifestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_FIELD_NUMBER: builtins.int
    @property
    def body(self) -> global___Body:
        """Manifest content"""

    def __init__(
        self,
        *,
        body: global___Body | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["body", b"body", "msg", b"msg"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["body", b"body", "msg", b"msg"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["msg", b"msg"]) -> typing.Literal["body"] | None: ...

global___SetManifestRequest = SetManifestRequest

@typing.final
class SetManifestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.empty_pb2.Empty:
        """empty result"""

    def __init__(
        self,
        *,
        result: google.protobuf.empty_pb2.Empty | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___SetManifestResponse = SetManifestResponse

@typing.final
class DeleteManifestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EMPTY_FIELD_NUMBER: builtins.int
    @property
    def empty(self) -> google.protobuf.empty_pb2.Empty:
        """empty request"""

    def __init__(
        self,
        *,
        empty: google.protobuf.empty_pb2.Empty | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["empty", b"empty"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["empty", b"empty"]) -> None: ...

global___DeleteManifestRequest = DeleteManifestRequest

@typing.final
class DeleteManifestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.empty_pb2.Empty:
        """empty result"""

    def __init__(
        self,
        *,
        result: google.protobuf.empty_pb2.Empty | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___DeleteManifestResponse = DeleteManifestResponse

@typing.final
class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATED_AT_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    etag: builtins.str
    """object instance etag"""
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """last updated timestamp (UTC)"""

    def __init__(
        self,
        *,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        etag: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["etag", b"etag", "updated_at", b"updated_at"]) -> None: ...

global___Metadata = Metadata

@typing.final
class Body(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """manifest content"""
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data"]) -> None: ...

global___Body = Body
