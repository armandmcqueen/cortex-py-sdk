# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    description: str

    name: str

    user_id: str

    is_admin: Optional[bool] = None
