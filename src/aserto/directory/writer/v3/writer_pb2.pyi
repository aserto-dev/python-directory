"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import aserto.directory.common.v3.common_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SetObjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_FIELD_NUMBER: builtins.int
    @property
    def object(self) -> aserto.directory.common.v3.common_pb2.Object:
        """object instance"""

    def __init__(
        self,
        *,
        object: aserto.directory.common.v3.common_pb2.Object | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["object", b"object"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["object", b"object"]) -> None: ...

global___SetObjectRequest = SetObjectRequest

@typing.final
class SetObjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> aserto.directory.common.v3.common_pb2.Object:
        """object instance"""

    def __init__(
        self,
        *,
        result: aserto.directory.common.v3.common_pb2.Object | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___SetObjectResponse = SetObjectResponse

@typing.final
class DeleteObjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    WITH_RELATIONS_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    with_relations: builtins.bool
    """delete object relations, both object and subject relations."""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        with_relations: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["object_id", b"object_id", "object_type", b"object_type", "with_relations", b"with_relations"]) -> None: ...

global___DeleteObjectRequest = DeleteObjectRequest

@typing.final
class DeleteObjectResponse(google.protobuf.message.Message):
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

global___DeleteObjectResponse = DeleteObjectResponse

@typing.final
class SetRelationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RELATION_FIELD_NUMBER: builtins.int
    @property
    def relation(self) -> aserto.directory.common.v3.common_pb2.Relation:
        """relation instance"""

    def __init__(
        self,
        *,
        relation: aserto.directory.common.v3.common_pb2.Relation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["relation", b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["relation", b"relation"]) -> None: ...

global___SetRelationRequest = SetRelationRequest

@typing.final
class SetRelationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> aserto.directory.common.v3.common_pb2.Relation:
        """relation instance"""

    def __init__(
        self,
        *,
        result: aserto.directory.common.v3.common_pb2.Relation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___SetRelationResponse = SetRelationResponse

@typing.final
class DeleteRelationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    relation: builtins.str
    """object relation name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    subject_relation: builtins.str
    """optional subject relation name"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        relation: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        subject_relation: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["object_id", b"object_id", "object_type", b"object_type", "relation", b"relation", "subject_id", b"subject_id", "subject_relation", b"subject_relation", "subject_type", b"subject_type"]) -> None: ...

global___DeleteRelationRequest = DeleteRelationRequest

@typing.final
class DeleteRelationResponse(google.protobuf.message.Message):
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

global___DeleteRelationResponse = DeleteRelationResponse
