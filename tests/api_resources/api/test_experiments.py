# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cortexsdk import Cortex, AsyncCortex
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_health_check(self, client: Cortex) -> None:
        experiment = client.api.experiments.health_check()
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_health_check(self, client: Cortex) -> None:
        response = client.api.experiments.with_raw_response.health_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_health_check(self, client: Cortex) -> None:
        with client.api.experiments.with_streaming_response.health_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(object, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExperiments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_health_check(self, async_client: AsyncCortex) -> None:
        experiment = await async_client.api.experiments.health_check()
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_health_check(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.experiments.with_raw_response.health_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_health_check(self, async_client: AsyncCortex) -> None:
        async with async_client.api.experiments.with_streaming_response.health_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(object, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True
