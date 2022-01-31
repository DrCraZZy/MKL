from fastapi import APIRouter, Depends, status, HTTPException

from .depends import get_transporter_contact_repository
from project.app.schema.transporter_contact import TransporterContactInSchema
from project.app.repositories.transporter_contact import TransporterContactRepository
from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.helper.message_parser import parse_message

router = APIRouter()


@router.get("/{transporter_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_transporter_contacts(
        transporter_inn: str,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.get_transporter_contacts_by_inn(transporter_inn=transporter_inn)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def create_transporter_contact(
        contact: TransporterContactInSchema,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.create_transporter_contact(contact=contact)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_transporter_contact(
        contact_id: int,
        transporter_inn: str,
        contact: TransporterContactInSchema,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.update_contact(contact_id=contact_id, transporter_inn=transporter_inn,
                                                           contact=contact)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.delete("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_transporter_contact_by_id(
        contact_id: int,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    answer: EndpointAnswer = await contacts.delete_transporter_contact_by_id(contact_id=contact_id)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer
