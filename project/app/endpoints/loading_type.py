from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_loading_type_repository
from project.app.schema.loading_type import LoadingTypeInSchema, LoadingTypeOutSchema
from project.app.repositories.loading_type import LoadingTypeRepository

router = APIRouter()


@router.post("/", response_model=LoadingTypeOutSchema, status_code=status.HTTP_201_CREATED)
async def create_loading_type(
        lt: LoadingTypeInSchema,
        ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    return await ltr.create_loading_type(lt)


@router.get("/", response_model=List[LoadingTypeOutSchema], status_code=status.HTTP_200_OK)
async def create_loading_type(ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    return await ltr.get_loading_types()


@router.put("/", response_model=LoadingTypeOutSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_loading_type(
        lt_id: int,
        lt: LoadingTypeInSchema,
        ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    return await ltr.update_loading_type(lt_id=lt_id, lt=lt)


@router.delete("/", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_loading_type(
        lt_id: int,
        ltr: LoadingTypeRepository = Depends(get_loading_type_repository)):
    return await ltr.delete_loading_type(lt_id)
