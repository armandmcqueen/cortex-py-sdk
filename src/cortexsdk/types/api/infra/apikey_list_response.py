# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .user import User
from ...._models import BaseModel

__all__ = ["ApikeyListResponse", "ApikeyListResponseItem"]


class ApikeyListResponseItem(BaseModel):
    token: str

    description: str

    user: User


ApikeyListResponse: TypeAlias = List[ApikeyListResponseItem]
