from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.dto.landmark.landmark_base_response import LandmarkBaseResponse
from src.app.dto.restaurant.restaurant_social_media import RestaurantSocialMediaBaseResponse
from src.app.dto.timestamp import TimestampDto


class RestaurantBase(CamelModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]
    menu_url: Optional[str]


class RestaurantPostRequest(RestaurantBase):
    city_id: Optional[int]
    landmark_id: Optional[int]


class RestaurantPutRequest(RestaurantBase):
    id: int
    city_id: Optional[int]
    landmark_id: Optional[int]


class RestaurantBaseResponse(RestaurantBase, TimestampDto):
    id: int
    city_id: Optional[int]
    landmark_id: Optional[int]

    class Config:
        from_attributes = True


class RestaurantDetailResponse(RestaurantBase, TimestampDto):
    id: int
    city: Optional[CityBaseResponse]
    landmark: Optional[LandmarkBaseResponse]
    social_medias: Optional[list[RestaurantSocialMediaBaseResponse]]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
