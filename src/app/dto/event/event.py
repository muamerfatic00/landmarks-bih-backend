from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto


class EventBase(CamelModel, TimestampDto):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]
    date: Optional[datetime.date]
    time: Optional[datetime.time]
    city_id: Optional[int]
    landmark_id: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True



class EventBaseResponse(EventBase):
    id: int
