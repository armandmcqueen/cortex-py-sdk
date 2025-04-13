# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["ApikeyCreateResponse"]


class ApikeyCreateResponse(BaseModel):
    token: str

    description: str

    user_id: str
