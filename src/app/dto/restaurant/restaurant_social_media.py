from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class RestaurantSocialMediaBase(CamelModel):
    type: SocialMediaType
    url: str


class RestaurantSocialMediaPostRequest(RestaurantSocialMediaBase):
    restaurant_id: int


class RestaurantSocialMediaPutRequest(RestaurantSocialMediaBase):
    id: int
    restaurant_id: int


class RestaurantSocialMediaBaseResponse(RestaurantSocialMediaBase, TimestampDto):
    id: int
    restaurant_id: int

    class Config:
        from_attributes = True
