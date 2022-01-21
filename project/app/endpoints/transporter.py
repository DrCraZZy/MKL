from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_transporter_repository
from project.app.schema.transporter import TransporterSchema
from project.app.repositories.transporter import TransporterRepository

router = APIRouter()


@router.post("/", response_model=TransporterSchema, status_code=status.HTTP_201_CREATED)
async def create_transporter(
        transporter: TransporterSchema,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    return await transporters.create_transporter(transporter)


@router.get("/", response_model=List[TransporterSchema], status_code=status.HTTP_200_OK)
async def get_transporters(
        limit: int = 100,
        skip: int = 0,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    return await transporters.get_all_transporters(limit=limit, skip=skip)


@router.get("/{transporter_inn}", response_model=TransporterSchema, status_code=status.HTTP_200_OK)
async def get_transporter_by_inn(
        transporter_inn: str,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    return await transporters.get_transporter_by_inn(transporter_inn=transporter_inn)


@router.get("/{transporter_email}", response_model=TransporterSchema, status_code=status.HTTP_200_OK)
async def get_transporter_by_email(
        transporter_email: str,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    return await transporters.get_transporter_by_email(transporter_email=transporter_email)


@router.put("/{transporter_inn}", response_model=TransporterSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_transporter_by_inn(
        transporter_inn: str,
        transporter: TransporterSchema,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    return await transporters.update_transporter_by_inn(transporter_inn=transporter_inn, transporter=transporter)


@router.delete("/{transporter_inn}", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_transporter_by_inn(
        transporter_inn: str,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    return await transporters.delete_transporter_by_inn(transporter_inn=transporter_inn)
