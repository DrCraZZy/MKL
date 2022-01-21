from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_transporter_vehicle_repository
from project.app.schema.transporter_vehicle import TransporterVehicleInSchema, TransporterVehicleOutSchema
from project.app.repositories.transporter_vehicle import TransporterVehicleRepository

router = APIRouter()


@router.post("/", response_model=TransporterVehicleOutSchema, status_code=status.HTTP_201_CREATED)
async def create_transporter_vehicle(
        vehicle: TransporterVehicleInSchema,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    return await vehicles.create_transporter_vehicle(vehicle)


@router.get("/", response_model=List[TransporterVehicleOutSchema], status_code=status.HTTP_200_OK)
async def get_all_vehicle(
        limit: int = 100,
        skip: int = 0,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    return await vehicles.get_all_vehicles(limit=limit, skip=skip)


@router.get("/{transporter_inn}", response_model=List[TransporterVehicleOutSchema], status_code=status.HTTP_200_OK)
async def get_transporter_vehicles_by_inn(
        customer_inn: str,
        limit: int = 100,
        skip: int = 0,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    return await vehicles.get_transporter_vehicles_by_inn(customer_inn=customer_inn, limit=limit, skip=skip)


@router.put("/", response_model=TransporterVehicleOutSchema, status_code=status.HTTP_201_CREATED)
async def update_vehicle(
        vehicle_id: int,
        customer_inn: str,
        vehicle: TransporterVehicleInSchema,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    return await vehicles.update_vehicle_by_id_by_inn(vehicle_id=vehicle_id, customer_inn=customer_inn, vehicle=vehicle)


@router.delete("/{vehicle_id}", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_vehicle_by_id(
        vehicle_id: int,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    return await vehicles.delete_vehicle_by_id(vehicle_id=vehicle_id)
