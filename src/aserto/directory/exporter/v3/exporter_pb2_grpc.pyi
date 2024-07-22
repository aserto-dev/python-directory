"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import aserto.directory.exporter.v3.exporter_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ExporterStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Export: grpc.UnaryStreamMultiCallable[
        aserto.directory.exporter.v3.exporter_pb2.ExportRequest,
        aserto.directory.exporter.v3.exporter_pb2.ExportResponse,
    ]
    """export objects and relations as a stream"""

class ExporterAsyncStub:
    Export: grpc.aio.UnaryStreamMultiCallable[
        aserto.directory.exporter.v3.exporter_pb2.ExportRequest,
        aserto.directory.exporter.v3.exporter_pb2.ExportResponse,
    ]
    """export objects and relations as a stream"""

class ExporterServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Export(
        self,
        request: aserto.directory.exporter.v3.exporter_pb2.ExportRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[aserto.directory.exporter.v3.exporter_pb2.ExportResponse], collections.abc.AsyncIterator[aserto.directory.exporter.v3.exporter_pb2.ExportResponse]]:
        """export objects and relations as a stream"""

def add_ExporterServicer_to_server(servicer: ExporterServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
