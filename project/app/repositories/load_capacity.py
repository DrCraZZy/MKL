from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.load_capacity import LoadCapacityInSchema, LoadCapacityOutSchema
from project.app.db.tables.references import load_capacity
from project.app.helper.endpoint_answer import EndpointAnswer


class LoadCapacityRepository(BaseRepository):

    @logger.catch
    async def get_load_capacity(self) -> EndpointAnswer:
        query = load_capacity.select()
        try:
            lc_list = await self.database.fetch_all(query)

            if not lc_list:
                message = f"There ara no load capacities"
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                lc_list_obj = []
                for lc in lc_list:
                    lc_list_obj.append(LoadCapacityOutSchema.parse_obj(lc))
                message = f"There are '{len(lc_list_obj)}' load capacities"
                result = EndpointAnswer(status="success", message=message, result=lc_list_obj)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def create_load_capacity(self, lc: LoadCapacityInSchema) -> EndpointAnswer:
        query = load_capacity.insert().values(
            weight_to=lc.weight_to,
            length_to=lc.length_to,
            width_to=lc.width_to,
            height_to=lc.height_to,
            volume_to=lc.volume_to)
        try:
            new_id = await self.database.execute(query)

            query = load_capacity.select().where(load_capacity.c.id == new_id)
            new_item = await self.database.fetch_one(query)

            if not new_item:
                message: str = "Load capacity can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = f"New loading capacity with id:'{new_id}' was created."
                result = EndpointAnswer(status="success", message=message, result=new_item)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_load_capacity(self, lc_id: int, lc: LoadCapacityInSchema) -> EndpointAnswer:
        # insert new values
        query = load_capacity.update().where(load_capacity.c.id == lc_id).values(
            weight_to=lc.weight_to,
            length_to=lc.length_to,
            width_to=lc.width_to,
            height_to=lc.height_to,
            volume_to=lc.volume_to)

        try:
            await self.database.execute(query)

            # get updated row
            query = load_capacity.select().where(load_capacity.c.id == lc_id)
            updated_lc = await self.database.fetch_one(query)
            message: str = f"Load capacity with id:{lc_id} was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_lc)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def delete_load_capacity(self, lc_id: int) -> EndpointAnswer:
        query = load_capacity.delete().where(load_capacity.c.id == lc_id)
        try:
            await self.database.execute(query)
            message: str = f"Load capacity with id:{lc_id} was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result
