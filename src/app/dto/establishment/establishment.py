from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.dto.landmark.landmark_base_response import LandmarkBaseResponse


class EstablishmentBaseCommon(CamelModel):
    city_id: Optional[int]
    landmark_id: Optional[int]

class EstablishmentDetailCommon(CamelModel):
    city: Optional[CityBaseResponse]
    landmark: Optional[LandmarkBaseResponse]
