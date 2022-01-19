from pydantic import BaseModel
from datetime import datetime


class CustomerOrderUpdateSchema(BaseModel):
    physical_properties: int | None
    weight: int | None
    dimension: float | None
    loading_type: int | None
    loading_address: str
    loading_coordinate: str | None
    delivery_address: str
    delivery_coordinate: str | None
    distance_km: int
    price: float
    is_active: bool


class CustomerOrderInSchema(CustomerOrderUpdateSchema):
    inn_kpp_customer: str


class CustomerOrderSchema(CustomerOrderInSchema):
    created_at: datetime
    updated_at: datetime


class CustomerOrderOutSchema(CustomerOrderSchema):
    id: int | None
