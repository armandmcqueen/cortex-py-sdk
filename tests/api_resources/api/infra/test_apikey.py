# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cortex_py_sdk import Cortex, AsyncCortex
from cortex_py_sdk.types.api.infra import ApikeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApikey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cortex) -> None:
        apikey = client.api.infra.apikey.create(
            description="description",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApikeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cortex) -> None:
        response = client.api.infra.apikey.with_raw_response.create(
            description="description",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = response.parse()
        assert_matches_type(ApikeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cortex) -> None:
        with client.api.infra.apikey.with_streaming_response.create(
            description="description",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = response.parse()
            assert_matches_type(ApikeyCreateResponse, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cortex) -> None:
        apikey = client.api.infra.apikey.delete(
            "token",
        )
        assert_matches_type(object, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cortex) -> None:
        response = client.api.infra.apikey.with_raw_response.delete(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = response.parse()
        assert_matches_type(object, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cortex) -> None:
        with client.api.infra.apikey.with_streaming_response.delete(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = response.parse()
            assert_matches_type(object, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cortex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.api.infra.apikey.with_raw_response.delete(
                "",
            )


class TestAsyncApikey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCortex) -> None:
        apikey = await async_client.api.infra.apikey.create(
            description="description",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApikeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.infra.apikey.with_raw_response.create(
            description="description",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = await response.parse()
        assert_matches_type(ApikeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCortex) -> None:
        async with async_client.api.infra.apikey.with_streaming_response.create(
            description="description",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = await response.parse()
            assert_matches_type(ApikeyCreateResponse, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCortex) -> None:
        apikey = await async_client.api.infra.apikey.delete(
            "token",
        )
        assert_matches_type(object, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCortex) -> None:
        response = await async_client.api.infra.apikey.with_raw_response.delete(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = await response.parse()
        assert_matches_type(object, apikey, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCortex) -> None:
        async with async_client.api.infra.apikey.with_streaming_response.delete(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = await response.parse()
            assert_matches_type(object, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCortex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.api.infra.apikey.with_raw_response.delete(
                "",
            )
