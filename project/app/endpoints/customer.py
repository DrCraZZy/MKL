from fastapi import APIRouter, Depends

from .depends import get_customer_repository
from project.app.models.customer import CustomerIn, CustomerOut
from project.app.repositories.customers import CustomerRepository

router = APIRouter()


@router.post("/", response_model=CustomerOut)
async def create_customer(
        customer: CustomerIn,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.create_customer(c=customer)
