# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import book_upload_epub_params
from ..._base_client import make_request_options

__all__ = ["BooksResource", "AsyncBooksResource"]


class BooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#accessing-raw-response-data-eg-headers
        """
        return BooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#with_streaming_response
        """
        return BooksResourceWithStreamingResponse(self)

    def upload_epub(
        self,
        *,
        file: FileTypes,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Upload an epub file to object storage and save metadata to database.

        - Accepts multipart/form-data with the epub file and metadata
        - Returns the ID and storage URL of the uploaded file

        Name should be in the form: "some_book_name.epub"

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/books/epub/upload",
            body=maybe_transform(body, book_upload_epub_params.BookUploadEpubParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncBooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/armandmcqueen/cortex-py-sdk#with_streaming_response
        """
        return AsyncBooksResourceWithStreamingResponse(self)

    async def upload_epub(
        self,
        *,
        file: FileTypes,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Upload an epub file to object storage and save metadata to database.

        - Accepts multipart/form-data with the epub file and metadata
        - Returns the ID and storage URL of the uploaded file

        Name should be in the form: "some_book_name.epub"

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/books/epub/upload",
            body=await async_maybe_transform(body, book_upload_epub_params.BookUploadEpubParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class BooksResourceWithRawResponse:
    def __init__(self, books: BooksResource) -> None:
        self._books = books

        self.upload_epub = to_raw_response_wrapper(
            books.upload_epub,
        )


class AsyncBooksResourceWithRawResponse:
    def __init__(self, books: AsyncBooksResource) -> None:
        self._books = books

        self.upload_epub = async_to_raw_response_wrapper(
            books.upload_epub,
        )


class BooksResourceWithStreamingResponse:
    def __init__(self, books: BooksResource) -> None:
        self._books = books

        self.upload_epub = to_streamed_response_wrapper(
            books.upload_epub,
        )


class AsyncBooksResourceWithStreamingResponse:
    def __init__(self, books: AsyncBooksResource) -> None:
        self._books = books

        self.upload_epub = async_to_streamed_response_wrapper(
            books.upload_epub,
        )
