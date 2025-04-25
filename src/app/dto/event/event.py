from datetime import date, time
from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.dto.event.event_social_media import EventSocialMediaBaseResponse
from src.app.dto.landmark.landmark_base_response import LandmarkBaseResponse
from src.app.dto.timestamp import TimestampDto


class EventBase(CamelModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]
    date: Optional[date]
    time: Optional[time]

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class EventPostRequest(EventBase):
    city_id: Optional[int]
    landmark_id: Optional[int]


class EventPutRequest(EventBase):
    id: int
    city_id: Optional[int]
    landmark_id: Optional[int]


class EventBaseResponse(EventBase, TimestampDto):
    id: int
    city_id: Optional[int]
    landmark_id: Optional[int]

    class Config:
        from_attributes = True


class EventDetailResponse(EventBase, TimestampDto):
    id: int
    city: Optional[CityBaseResponse]
    landmark: Optional[LandmarkBaseResponse]
    social_medias: Optional[list[EventSocialMediaBaseResponse]]

    class Config:
        from_attributes = True
