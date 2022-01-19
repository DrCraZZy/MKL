from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_customer_repository
from project.app.schema.customer import CustomerSchema
from project.app.repositories.customers import CustomerRepository

router = APIRouter()


@router.post("/", response_model=CustomerSchema, status_code=status.HTTP_201_CREATED)
async def create_customer(
        customer: CustomerSchema,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.create_customer(customer)


@router.get("/", response_model=List[CustomerSchema], status_code=status.HTTP_200_OK)
async def get_customers(
        limit: int = 100,
        skip: int = 0,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.get_all_customers(limit=limit, skip=skip)


@router.get("/{customer_inn}", response_model=CustomerSchema, status_code=status.HTTP_200_OK)
async def get_customer_by_inn(
        customer_inn: str,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.get_customer_by_inn(customer_inn=customer_inn)


@router.get("/{customer_email}", response_model=CustomerSchema, status_code=status.HTTP_200_OK)
async def get_customer_by_email(
        customer_email: str,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.get_customer_by_email(customer_email=customer_email)


@router.put("/{customer_inn}", response_model=CustomerSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_customer_by_inn(
        customer_inn: str,
        customer: CustomerSchema,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.update_customer_by_inn(customer_inn=customer_inn, customer=customer)


@router.delete("/{customer_inn}", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_customer_by_inn(
        customer_inn: str,
        customers: CustomerRepository = Depends(get_customer_repository)):
    return await customers.delete_customer_by_inn(customer_inn=customer_inn)
