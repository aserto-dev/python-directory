"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import aserto.directory.common.v3.common_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetObjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    WITH_RELATIONS_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type name (lc-string)"""
    object_id: builtins.str
    """object identifier (cs-string)"""
    with_relations: builtins.bool
    """materialize the object relations objects"""
    @property
    def page(self) -> aserto.directory.common.v3.common_pb2.PaginationRequest:
        """pagination request"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        with_relations: builtins.bool = ...,
        page: aserto.directory.common.v3.common_pb2.PaginationRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type", "page", b"page", "with_relations", b"with_relations"]) -> None: ...

global___GetObjectRequest = GetObjectRequest

@typing_extensions.final
class GetObjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    RELATIONS_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> aserto.directory.common.v3.common_pb2.Object:
        """object instance"""
    @property
    def relations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.directory.common.v3.common_pb2.Relation]:
        """object relations"""
    @property
    def page(self) -> aserto.directory.common.v3.common_pb2.PaginationResponse:
        """pagination response"""
    def __init__(
        self,
        *,
        result: aserto.directory.common.v3.common_pb2.Object | None = ...,
        relations: collections.abc.Iterable[aserto.directory.common.v3.common_pb2.Relation] | None = ...,
        page: aserto.directory.common.v3.common_pb2.PaginationResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["page", b"page", "relations", b"relations", "result", b"result"]) -> None: ...

global___GetObjectResponse = GetObjectResponse

@typing_extensions.final
class GetObjectManyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAM_FIELD_NUMBER: builtins.int
    @property
    def param(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.directory.common.v3.common_pb2.ObjectIdentifier]:
        """object identifier list"""
    def __init__(
        self,
        *,
        param: collections.abc.Iterable[aserto.directory.common.v3.common_pb2.ObjectIdentifier] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["param", b"param"]) -> None: ...

global___GetObjectManyRequest = GetObjectManyRequest

@typing_extensions.final
class GetObjectManyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.directory.common.v3.common_pb2.Object]:
        """array of object instances"""
    def __init__(
        self,
        *,
        results: collections.abc.Iterable[aserto.directory.common.v3.common_pb2.Object] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results", b"results"]) -> None: ...

global___GetObjectManyResponse = GetObjectManyResponse

@typing_extensions.final
class GetObjectsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type name (lc-string)"""
    @property
    def page(self) -> aserto.directory.common.v3.common_pb2.PaginationRequest:
        """pagination request"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        page: aserto.directory.common.v3.common_pb2.PaginationRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_type", b"object_type", "page", b"page"]) -> None: ...

global___GetObjectsRequest = GetObjectsRequest

@typing_extensions.final
class GetObjectsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULTS_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.directory.common.v3.common_pb2.Object]:
        """array of object instances"""
    @property
    def page(self) -> aserto.directory.common.v3.common_pb2.PaginationResponse:
        """pagination response"""
    def __init__(
        self,
        *,
        results: collections.abc.Iterable[aserto.directory.common.v3.common_pb2.Object] | None = ...,
        page: aserto.directory.common.v3.common_pb2.PaginationResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["page", b"page", "results", b"results"]) -> None: ...

global___GetObjectsResponse = GetObjectsResponse

@typing_extensions.final
class GetRelationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    WITH_OBJECTS_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    relation: builtins.str
    """relation name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    subject_relation: builtins.str
    """optional subject relation name"""
    with_objects: builtins.bool
    """materialize relation objects"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        relation: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        subject_relation: builtins.str = ...,
        with_objects: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type", "relation", b"relation", "subject_id", b"subject_id", "subject_relation", b"subject_relation", "subject_type", b"subject_type", "with_objects", b"with_objects"]) -> None: ...

global___GetRelationRequest = GetRelationRequest

@typing_extensions.final
class GetRelationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ObjectsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> aserto.directory.common.v3.common_pb2.Object: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: aserto.directory.common.v3.common_pb2.Object | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESULT_FIELD_NUMBER: builtins.int
    OBJECTS_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> aserto.directory.common.v3.common_pb2.Relation:
        """relation instance"""
    @property
    def objects(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, aserto.directory.common.v3.common_pb2.Object]:
        """map of materialized relation objects"""
    def __init__(
        self,
        *,
        result: aserto.directory.common.v3.common_pb2.Relation | None = ...,
        objects: collections.abc.Mapping[builtins.str, aserto.directory.common.v3.common_pb2.Object] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["objects", b"objects", "result", b"result"]) -> None: ...

global___GetRelationResponse = GetRelationResponse

@typing_extensions.final
class GetRelationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    WITH_OBJECTS_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    relation: builtins.str
    """relation name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    subject_relation: builtins.str
    """optional subject relation name"""
    with_objects: builtins.bool
    """materialize relation objects"""
    @property
    def page(self) -> aserto.directory.common.v3.common_pb2.PaginationRequest:
        """pagination request"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        relation: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        subject_relation: builtins.str = ...,
        with_objects: builtins.bool = ...,
        page: aserto.directory.common.v3.common_pb2.PaginationRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type", "page", b"page", "relation", b"relation", "subject_id", b"subject_id", "subject_relation", b"subject_relation", "subject_type", b"subject_type", "with_objects", b"with_objects"]) -> None: ...

global___GetRelationsRequest = GetRelationsRequest

@typing_extensions.final
class GetRelationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ObjectsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> aserto.directory.common.v3.common_pb2.Object: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: aserto.directory.common.v3.common_pb2.Object | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESULTS_FIELD_NUMBER: builtins.int
    OBJECTS_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.directory.common.v3.common_pb2.Relation]:
        """array of relation instances"""
    @property
    def objects(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, aserto.directory.common.v3.common_pb2.Object]:
        """map of materialized relation objects"""
    @property
    def page(self) -> aserto.directory.common.v3.common_pb2.PaginationResponse:
        """pagination response"""
    def __init__(
        self,
        *,
        results: collections.abc.Iterable[aserto.directory.common.v3.common_pb2.Relation] | None = ...,
        objects: collections.abc.Mapping[builtins.str, aserto.directory.common.v3.common_pb2.Object] | None = ...,
        page: aserto.directory.common.v3.common_pb2.PaginationResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["objects", b"objects", "page", b"page", "results", b"results"]) -> None: ...

global___GetRelationsResponse = GetRelationsResponse

@typing_extensions.final
class CheckRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    relation: builtins.str
    """relation name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    trace: builtins.bool
    """collect trace information"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        relation: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        trace: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type", "relation", b"relation", "subject_id", b"subject_id", "subject_type", b"subject_type", "trace", b"trace"]) -> None: ...

global___CheckRequest = CheckRequest

@typing_extensions.final
class CheckResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECK_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    check: builtins.bool
    """check result"""
    @property
    def trace(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """trace information"""
    def __init__(
        self,
        *,
        check: builtins.bool = ...,
        trace: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["check", b"check", "trace", b"trace"]) -> None: ...

global___CheckResponse = CheckResponse

@typing_extensions.final
class CheckPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    permission: builtins.str
    """permission name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    trace: builtins.bool
    """collect trace information"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        permission: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        trace: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type", "permission", b"permission", "subject_id", b"subject_id", "subject_type", b"subject_type", "trace", b"trace"]) -> None: ...

global___CheckPermissionRequest = CheckPermissionRequest

@typing_extensions.final
class CheckPermissionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECK_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    check: builtins.bool
    """check result"""
    @property
    def trace(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """trace information"""
    def __init__(
        self,
        *,
        check: builtins.bool = ...,
        trace: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["check", b"check", "trace", b"trace"]) -> None: ...

global___CheckPermissionResponse = CheckPermissionResponse

@typing_extensions.final
class CheckRelationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    relation: builtins.str
    """relation name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    trace: builtins.bool
    """collect trace information"""
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        relation: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        trace: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type", "relation", b"relation", "subject_id", b"subject_id", "subject_type", b"subject_type", "trace", b"trace"]) -> None: ...

