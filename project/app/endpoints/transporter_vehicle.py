from fastapi import APIRouter, Depends, status, HTTPException

from .depends import get_transporter_vehicle_repository
from project.app.schema.transporter_vehicle import TransporterVehicleInSchema
from project.app.repositories.transporter_vehicle import TransporterVehicleRepository
from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.helper.message_parser import parse_message

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_transporter_vehicle(
        vehicle: TransporterVehicleInSchema,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    answer: EndpointAnswer = await vehicles.create_transporter_vehicle(vehicle)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_all_vehicle(
        limit: int = 100,
        skip: int = 0,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    answer: EndpointAnswer = await vehicles.get_all_vehicles(limit=limit, skip=skip)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.get("/{transporter_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_transporter_vehicles_by_inn(
        customer_inn: str,
        limit: int = 100,
        skip: int = 0,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    answer: EndpointAnswer = await vehicles.get_transporter_vehicles_by_inn(customer_inn=customer_inn, limit=limit,
                                                                            skip=skip)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def update_vehicle(
        vehicle_id: int,
        customer_inn: str,
        vehicle: TransporterVehicleInSchema,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    answer: EndpointAnswer = await vehicles.update_vehicle_by_id_by_inn(vehicle_id=vehicle_id,
                                                                        customer_inn=customer_inn, vehicle=vehicle)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer


@router.delete("/{vehicle_id}", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_vehicle_by_id(
        vehicle_id: int,
        vehicles: TransporterVehicleRepository = Depends(get_transporter_vehicle_repository)):
    answer: EndpointAnswer = await vehicles.delete_vehicle_by_id(vehicle_id=vehicle_id)
    if answer.status != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=parse_message(answer.message)
        )

    return answer
