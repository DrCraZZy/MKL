from datetime import datetime
from sqlalchemy import and_

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.transporter_vehicle import TransporterVehicleInSchema, TransporterVehicleOutSchema
from project.app.db.tables.transporter import transporter_vehicle
from project.app.helper.log import logger
from project.app.helper.endpoint_answer import EndpointAnswer


class TransporterVehicleRepository(BaseRepository):

    @logger.catch
    async def create_transporter_vehicle(self, vehicle: TransporterVehicleInSchema) -> EndpointAnswer:
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
        try:
            new_id = await self.database.execute(query)
            query = transporter_vehicle.select().where(transporter_vehicle.c.id == new_id)
            new_vehicle = await self.database.fetch_one(query)
            if not new_vehicle:
                message: str = "Vehicle can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = \
                    f"New vehicle with id:'{new_id}' for customer with inn:'{vehicle.inn_transporter}' was created."
                result = EndpointAnswer(status="success", message=message, result=new_vehicle)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_all_vehicles(self, limit: int = 100, skip: int = 0) -> EndpointAnswer:
        query = transporter_vehicle.select().limit(limit).offset(skip)
        try:
            vehicle_list = await self.database.fetch_all(query)
            if not vehicle_list:
                message = f"Vehicles were not found"
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                vehicle_list_object = []
                for c in vehicle_list:
                    vehicle_list_object.append(TransporterVehicleOutSchema.parse_obj(c))
                message = f"There are '{len(vehicle_list_object)}' vehicles."
                result = EndpointAnswer(status="success", message=message, result=vehicle_list_object)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_transporter_vehicles_by_inn(self, transporter_inn: str, limit: int = 100, skip: int = 0) -> \
            EndpointAnswer:
        query = transporter_vehicle.select().where(transporter_vehicle.c.inn_transporter == transporter_inn). \
            limit(limit).offset(skip)
        try:
            vehicle_list = await self.database.fetch_all(query=query)

            if not vehicle_list:
                message = f"Vehicles for customer with inn:'{transporter_inn}' does not exists."
                result = EndpointAnswer(status="success", message=message)
                logger.error(message)
            else:
                vehicle_list_object = []
                for o in vehicle_list:
                    vehicle_list_object.append(TransporterVehicleOutSchema.parse_obj(o))
                message = f"There are '{len(vehicle_list_object)}' " \
                          f"vehicles(s) for transporter with inn:'{transporter_inn}'"
                result = EndpointAnswer(status="success", message=message, result=vehicle_list_object)
                logger.info(message)

        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_vehicle_by_id_by_inn(self,
                                          vehicle_id: int,
                                          transporter_inn: str,
                                          vehicle: TransporterVehicleInSchema) -> EndpointAnswer:
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
        try:
            await self.database.execute(query)

            query = transporter_vehicle.select().where(
                and_(
                    transporter_vehicle.c.inn_transporter == transporter_inn,
                    transporter_vehicle.c.id == vehicle_id)
            )
            updated_vehicle = await self.database.fetch_one(query)

            message: str = f"Vehicle with id:{vehicle_id} for customer with inn:'{transporter_inn}' was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_vehicle)
            logger.info(message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))

        return result

    @logger.catch
    async def delete_vehicle_by_id(self, vehicle_id: int) -> EndpointAnswer:
        query = transporter_vehicle.delete().where(transporter_vehicle.c.id == vehicle_id)
        try:
            await self.database.execute(query)
            message = f"Vehicle with id:'{vehicle_id}' was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result
