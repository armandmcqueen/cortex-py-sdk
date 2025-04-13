# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cortex_py_sdk import Cortex, AsyncCortex

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_room(self, client: Cortex) -> None:
        public = client.api.public.retrieve_room()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_room(self, client: Cortex) -> None:
        response = client.api.public.with_raw_response.retrieve_room()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public = response.parse()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_room(self, client: Cortex) -> None:
        with client.api.public.with_streaming_response.retrieve_room() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public = response.parse()
            assert_matches_type(object, public, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_whoami(self, client: Cortex) -> None:
        public = client.api.public.whoami()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_whoami(self, client: Cortex) -> None:
        response = client.api.public.with_raw_response.whoami()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public = response.parse()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_whoami(self, client: Cortex) -> None:
        with client.api.public.with_streaming_response.whoami() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public = response.parse()
            assert_matches_type(object, public, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPublic:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_room(self, async_client: AsyncCortex) -> None:
        public = await async_client.api.public.retrieve_room()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_room(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.public.with_raw_response.retrieve_room()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public = await response.parse()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_room(self, async_client: AsyncCortex) -> None:
        async with async_client.api.public.with_streaming_response.retrieve_room() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public = await response.parse()
            assert_matches_type(object, public, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_whoami(self, async_client: AsyncCortex) -> None:
        public = await async_client.api.public.whoami()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_whoami(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.public.with_raw_response.whoami()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public = await response.parse()
        assert_matches_type(object, public, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_whoami(self, async_client: AsyncCortex) -> None:
        async with async_client.api.public.with_streaming_response.whoami() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public = await response.parse()
            assert_matches_type(object, public, path=["response"])

        assert cast(Any, response.is_closed) is True
