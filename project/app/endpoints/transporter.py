from fastapi import APIRouter, Depends, status, HTTPException

from .depends import get_transporter_repository
from project.app.schema.transporter import TransporterSchema
from project.app.repositories.transporter import TransporterRepository
from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.helper.message_parser import parse_message

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_transporter(
        transporter: TransporterSchema,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    answer: EndpointAnswer = await transporters.create_transporter(transporter)

    return answer

@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_transporters(
        limit: int = 100,
        skip: int = 0,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    answer: EndpointAnswer = await transporters.get_all_transporters(limit=limit, skip=skip)

    return answer


@router.get("/{transporter_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_transporter_by_inn(
        transporter_inn: str,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    answer: EndpointAnswer = await transporters.get_transporter_by_inn(transporter_inn=transporter_inn)

    return answer


@router.get("/{transporter_email}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_transporter_by_email(
        transporter_email: str,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    answer: EndpointAnswer = await transporters.get_transporter_by_email(transporter_email=transporter_email)

    return answer


@router.put("/{transporter_inn}", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_transporter_by_inn(
        transporter_inn: str,
        transporter: TransporterSchema,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    answer: EndpointAnswer = await transporters.update_transporter_by_inn(transporter_inn=transporter_inn,
                                                                          transporter=transporter)

    return answer


@router.delete("/{transporter_inn}", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_transporter_by_inn(
        transporter_inn: str,
        transporters: TransporterRepository = Depends(get_transporter_repository)):
    answer: EndpointAnswer = await transporters.delete_transporter_by_inn(transporter_inn=transporter_inn)

    return answer
