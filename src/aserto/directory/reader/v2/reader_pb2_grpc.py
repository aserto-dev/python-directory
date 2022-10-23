# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aserto.directory.reader.v2 import reader_pb2 as aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2


class ReaderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetObjectType = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetObjectType',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypeRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypeResponse.FromString,
                )
        self.GetObjectTypes = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetObjectTypes',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypesRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypesResponse.FromString,
                )
        self.GetRelationType = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetRelationType',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypeRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypeResponse.FromString,
                )
        self.GetRelationTypes = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetRelationTypes',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypesRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypesResponse.FromString,
                )
        self.GetPermission = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetPermission',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionResponse.FromString,
                )
        self.GetPermissions = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetPermissions',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionsRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionsResponse.FromString,
                )
        self.GetObject = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetObject',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectResponse.FromString,
                )
        self.GetObjectMany = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetObjectMany',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectManyRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectManyResponse.FromString,
                )
        self.GetObjects = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetObjects',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectsRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectsResponse.FromString,
                )
        self.GetRelation = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetRelation',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationResponse.FromString,
                )
        self.GetRelations = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetRelations',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationsRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationsResponse.FromString,
                )
        self.CheckPermission = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/CheckPermission',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckPermissionRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckPermissionResponse.FromString,
                )
        self.CheckRelation = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/CheckRelation',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckRelationRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckRelationResponse.FromString,
                )
        self.GetGraph = channel.unary_unary(
                '/aserto.directory.reader.v2.Reader/GetGraph',
                request_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetGraphRequest.SerializeToString,
                response_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetGraphResponse.FromString,
                )


class ReaderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetObjectType(self, request, context):
        """object type metadata methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelationType(self, request, context):
        """relation type metadata methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelationTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPermission(self, request, context):
        """permission metadata methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPermissions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObject(self, request, context):
        """object methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelation(self, request, context):
        """relation methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckPermission(self, request, context):
        """check methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckRelation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGraph(self, request, context):
        """graph methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReaderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetObjectType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectType,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypeRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypeResponse.SerializeToString,
            ),
            'GetObjectTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectTypes,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypesRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypesResponse.SerializeToString,
            ),
            'GetRelationType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRelationType,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypeRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypeResponse.SerializeToString,
            ),
            'GetRelationTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRelationTypes,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypesRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypesResponse.SerializeToString,
            ),
            'GetPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPermission,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionResponse.SerializeToString,
            ),
            'GetPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPermissions,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionsRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionsResponse.SerializeToString,
            ),
            'GetObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObject,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectResponse.SerializeToString,
            ),
            'GetObjectMany': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectMany,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectManyRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectManyResponse.SerializeToString,
            ),
            'GetObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjects,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectsRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectsResponse.SerializeToString,
            ),
            'GetRelation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRelation,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationResponse.SerializeToString,
            ),
            'GetRelations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRelations,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationsRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationsResponse.SerializeToString,
            ),
            'CheckPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckPermission,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckPermissionRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckPermissionResponse.SerializeToString,
            ),
            'CheckRelation': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckRelation,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckRelationRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckRelationResponse.SerializeToString,
            ),
            'GetGraph': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGraph,
                    request_deserializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetGraphRequest.FromString,
                    response_serializer=aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetGraphResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aserto.directory.reader.v2.Reader', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reader(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetObjectType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetObjectType',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypeRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetObjectTypes',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypesRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRelationType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetRelationType',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypeRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRelationTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetRelationTypes',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypesRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetPermission',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetPermissions',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionsRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetPermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetObject',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetObjectMany',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectManyRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectManyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetObjects',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectsRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetObjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRelation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetRelation',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRelations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetRelations',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationsRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetRelationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/CheckPermission',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckPermissionRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckPermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckRelation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/CheckRelation',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckRelationRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.CheckRelationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGraph(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aserto.directory.reader.v2.Reader/GetGraph',
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetGraphRequest.SerializeToString,
            aserto_dot_directory_dot_reader_dot_v2_dot_reader__pb2.GetGraphResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
