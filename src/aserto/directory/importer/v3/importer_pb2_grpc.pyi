"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import aserto.directory.importer.v3.importer_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class ImporterStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Import: grpc.StreamStreamMultiCallable[
        aserto.directory.importer.v3.importer_pb2.ImportRequest,
        aserto.directory.importer.v3.importer_pb2.ImportResponse,
    ]

class ImporterAsyncStub:
    Import: grpc.aio.StreamStreamMultiCallable[
        aserto.directory.importer.v3.importer_pb2.ImportRequest,
        aserto.directory.importer.v3.importer_pb2.ImportResponse,
    ]

class ImporterServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Import(
        self,
        request_iterator: _MaybeAsyncIterator[aserto.directory.importer.v3.importer_pb2.ImportRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[aserto.directory.importer.v3.importer_pb2.ImportResponse], collections.abc.AsyncIterator[aserto.directory.importer.v3.importer_pb2.ImportResponse]]: ...

def add_ImporterServicer_to_server(servicer: ImporterServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
