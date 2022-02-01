from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.physical_property import PhysicalPropertyOutSchema, PhysicalPropertyInSchema
from project.app.db.tables.references import physical_property
from project.app.helper.endpoint_answer import EndpointAnswer


class PhysicalPropertyRepository(BaseRepository):

    @logger.catch
    async def get_physical_properties(self) -> EndpointAnswer:
        query = physical_property.select()
        try:
            pp_list = await self.database.fetch_all(query)

            pp_list_obj = []
            for pp in pp_list:
                pp_list_obj.append(PhysicalPropertyOutSchema.parse_obj(pp))
            message: str = "List of physical properties is created."
            result = EndpointAnswer(status="success", message=message, result=pp_list_obj)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def create_physical_property(self, pp: PhysicalPropertyInSchema) -> EndpointAnswer:
        query = physical_property.insert().values(
            physical_property=pp.physical_property,
            description=pp.description)
        try:
            new_id = await self.database.execute(query)
            query = physical_property.select().where(physical_property.c.id == new_id)
            new_item = await self.database.fetch_one(query)

            if not new_item:
                message: str = "Physical property can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = f"New physical property with id:'{new_id}' was created."
                result = EndpointAnswer(status="success", message=message, result=new_item)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_physical_property(
            self,
            pp_id: int,
            pp: PhysicalPropertyInSchema) -> EndpointAnswer:
        # insert new values
        query = physical_property.update().where(physical_property.c.id == pp_id). \
            values(physical_property=pp.physical_property, description=pp.description)
        try:
            await self.database.execute(query)

            # get updated row
            query = physical_property.select().where(physical_property.c.id == pp_id)
            updated_pp = await self.database.fetch_one(query)
            message: str = f"Physical property with id:'{pp_id}' was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_pp)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def delete_physical_property(self, pp_id: int) -> EndpointAnswer:
        query = physical_property.delete().where(physical_property.c.id == pp_id)
        try:
            await self.database.execute(query)
            message: str = f"Physical property with id:'{pp_id}' was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result
