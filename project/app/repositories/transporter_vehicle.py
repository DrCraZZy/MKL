from typing import List
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import and_

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.transporter_vehicle import TransporterVehicleInSchema, TransporterVehicleOutSchema
from project.app.db.tables.transporter import transporter_vehicle
from project.app.helper.log import logger


class TransporterVehicleRepository(BaseRepository):

    @logger.catch
    async def create_transporter_vehicle(self, vehicle: TransporterVehicleInSchema) -> TransporterVehicleOutSchema:
        query = transporter_vehicle.insert().values(
            inn_transporter=vehicle.inn_transporter,
            brand=vehicle.brand,
            model=vehicle.model,
            dry_weight=vehicle.dry_weight,
            max_weight=vehicle.max_weight,
            physical_property=vehicle.physical_property,
            weight=vehicle.weight,
            dimension=vehicle.dimension,
            loading_type=vehicle.loading_type,
            cost_up_to_100km=vehicle.cost_up_to_100km,
            cost_up_to_500km=vehicle.cost_up_to_500km,
            cost_up_to_1000km=vehicle.cost_up_to_1000km,
            is_available=vehicle.is_available,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        new_id = await self.database.execute(query)

        query = transporter_vehicle.select().where(transporter_vehicle.c.id == new_id)
        new_vehicle = await self.database.fetch_one(query)

        if not new_vehicle:
            message: str = "Vehicle can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New vehicle with id:'{new_id}' for customer with inn:'{vehicle.inn_transporter}' was created.")

        return TransporterVehicleOutSchema.parse_obj(new_vehicle)

    @logger.catch
    async def get_all_vehicles(self, limit: int = 100, skip: int = 0) -> List[TransporterVehicleOutSchema]:
        query = transporter_vehicle.select().limit(limit).offset(skip)
        customer_list = await self.database.fetch_all(query)
        customer_list_object = []
        for c in customer_list:
            customer_list_object.append(TransporterVehicleOutSchema.parse_obj(c))

        return customer_list_object

    @logger.catch
    async def get_transporter_vehicles_by_inn(self, transporter_inn: str, limit: int = 100, skip: int = 0) -> \
            List[TransporterVehicleOutSchema]:
        query = \
            transporter_vehicle. \
            select(). \
            where(transporter_vehicle.c.inn_transporter == transporter_inn). \
            limit(limit). \
            offset(skip)
        vehicle_list = await self.database.fetch_all(query=query)

        if not vehicle_list:
            message = f"Vehicles for customer with inn:'{transporter_inn}' does not exists."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message
            )

        vehicle_list_object = []
        for o in vehicle_list:
            vehicle_list_object.append(TransporterVehicleOutSchema.parse_obj(o))

        return vehicle_list_object

    @logger.catch
    async def update_vehicle_by_id_by_inn(self,
                                          vehicle_id: int,
                                          transporter_inn: str,
                                          vehicle: TransporterVehicleInSchema) -> TransporterVehicleOutSchema:
        query = transporter_vehicle.update().where(
            and_(transporter_vehicle.c.inn_transporter == transporter_inn, transporter_vehicle.c.id == vehicle_id)). \
            values(
            inn_transporter=vehicle.inn_transporter,
            brand=vehicle.brand,
            model=vehicle.model,
            dry_weight=vehicle.dry_weight,
            max_weight=vehicle.max_weight,
            physical_property=vehicle.physical_property,
            weight=vehicle.weight,
            dimension=vehicle.dimension,
            loading_type=vehicle.loading_type,
            cost_up_to_100km=vehicle.cost_up_to_100km,
            cost_up_to_500km=vehicle.cost_up_to_500km,
            cost_up_to_1000km=vehicle.cost_up_to_1000km,
            is_available=vehicle.is_available,
            updated_at=datetime.utcnow()
        )
        await self.database.execute(query)

        query = transporter_vehicle.select().where(
            and_(
                transporter_vehicle.c.inn_transporter == transporter_inn,
                transporter_vehicle.c.id == vehicle_id)
        )
        updated_vehicle = await self.database.fetch_one(query)

        logger.info(f"Vehicle with id:{vehicle_id} for customer with inn:'{transporter_inn}' was updated.")
        return TransporterVehicleOutSchema.parse_obj(updated_vehicle)

    @logger.catch
    async def delete_vehicle_by_id(self, vehicle_id: int) -> dict:
        query = transporter_vehicle.delete().where(transporter_vehicle.c.id == vehicle_id)
        await self.database.execute(query)

        message = f"Vehicle with id:'{vehicle_id}' was deleted."
        logger.info(message)
        return {"message": message}
