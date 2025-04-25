from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.restaurant.restaurant import RestaurantBaseResponse
from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class RestaurantSocialMediaDetailResponse(CamelModel, TimestampDto):
    id: int
    type: SocialMediaType
    url: str
    restaurant: Optional[RestaurantBaseResponse]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
