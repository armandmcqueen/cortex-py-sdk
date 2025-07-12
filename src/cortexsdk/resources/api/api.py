# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ... import _resource
from .books import (
    BooksResource,
    AsyncBooksResource,
    BooksResourceWithRawResponse,
    AsyncBooksResourceWithRawResponse,
    BooksResourceWithStreamingResponse,
    AsyncBooksResourceWithStreamingResponse,
)
from .public import (
    PublicResource,
    AsyncPublicResource,
    PublicResourceWithRawResponse,
    AsyncPublicResourceWithRawResponse,
    PublicResourceWithStreamingResponse,
    AsyncPublicResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .experiments import (
    ExperimentsResource,
    AsyncExperimentsResource,
    ExperimentsResourceWithRawResponse,
    AsyncExperimentsResourceWithRawResponse,
    ExperimentsResourceWithStreamingResponse,
    AsyncExperimentsResourceWithStreamingResponse,
)
from .infra.infra import (
    InfraResource,
    AsyncInfraResource,
    InfraResourceWithRawResponse,
    AsyncInfraResourceWithRawResponse,
    InfraResourceWithStreamingResponse,
    AsyncInfraResourceWithStreamingResponse,
)

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(_resource.SyncAPIResource):
    @cached_property
    def infra(self) -> InfraResource:
        return InfraResource(self._client)

    @cached_property
    def experiments(self) -> ExperimentsResource:
        return ExperimentsResource(self._client)

    @cached_property
    def public(self) -> PublicResource:
        return PublicResource(self._client)

    @cached_property
    def books(self) -> BooksResource:
        return BooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)


class AsyncAPIResource(_resource.AsyncAPIResource):
    @cached_property
    def infra(self) -> AsyncInfraResource:
        return AsyncInfraResource(self._client)

    @cached_property
    def experiments(self) -> AsyncExperimentsResource:
        return AsyncExperimentsResource(self._client)

    @cached_property
    def public(self) -> AsyncPublicResource:
        return AsyncPublicResource(self._client)

    @cached_property
    def books(self) -> AsyncBooksResource:
        return AsyncBooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def infra(self) -> InfraResourceWithRawResponse:
        return InfraResourceWithRawResponse(self._api.infra)

    @cached_property
    def experiments(self) -> ExperimentsResourceWithRawResponse:
        return ExperimentsResourceWithRawResponse(self._api.experiments)

    @cached_property
    def public(self) -> PublicResourceWithRawResponse:
        return PublicResourceWithRawResponse(self._api.public)

    @cached_property
    def books(self) -> BooksResourceWithRawResponse:
        return BooksResourceWithRawResponse(self._api.books)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def infra(self) -> AsyncInfraResourceWithRawResponse:
        return AsyncInfraResourceWithRawResponse(self._api.infra)

    @cached_property
    def experiments(self) -> AsyncExperimentsResourceWithRawResponse:
        return AsyncExperimentsResourceWithRawResponse(self._api.experiments)

    @cached_property
    def public(self) -> AsyncPublicResourceWithRawResponse:
        return AsyncPublicResourceWithRawResponse(self._api.public)

    @cached_property
    def books(self) -> AsyncBooksResourceWithRawResponse:
        return AsyncBooksResourceWithRawResponse(self._api.books)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def infra(self) -> InfraResourceWithStreamingResponse:
        return InfraResourceWithStreamingResponse(self._api.infra)

    @cached_property
    def experiments(self) -> ExperimentsResourceWithStreamingResponse:
        return ExperimentsResourceWithStreamingResponse(self._api.experiments)

    @cached_property
    def public(self) -> PublicResourceWithStreamingResponse:
        return PublicResourceWithStreamingResponse(self._api.public)

    @cached_property
    def books(self) -> BooksResourceWithStreamingResponse:
        return BooksResourceWithStreamingResponse(self._api.books)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def infra(self) -> AsyncInfraResourceWithStreamingResponse:
        return AsyncInfraResourceWithStreamingResponse(self._api.infra)

    @cached_property
    def experiments(self) -> AsyncExperimentsResourceWithStreamingResponse:
        return AsyncExperimentsResourceWithStreamingResponse(self._api.experiments)

    @cached_property
    def public(self) -> AsyncPublicResourceWithStreamingResponse:
        return AsyncPublicResourceWithStreamingResponse(self._api.public)

    @cached_property
    def books(self) -> AsyncBooksResourceWithStreamingResponse:
        return AsyncBooksResourceWithStreamingResponse(self._api.books)