global___CheckRelationRequest = CheckRelationRequest

@typing_extensions.final
class CheckRelationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECK_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    check: builtins.bool
    """check result"""
    @property
    def trace(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """trace information"""
    def __init__(
        self,
        *,
        check: builtins.bool = ...,
        trace: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["check", b"check", "trace", b"trace"]) -> None: ...

global___CheckRelationResponse = CheckRelationResponse

@typing_extensions.final
class GetGraphRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ANCHOR_TYPE_FIELD_NUMBER: builtins.int
    ANCHOR_ID_FIELD_NUMBER: builtins.int
    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    anchor_type: builtins.str
    """anchor type"""
    anchor_id: builtins.str
    """anchor identifier"""
    object_type: builtins.str
    """object type"""
    object_id: builtins.str
    """object identifier"""
    relation: builtins.str
    """relation name"""
    subject_type: builtins.str
    """subject type"""
    subject_id: builtins.str
    """subject identifier"""
    subject_relation: builtins.str
    """subject relation"""
    def __init__(
        self,
        *,
        anchor_type: builtins.str = ...,
        anchor_id: builtins.str = ...,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
        relation: builtins.str = ...,
        subject_type: builtins.str = ...,
        subject_id: builtins.str = ...,
        subject_relation: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["anchor_id", b"anchor_id", "anchor_type", b"anchor_type", "object_id", b"object_id", "object_type", b"object_type", "relation", b"relation", "subject_id", b"subject_id", "subject_relation", b"subject_relation", "subject_type", b"subject_type"]) -> None: ...

global___GetGraphRequest = GetGraphRequest

@typing_extensions.final
class GetGraphResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.directory.common.v3.common_pb2.ObjectDependency]:
        """dependency graph"""
    def __init__(
        self,
        *,
        results: collections.abc.Iterable[aserto.directory.common.v3.common_pb2.ObjectDependency] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results", b"results"]) -> None: ...

global___GetGraphResponse = GetGraphResponse
