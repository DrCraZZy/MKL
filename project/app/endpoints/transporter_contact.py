from fastapi import APIRouter, Depends, status

from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.repositories.transporter_contact import TransporterContactRepository
from project.app.schema.transporter_contact import TransporterContactInSchema
from .depends import get_transporter_contact_repository

router = APIRouter()


@router.get("/{transporter_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_transporter_contacts(
        transporter_inn: str,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.get_transporter_contacts_by_inn(transporter_inn=transporter_inn)

    return answer


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def create_transporter_contact(
        contact: TransporterContactInSchema,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.create_transporter_contact(contact=contact)

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_transporter_contact(
        contact_id: int,
        transporter_inn: str,
        contact: TransporterContactInSchema,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.update_contact(contact_id=contact_id, transporter_inn=transporter_inn,
                                                           contact=contact)

    return answer


@router.delete("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_transporter_contact_by_id(
        contact_id: int,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.delete_transporter_contact_by_id(contact_id=contact_id)

    return answer
