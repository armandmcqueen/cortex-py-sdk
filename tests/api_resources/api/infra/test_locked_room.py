# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cortexsdk import Cortex, AsyncCortex
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockedRoom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_admin_room(self, client: Cortex) -> None:
        locked_room = client.api.infra.locked_room.admin_room()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_admin_room(self, client: Cortex) -> None:
        response = client.api.infra.locked_room.with_raw_response.admin_room()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_admin_room(self, client: Cortex) -> None:
        with client.api.infra.locked_room.with_streaming_response.admin_room() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_user_room(self, client: Cortex) -> None:
        locked_room = client.api.infra.locked_room.user_room()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_room(self, client: Cortex) -> None:
        response = client.api.infra.locked_room.with_raw_response.user_room()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_room(self, client: Cortex) -> None:
        with client.api.infra.locked_room.with_streaming_response.user_room() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLockedRoom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_admin_room(self, async_client: AsyncCortex) -> None:
        locked_room = await async_client.api.infra.locked_room.admin_room()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_admin_room(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.infra.locked_room.with_raw_response.admin_room()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = await response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_admin_room(self, async_client: AsyncCortex) -> None:
        async with async_client.api.infra.locked_room.with_streaming_response.admin_room() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = await response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_room(self, async_client: AsyncCortex) -> None:
        locked_room = await async_client.api.infra.locked_room.user_room()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_room(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.infra.locked_room.with_raw_response.user_room()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locked_room = await response.parse()
        assert_matches_type(object, locked_room, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_room(self, async_client: AsyncCortex) -> None:
        async with async_client.api.infra.locked_room.with_streaming_response.user_room() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locked_room = await response.parse()
            assert_matches_type(object, locked_room, path=["response"])

        assert cast(Any, response.is_closed) is True
