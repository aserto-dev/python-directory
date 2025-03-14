# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aserto.directory.importer.v3 import importer_pb2 as aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2


class ImporterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Import = channel.stream_stream(
                '/aserto.directory.importer.v3.Importer/Import',
                request_serializer=aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2.ImportRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2.ImportResponse.FromString,
                _registered_method=True)


class ImporterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Import(self, request_iterator, context):
        """import stream of objects and relations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImporterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Import': grpc.stream_stream_rpc_method_handler(
                    servicer.Import,
                    request_deserializer=aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2.ImportRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2.ImportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aserto.directory.importer.v3.Importer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('aserto.directory.importer.v3.Importer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Importer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Import(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/aserto.directory.importer.v3.Importer/Import',
            aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2.ImportRequest.SerializeToString,
            aserto_dot_directory_dot_importer_dot_v3_dot_importer__pb2.ImportResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
