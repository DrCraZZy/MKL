from fastapi import APIRouter, Depends, status

from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.repositories.customer_contact import CustomerContactRepository
from project.app.schema.customer_contact import CustomerContactInSchema
from .depends import get_customer_contact_repository

router = APIRouter()


@router.get("/{customer_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_customer_contacts(
        customer_inn: str,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    answer: EndpointAnswer = await contacts.get_customer_contacts_by_inn(customer_inn=customer_inn)

    return answer


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def create_customer_contact(
        contact: CustomerContactInSchema,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    answer: EndpointAnswer = await contacts.create_customer_contact(contact=contact)

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_customer_contact(
        contact_id: int,
        customer_inn: str,
        contact: CustomerContactInSchema,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    answer: EndpointAnswer = await contacts.update_contact(contact_id=contact_id, customer_inn=customer_inn,
                                                           contact=contact)

    return answer


@router.delete("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_customer_contact_by_id(
        contact_id: int,
        contacts: CustomerContactRepository = Depends(get_customer_contact_repository)):
    answer: EndpointAnswer = await contacts.delete_customer_contact_by_id(contact_id=contact_id)

    return answer
