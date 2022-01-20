from pydantic import BaseModel, EmailStr
from datetime import datetime, date


# Base customer information
class CustomerSchema(BaseModel):
    inn: str
    kpp: str
    ogrn: str
    name: str
    date_of_formation: date | None
    director: str | None
    legal_address: str
    address: str
    email: EmailStr
    telephone: str | None
    payment_account: str
    corporate_account: str


class CustomerOutSchema(CustomerSchema):
    created_at: datetime
    updated_at: datetime
