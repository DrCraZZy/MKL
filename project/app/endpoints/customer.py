from fastapi import APIRouter, Depends

from .depends import get_customer_repository
from project.app.schema.customer import CustomerSchema
from project.app.repositories.customers import CustomerRepository

router = APIRouter()


@router.post("/", response_model=CustomerSchema, status_code=status.HTTP_201_CREATED)
async def create_customer(
        customer: CustomerIn,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.create_customer(c=customer)
