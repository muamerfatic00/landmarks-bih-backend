from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto


class RestaurantBase(CamelModel, TimestampDto):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]
    menu_url: Optional[str]
    city_id: Optional[int]
    landmark_id: Optional[int]


class RestaurantBaseResponse(RestaurantBase):
    id: int

    class Config:
        from_attributes = True
