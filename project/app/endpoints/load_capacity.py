from fastapi import APIRouter, Depends, status

from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.repositories.load_capacity import LoadCapacityRepository
from project.app.schema.load_capacity import LoadCapacityInSchema
from .depends import get_load_capacity_repository

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_load_capacity(
        lc: LoadCapacityInSchema,
        lcr: LoadCapacityRepository = Depends(get_load_capacity_repository)):
    answer: EndpointAnswer = await lcr.create_load_capacity(lc)

    return answer


@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_load_capacity(lcr: LoadCapacityRepository = Depends(get_load_capacity_repository)):
    answer: EndpointAnswer = await lcr.get_load_capacity()

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_load_capacity(
        lc_id: int,
        lc: LoadCapacityInSchema,
        lcr: LoadCapacityRepository = Depends(get_load_capacity_repository)):
    answer: EndpointAnswer = await lcr.update_load_capacity(lc_id=lc_id, lc=lc)

    return answer


@router.delete("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_load_capacity(
        lc_id: int,
        lcr: LoadCapacityRepository = Depends(get_load_capacity_repository)):
    answer: EndpointAnswer = await lcr.delete_load_capacity(lc_id)

    return answer
