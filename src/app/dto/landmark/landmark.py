from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.accommodation.accommodation import AccommodationBaseResponse
from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.dto.event.event import EventBaseResponse
from src.app.dto.restaurant.restaurant import RestaurantBaseResponse
from src.app.dto.timestamp import TimestampDto


class LandmarkBase(CamelModel):
    name: str
    description: str
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class LandmarkPostRequest(LandmarkBase):
    city_id: Optional[int]


class LandmarkPutRequest(LandmarkBase):
    id: int
    city_id: Optional[int]


class LandmarkDetailResponse(LandmarkBase, TimestampDto):
    id: int
    city: Optional[CityBaseResponse]
    accommodations: Optional[list[AccommodationBaseResponse]]
    events: Optional[list[EventBaseResponse]]
    restaurants: Optional[list[RestaurantBaseResponse]]
