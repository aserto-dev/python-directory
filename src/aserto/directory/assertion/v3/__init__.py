# This file is generated by init_gen.py. Do not edit.

from typing import TYPE_CHECKING

from aserto.directory.assertion.v3.assertion_pb2_grpc import (
    AssertionStub,
    AssertionServicer,
)

if TYPE_CHECKING:
    from aserto.directory.assertion.v3.assertion_pb2_grpc import (
        AssertionAsyncStub,
    )

from aserto.directory.assertion.v3.assertion_pb2 import (
    GetAssertionRequest,
    GetAssertionResponse,
    ListAssertionsRequest,
    ListAssertionsResponse,
    SetAssertionRequest,
    SetAssertionResponse,
    DeleteAssertionRequest,
    DeleteAssertionResponse,
    Assert,
)

__all__ = [
    "AssertionStub",
    "AssertionServicer",
    "GetAssertionRequest",
    "GetAssertionResponse",
    "ListAssertionsRequest",
    "ListAssertionsResponse",
    "SetAssertionRequest",
    "SetAssertionResponse",
    "DeleteAssertionRequest",
    "DeleteAssertionResponse",
    "Assert",
]
