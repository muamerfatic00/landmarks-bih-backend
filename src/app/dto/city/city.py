from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.accommodation.accommodation import AccommodationBaseResponse
from src.app.dto.event.event import EventBaseResponse
from src.app.dto.landmark.landmark_base_response import LandmarkBaseResponse
from src.app.dto.restaurant.restaurant import RestaurantBaseResponse
from src.app.dto.timestamp import TimestampDto


class CityBase(CamelModel):
    name: str
    description: str
    image_url: Optional[str]
    google_maps_url: Optional[str]


class CityPostRequest(CityBase):
    pass


class CityPutRequest(CityBase):
    id: int


class CityDetailResponse(CityBase, TimestampDto):
    id: int
    landmarks: Optional[list[LandmarkBaseResponse]]
    accommodations: Optional[list[AccommodationBaseResponse]]
    events: Optional[list[EventBaseResponse]]
    restaurants: Optional[list[RestaurantBaseResponse]]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
