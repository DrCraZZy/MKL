from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_customer_contact_repository
from project.app.schema.customer_contact import CustomerContactInSchema, CustomerContactOutSchema
from project.app.repositories.customer_contact import CustomerContactRepository

router = APIRouter()


@router.get("/{customer_inn}", response_model=List[CustomerContactOutSchema], status_code=status.HTTP_200_OK)
async def get_customer_contacts(
        customer_inn: str,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    return await contacts.get_customer_contacts_by_inn(customer_inn=customer_inn)


@router.post("/", response_model=CustomerContactOutSchema, status_code=status.HTTP_202_ACCEPTED)
async def create_customer_contact(
        contact: CustomerContactInSchema,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    return await contacts.create_customer_contact(contact=contact)


@router.put("/", response_model=CustomerContactOutSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_customer_contact(
        contact_id: int,
        customer_inn: str,
        contact: CustomerContactInSchema,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    return await contacts.update_contact(contact_id=contact_id, customer_inn=customer_inn, contact=contact)


@router.delete("/", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_customer_contact_by_id(
        contact_id: int,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    return await contacts.delete_customer_contact_by_id(contact_id=contact_id)
