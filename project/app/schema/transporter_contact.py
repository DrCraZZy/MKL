from pydantic import BaseModel, EmailStr
from datetime import datetime


class TransporterContactInSchema(BaseModel):
    inn_transporter: str
    name: str
    surname: str
    patronymic: str | None
    position: str | None
    telephone: str | None
    email: EmailStr


class TransporterContactOutSchema(TransporterContactInSchema):
    id: int
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

