from fastapi import APIRouter, Depends, status

from .depends import get_customer_repository
from project.app.schema.customer import CustomerSchema
from project.app.repositories.customer import CustomerRepository
from project.app.helper.endpoint_answer import EndpointAnswer

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_customer(
        customer: CustomerSchema,
        customers: CustomerRepository = Depends(get_customer_repository)):
    answer: EndpointAnswer = await customers.create_customer(customer)

    return answer


@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_customers(
        limit: int = 100,
        skip: int = 0,
        customers: CustomerRepository = Depends(get_customer_repository)):
    answer: EndpointAnswer = await customers.get_all_customers(limit=limit, skip=skip)

    return answer


@router.get("/{customer_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_customer_by_inn(
        customer_inn: str,
        customers: CustomerRepository = Depends(get_customer_repository)):
    answer: EndpointAnswer = await customers.get_customer_by_inn(customer_inn=customer_inn)

    return answer


@router.get("/{customer_email}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_customer_by_email(
        customer_email: str,
        customers: CustomerRepository = Depends(get_customer_repository)):
    answer: EndpointAnswer = await customers.get_customer_by_email(customer_email=customer_email)

    return answer


@router.put("/{customer_inn}", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_customer_by_inn(
        customer_inn: str,
        customer: CustomerSchema,
        customers: CustomerRepository = Depends(get_customer_repository)):
    answer: EndpointAnswer = await customers.update_customer_by_inn(customer_inn=customer_inn, customer=customer)

    return answer


@router.delete("/{customer_inn}", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_customer_by_inn(
        customer_inn: str,
        customers: CustomerRepository = Depends(get_customer_repository)):
    answer: EndpointAnswer = await customers.delete_customer_by_inn(customer_inn=customer_inn)

    return answer
