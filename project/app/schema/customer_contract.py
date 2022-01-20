from pydantic import BaseModel
from datetime import datetime, date


class CustomerContractSchema(BaseModel):
    contract_number: str
    inn_customer: str
    customer_order_id: int
    start_date: date
    end_date: date


class CustomerContractOutSchema(CustomerContractSchema):
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()