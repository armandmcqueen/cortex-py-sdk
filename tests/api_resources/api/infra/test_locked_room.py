# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cortex_amq import CortexAmq, AsyncCortexAmq
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockedRoom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_admin(self, client: CortexAmq) -> None:
        locked_room = client.api.infra.locked_room.retrieve_admin()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_admin(self, client: CortexAmq) -> None:
        response = client.api.infra.locked_room.with_raw_response.retrieve_admin()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_admin(self, client: CortexAmq) -> None:
        with client.api.infra.locked_room.with_streaming_response.retrieve_admin() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_user(self, client: CortexAmq) -> None:
        locked_room = client.api.infra.locked_room.retrieve_user()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_user(self, client: CortexAmq) -> None:
        response = client.api.infra.locked_room.with_raw_response.retrieve_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_user(self, client: CortexAmq) -> None:
        with client.api.infra.locked_room.with_streaming_response.retrieve_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLockedRoom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_admin(self, async_client: AsyncCortexAmq) -> None:
        locked_room = await async_client.api.infra.locked_room.retrieve_admin()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_admin(self, async_client: AsyncCortexAmq) -> None:
        response = await async_client.api.infra.locked_room.with_raw_response.retrieve_admin()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = await response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_admin(self, async_client: AsyncCortexAmq) -> None:
        async with async_client.api.infra.locked_room.with_streaming_response.retrieve_admin() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = await response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_user(self, async_client: AsyncCortexAmq) -> None:
        locked_room = await async_client.api.infra.locked_room.retrieve_user()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_user(self, async_client: AsyncCortexAmq) -> None:
        response = await async_client.api.infra.locked_room.with_raw_response.retrieve_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = await response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_user(self, async_client: AsyncCortexAmq) -> None:
        async with async_client.api.infra.locked_room.with_streaming_response.retrieve_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = await response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True
