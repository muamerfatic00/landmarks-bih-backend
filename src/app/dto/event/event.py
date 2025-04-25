from datetime import date, time
from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.dto.establishment.establishment import EstablishmentBaseCommon, EstablishmentDetailCommon
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


class EventPostRequest(EstablishmentBaseCommon, EventBase):
    pass


class EventPutRequest(EstablishmentBaseCommon, EventBase):
    id: int


class EventBaseResponse(EstablishmentBaseCommon, EventBase, TimestampDto):
    id: int


class EventDetailResponse(EventBase, EstablishmentDetailCommon, TimestampDto):
    id: int
    social_medias: Optional[list[EventSocialMediaBaseResponse]]
