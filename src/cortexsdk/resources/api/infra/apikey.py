# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.infra import apikey_create_params
from ....types.api.infra.apikey_list_response import ApikeyListResponse
from ....types.api.infra.apikey_create_response import ApikeyCreateResponse

__all__ = ["ApikeyResource", "AsyncApikeyResource"]


class ApikeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApikeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#accessing-raw-response-data-eg-headers
        """
        return ApikeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApikeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#with_streaming_response
        """
        return ApikeyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApikeyCreateResponse:
        """
        Create Api Key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/infra/apikey",
            body=maybe_transform(
                {
                    "description": description,
                    "user_id": user_id,
                },
                apikey_create_params.ApikeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApikeyCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApikeyListResponse:
        """List Api Keys"""
        return self._get(
            "/api/infra/apikey",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApikeyListResponse,
        )

    def delete(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Api Key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._delete(
            f"/api/infra/apikey/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncApikeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApikeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncApikeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApikeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#with_streaming_response
        """
        return AsyncApikeyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApikeyCreateResponse:
        """
        Create Api Key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/infra/apikey",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "user_id": user_id,
                },
                apikey_create_params.ApikeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApikeyCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApikeyListResponse:
        """List Api Keys"""
        return await self._get(
            "/api/infra/apikey",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApikeyListResponse,
        )

    async def delete(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Api Key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._delete(
            f"/api/infra/apikey/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ApikeyResourceWithRawResponse:
    def __init__(self, apikey: ApikeyResource) -> None:
        self._apikey = apikey

        self.create = to_raw_response_wrapper(
            apikey.create,
        )
        self.list = to_raw_response_wrapper(
            apikey.list,
        )
        self.delete = to_raw_response_wrapper(
            apikey.delete,
        )


class AsyncApikeyResourceWithRawResponse:
    def __init__(self, apikey: AsyncApikeyResource) -> None:
        self._apikey = apikey

        self.create = async_to_raw_response_wrapper(
            apikey.create,
        )
        self.list = async_to_raw_response_wrapper(
            apikey.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apikey.delete,
        )


class ApikeyResourceWithStreamingResponse:
    def __init__(self, apikey: ApikeyResource) -> None:
        self._apikey = apikey

        self.create = to_streamed_response_wrapper(
            apikey.create,
        )
        self.list = to_streamed_response_wrapper(
            apikey.list,
        )
        self.delete = to_streamed_response_wrapper(
            apikey.delete,
        )


class AsyncApikeyResourceWithStreamingResponse:
    def __init__(self, apikey: AsyncApikeyResource) -> None:
        self._apikey = apikey

        self.create = async_to_streamed_response_wrapper(
            apikey.create,
        )
        self.list = async_to_streamed_response_wrapper(
            apikey.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apikey.delete,
        )
