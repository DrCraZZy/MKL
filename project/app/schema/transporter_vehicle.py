from pydantic import BaseModel
from datetime import datetime


class TransporterVehicleInSchema(BaseModel):
    inn_transporter: str
    brand: str
    model: str
    dry_weight: int
    max_weight: int
    physical_property: int
    weight: int
    dimension: float
    loading_type: int
    cost_up_to_100km: float
    cost_up_to_500km: float
    cost_up_to_1000km: float
    is_available: bool


class TransporterVehicleOutSchema(TransporterVehicleInSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    