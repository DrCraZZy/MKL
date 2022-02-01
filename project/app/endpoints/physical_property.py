from fastapi import APIRouter, Depends, status, HTTPException

from .depends import get_physical_property_repository
from project.app.schema.physical_property import PhysicalPropertyInSchema
from project.app.repositories.physical_property import PhysicalPropertyRepository
from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.helper.message_parser import parse_message

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_physical_property(
        pp: PhysicalPropertyInSchema,
        ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    answer: EndpointAnswer = await ppr.create_physical_property(pp)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_physical_properties(ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    answer: EndpointAnswer = await ppr.get_physical_properties()
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_physical_property(
        pp_id: int,
        pp: PhysicalPropertyInSchema,
        ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    answer: EndpointAnswer = await ppr.update_physical_property(pp_id=pp_id, pp=pp)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.delete("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_physical_property(
        pp_id: int,
        ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    answer: EndpointAnswer = await ppr.delete_physical_property(pp_id)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer
