"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import aserto.directory.reader.v3.reader_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ReaderStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetObject: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetObjectRequest,
        aserto.directory.reader.v3.reader_pb2.GetObjectResponse,
    ]
    """get object"""

    GetObjectMany: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetObjectManyRequest,
        aserto.directory.reader.v3.reader_pb2.GetObjectManyResponse,
    ]
    """get multiple objects"""

    GetObjects: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetObjectsRequest,
        aserto.directory.reader.v3.reader_pb2.GetObjectsResponse,
    ]
    """list objects"""

    GetRelation: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetRelationRequest,
        aserto.directory.reader.v3.reader_pb2.GetRelationResponse,
    ]
    """get relation"""

    GetRelations: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetRelationsRequest,
        aserto.directory.reader.v3.reader_pb2.GetRelationsResponse,
    ]
    """list relations"""

    Check: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.CheckRequest,
        aserto.directory.reader.v3.reader_pb2.CheckResponse,
    ]
    """check if subject has relation or permission with object"""

    CheckPermission: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.CheckPermissionRequest,
        aserto.directory.reader.v3.reader_pb2.CheckPermissionResponse,
    ]
    """check permission (deprecated, use the check method)
    Deprecated: use directory.v3.Check()
    """

    CheckRelation: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.CheckRelationRequest,
        aserto.directory.reader.v3.reader_pb2.CheckRelationResponse,
    ]
    """check relation (deprecated, use the check method)
    Deprecated: use directory.v3.Check()
    """

    GetGraph: grpc.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetGraphRequest,
        aserto.directory.reader.v3.reader_pb2.GetGraphResponse,
    ]
    """get object relationship graph"""

class ReaderAsyncStub:
    GetObject: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetObjectRequest,
        aserto.directory.reader.v3.reader_pb2.GetObjectResponse,
    ]
    """get object"""

    GetObjectMany: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetObjectManyRequest,
        aserto.directory.reader.v3.reader_pb2.GetObjectManyResponse,
    ]
    """get multiple objects"""

    GetObjects: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetObjectsRequest,
        aserto.directory.reader.v3.reader_pb2.GetObjectsResponse,
    ]
    """list objects"""

    GetRelation: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetRelationRequest,
        aserto.directory.reader.v3.reader_pb2.GetRelationResponse,
    ]
    """get relation"""

    GetRelations: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetRelationsRequest,
        aserto.directory.reader.v3.reader_pb2.GetRelationsResponse,
    ]
    """list relations"""

    Check: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.CheckRequest,
        aserto.directory.reader.v3.reader_pb2.CheckResponse,
    ]
    """check if subject has relation or permission with object"""

    CheckPermission: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.CheckPermissionRequest,
        aserto.directory.reader.v3.reader_pb2.CheckPermissionResponse,
    ]
    """check permission (deprecated, use the check method)
    Deprecated: use directory.v3.Check()
    """

    CheckRelation: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.CheckRelationRequest,
        aserto.directory.reader.v3.reader_pb2.CheckRelationResponse,
    ]
    """check relation (deprecated, use the check method)
    Deprecated: use directory.v3.Check()
    """

    GetGraph: grpc.aio.UnaryUnaryMultiCallable[
        aserto.directory.reader.v3.reader_pb2.GetGraphRequest,
        aserto.directory.reader.v3.reader_pb2.GetGraphResponse,
    ]
    """get object relationship graph"""

class ReaderServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetObject(
        self,
        request: aserto.directory.reader.v3.reader_pb2.GetObjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.GetObjectResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.GetObjectResponse]]:
        """get object"""

    @abc.abstractmethod
    def GetObjectMany(
        self,
        request: aserto.directory.reader.v3.reader_pb2.GetObjectManyRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.GetObjectManyResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.GetObjectManyResponse]]:
        """get multiple objects"""

    @abc.abstractmethod
    def GetObjects(
        self,
        request: aserto.directory.reader.v3.reader_pb2.GetObjectsRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.GetObjectsResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.GetObjectsResponse]]:
        """list objects"""

    @abc.abstractmethod
    def GetRelation(
        self,
        request: aserto.directory.reader.v3.reader_pb2.GetRelationRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.GetRelationResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.GetRelationResponse]]:
        """get relation"""

    @abc.abstractmethod
    def GetRelations(
        self,
        request: aserto.directory.reader.v3.reader_pb2.GetRelationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.GetRelationsResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.GetRelationsResponse]]:
        """list relations"""

    @abc.abstractmethod
    def Check(
        self,
        request: aserto.directory.reader.v3.reader_pb2.CheckRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.CheckResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.CheckResponse]]:
        """check if subject has relation or permission with object"""

    @abc.abstractmethod
    def CheckPermission(
        self,
        request: aserto.directory.reader.v3.reader_pb2.CheckPermissionRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.CheckPermissionResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.CheckPermissionResponse]]:
        """check permission (deprecated, use the check method)
        Deprecated: use directory.v3.Check()
        """

    @abc.abstractmethod
    def CheckRelation(
        self,
        request: aserto.directory.reader.v3.reader_pb2.CheckRelationRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.CheckRelationResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.CheckRelationResponse]]:
        """check relation (deprecated, use the check method)
        Deprecated: use directory.v3.Check()
        """

    @abc.abstractmethod
    def GetGraph(
        self,
        request: aserto.directory.reader.v3.reader_pb2.GetGraphRequest,
        context: _ServicerContext,
    ) -> typing.Union[aserto.directory.reader.v3.reader_pb2.GetGraphResponse, collections.abc.Awaitable[aserto.directory.reader.v3.reader_pb2.GetGraphResponse]]:
        """get object relationship graph"""

def add_ReaderServicer_to_server(servicer: ReaderServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
