from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto


class LandmarkBaseResponse(CamelModel, TimestampDto):
    id: int
    name: str
    description: str
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]
    city_id: Optional[int]

    class Config:
        from_attributes = True
