from pydantic import BaseModel, EmailStr
from datetime import datetime


# Base customer information
class CustomerBase(BaseModel):
    inn_kpp: str
    ogrn: str
    name: str
    date_of_formation: datetime | None
    director: str | None
    legal_address: str
    address: str
    email: EmailStr
    telephone: str | None
    payment_account: str
    corporate_account: str


# Customer gives data for insert it to the database
class CustomerIn(CustomerBase):
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()


# Output customer parameters for viewing
class CustomerOut(CustomerBase):
    ...
