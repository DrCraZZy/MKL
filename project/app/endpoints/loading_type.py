from fastapi import APIRouter, Depends, status, HTTPException

from .depends import get_loading_type_repository
from project.app.schema.loading_type import LoadingTypeInSchema
from project.app.repositories.loading_type import LoadingTypeRepository
from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.helper.message_parser import parse_message

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_loading_type(
        lt: LoadingTypeInSchema,
        ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    answer: EndpointAnswer = await ltr.create_loading_type(lt)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_loading_type(ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    answer: EndpointAnswer = await ltr.get_loading_types()
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer

@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_loading_type(
        lt_id: int,
        lt: LoadingTypeInSchema,
        ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    answer: EndpointAnswer = await ltr.update_loading_type(lt_id=lt_id, lt=lt)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer

@router.delete("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_loading_type(
        lt_id: int,
        ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    answer: EndpointAnswer = await ltr.delete_loading_type(lt_id)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer
