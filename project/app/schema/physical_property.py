from pydantic import BaseModel


class PhysicalPropertyInSchema(BaseModel):
    physical_property: str
    description: str


class PhysicalPropertyOutSchema(PhysicalPropertyInSchema):
    id: int
