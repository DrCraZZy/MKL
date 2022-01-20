from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_physical_property_repository
from project.app.schema.physical_property import PhysicalPropertyInSchema, PhysicalPropertyOutSchema
from project.app.repositories.physical_property import PhysicalPropertyRepository

router = APIRouter()


@router.post("/", response_model=PhysicalPropertyOutSchema, status_code=status.HTTP_201_CREATED)
async def create_physical_property(
        pp: PhysicalPropertyInSchema,
        ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    return await ppr.create_physical_property(pp)


@router.get("/", response_model=List[PhysicalPropertyOutSchema], status_code=status.HTTP_200_OK)
async def get_physical_property(ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    return await ppr.get_physical_property()


@router.put("/", response_model=PhysicalPropertyOutSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_physical_property(
        pp_id: int,
        pp: PhysicalPropertyInSchema,
        ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    return await ppr.update_physical_property(pp_id=pp_id, pp=pp)


@router.delete("/", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_physical_property(
        pp_id: int,
        ppr: PhysicalPropertyRepository = Depends(get_physical_property_repository)):
    return await ppr.delete_physical_property(pp_id)
