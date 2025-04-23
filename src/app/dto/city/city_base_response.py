from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto


class CityBaseResponse(CamelModel, TimestampDto):
    id: int
    name: str
    description: str
    image_url: Optional[str]
    google_maps_url: Optional[str]

    class Config:
        from_attributes = True
