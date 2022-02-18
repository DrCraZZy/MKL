from pydantic import BaseModel, EmailStr
from datetime import datetime


class CustomerContactInSchema(BaseModel):
    inn_customer: str
    name: str
    surname: str
    patronymic: str | None
    position: str | None
    telephone: str | None
    email: EmailStr


class CustomerContactOutSchema(CustomerContactInSchema):
    id: int
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
