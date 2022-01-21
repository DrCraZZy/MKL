from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_transporter_contact_repository
from project.app.schema.transporter_contact import TransporterContactInSchema, TransporterContactOutSchema
from project.app.repositories.transporter_contact import TransporterContactRepository

router = APIRouter()


@router.get("/{transporter_inn}", response_model=List[TransporterContactOutSchema], status_code=status.HTTP_200_OK)
async def get_transporter_contacts(
        transporter_inn: str,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    return await contacts.get_transporter_contacts_by_inn(transporter_inn=transporter_inn)


@router.post("/", response_model=TransporterContactOutSchema, status_code=status.HTTP_202_ACCEPTED)
async def create_transporter_contact(
        contact: TransporterContactInSchema,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    return await contacts.create_transporter_contact(contact=contact)


@router.put("/", response_model=TransporterContactOutSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_transporter_contact(
        contact_id: int,
        transporter_inn: str,
        contact: TransporterContactInSchema,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    return await contacts.update_contact(contact_id=contact_id, transporter_inn=transporter_inn, contact=contact)


@router.delete("/", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_transporter_contact_by_id(
        contact_id: int,
        contacts: TransporterContactRepository = Depends(get_transporter_contact_repository)):
    return await contacts.delete_transporter_contact_by_id(contact_id=contact_id)
