from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class RestaurantSocialMediaBase(CamelModel):
    type: SocialMediaType
    url: str
    restaurant_id: int


class RestaurantSocialMediaPostRequest(RestaurantSocialMediaBase):
    pass


class RestaurantSocialMediaPutRequest(RestaurantSocialMediaBase):
    id: int


class RestaurantSocialMediaBaseResponse(RestaurantSocialMediaBase, TimestampDto):
    id: int

    class Config:
        from_attributes = True
