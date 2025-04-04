"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GroupProperties(google.protobuf.message.Message):
    """Properties of "group" objects."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_ID_FIELD_NUMBER: builtins.int
    connection_id: builtins.str
    """ID of the IDP connection the group instance is associated with."""
    def __init__(
        self,
        *,
        connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connection_id", b"connection_id"]) -> None: ...

global___GroupProperties = GroupProperties
