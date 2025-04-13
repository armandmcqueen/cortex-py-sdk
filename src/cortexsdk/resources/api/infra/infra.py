# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .apikey import (
    ApikeyResource,
    AsyncApikeyResource,
    ApikeyResourceWithRawResponse,
    AsyncApikeyResourceWithRawResponse,
    ApikeyResourceWithStreamingResponse,
    AsyncApikeyResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .locked_room import (
    LockedRoomResource,
    AsyncLockedRoomResource,
    LockedRoomResourceWithRawResponse,
    AsyncLockedRoomResourceWithRawResponse,
    LockedRoomResourceWithStreamingResponse,
    AsyncLockedRoomResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InfraResource", "AsyncInfraResource"]


class InfraResource(SyncAPIResource):
    @cached_property
    def locked_room(self) -> LockedRoomResource:
        return LockedRoomResource(self._client)

    @cached_property
    def apikey(self) -> ApikeyResource:
        return ApikeyResource(self._client)

    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> InfraResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#accessing-raw-response-data-eg-headers
        """
        return InfraResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfraResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#with_streaming_response
        """
        return InfraResourceWithStreamingResponse(self)


class AsyncInfraResource(AsyncAPIResource):
    @cached_property
    def locked_room(self) -> AsyncLockedRoomResource:
        return AsyncLockedRoomResource(self._client)

    @cached_property
    def apikey(self) -> AsyncApikeyResource:
        return AsyncApikeyResource(self._client)

    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInfraResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfraResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfraResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#with_streaming_response
        """
        return AsyncInfraResourceWithStreamingResponse(self)


class InfraResourceWithRawResponse:
    def __init__(self, infra: InfraResource) -> None:
        self._infra = infra

    @cached_property
    def locked_room(self) -> LockedRoomResourceWithRawResponse:
        return LockedRoomResourceWithRawResponse(self._infra.locked_room)

    @cached_property
    def apikey(self) -> ApikeyResourceWithRawResponse:
        return ApikeyResourceWithRawResponse(self._infra.apikey)

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._infra.user)


class AsyncInfraResourceWithRawResponse:
    def __init__(self, infra: AsyncInfraResource) -> None:
        self._infra = infra

    @cached_property
    def locked_room(self) -> AsyncLockedRoomResourceWithRawResponse:
        return AsyncLockedRoomResourceWithRawResponse(self._infra.locked_room)

    @cached_property
    def apikey(self) -> AsyncApikeyResourceWithRawResponse:
        return AsyncApikeyResourceWithRawResponse(self._infra.apikey)

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._infra.user)


class InfraResourceWithStreamingResponse:
    def __init__(self, infra: InfraResource) -> None:
        self._infra = infra

    @cached_property
    def locked_room(self) -> LockedRoomResourceWithStreamingResponse:
        return LockedRoomResourceWithStreamingResponse(self._infra.locked_room)

    @cached_property
    def apikey(self) -> ApikeyResourceWithStreamingResponse:
        return ApikeyResourceWithStreamingResponse(self._infra.apikey)

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._infra.user)


class AsyncInfraResourceWithStreamingResponse:
    def __init__(self, infra: AsyncInfraResource) -> None:
        self._infra = infra

    @cached_property
    def locked_room(self) -> AsyncLockedRoomResourceWithStreamingResponse:
        return AsyncLockedRoomResourceWithStreamingResponse(self._infra.locked_room)

    @cached_property
    def apikey(self) -> AsyncApikeyResourceWithStreamingResponse:
        return AsyncApikeyResourceWithStreamingResponse(self._infra.apikey)

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._infra.user)
