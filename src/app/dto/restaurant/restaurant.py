from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.establishment.establishment import EstablishmentBaseCommon, EstablishmentDetailCommon
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

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class RestaurantPostRequest(EstablishmentBaseCommon, RestaurantBase):
    pass


class RestaurantPutRequest(EstablishmentBaseCommon, RestaurantBase):
    id: int


class RestaurantBaseResponse(EstablishmentBaseCommon, RestaurantBase, TimestampDto):
    id: int


class RestaurantDetailResponse(RestaurantBase, EstablishmentDetailCommon, TimestampDto):
    id: int
    social_medias: Optional[list[RestaurantSocialMediaBaseResponse]]
