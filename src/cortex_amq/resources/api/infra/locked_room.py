# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["LockedRoomResource", "AsyncLockedRoomResource"]


class LockedRoomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockedRoomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#accessing-raw-response-data-eg-headers
        """
        return LockedRoomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockedRoomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#with_streaming_response
        """
        return LockedRoomResourceWithStreamingResponse(self)

    def retrieve_admin(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Locked Admin Room"""
        return self._get(
            "/api/infra/locked-room/admin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Locked User Room"""
        return self._get(
            "/api/infra/locked-room/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncLockedRoomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockedRoomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLockedRoomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockedRoomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cortex-amq-python#with_streaming_response
        """
        return AsyncLockedRoomResourceWithStreamingResponse(self)

    async def retrieve_admin(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Locked Admin Room"""
        return await self._get(
            "/api/infra/locked-room/admin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Locked User Room"""
        return await self._get(
            "/api/infra/locked-room/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class LockedRoomResourceWithRawResponse:
    def __init__(self, locked_room: LockedRoomResource) -> None:
        self._locked_room = locked_room

        self.retrieve_admin = to_raw_response_wrapper(
            locked_room.retrieve_admin,
        )
        self.retrieve_user = to_raw_response_wrapper(
            locked_room.retrieve_user,
        )


class AsyncLockedRoomResourceWithRawResponse:
    def __init__(self, locked_room: AsyncLockedRoomResource) -> None:
        self._locked_room = locked_room

        self.retrieve_admin = async_to_raw_response_wrapper(
            locked_room.retrieve_admin,
        )
        self.retrieve_user = async_to_raw_response_wrapper(
            locked_room.retrieve_user,
        )


class LockedRoomResourceWithStreamingResponse:
    def __init__(self, locked_room: LockedRoomResource) -> None:
        self._locked_room = locked_room

        self.retrieve_admin = to_streamed_response_wrapper(
            locked_room.retrieve_admin,
        )
        self.retrieve_user = to_streamed_response_wrapper(
            locked_room.retrieve_user,
        )


class AsyncLockedRoomResourceWithStreamingResponse:
    def __init__(self, locked_room: AsyncLockedRoomResource) -> None:
        self._locked_room = locked_room

        self.retrieve_admin = async_to_streamed_response_wrapper(
            locked_room.retrieve_admin,
        )
        self.retrieve_user = async_to_streamed_response_wrapper(
            locked_room.retrieve_user,
        )
