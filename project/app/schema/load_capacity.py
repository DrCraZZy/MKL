from pydantic import BaseModel


class LoadCapacityInSchema(BaseModel):
    weight_to: float
    length_to: float
    width_to: float
    height_to: float
    volume_to: float


class LoadCapacityOutSchema(LoadCapacityInSchema):
    id: int
