from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.loading_type import LoadingTypeInSchema, LoadingTypeOutSchema
from project.app.db.tables.references import loading_type
from project.app.helper.endpoint_answer import EndpointAnswer


class LoadingTypeRepository(BaseRepository):

    @logger.catch
    async def get_loading_types(self) -> EndpointAnswer:
        query = loading_type.select()
        try:
            lt_list = await self.database.fetch_all(query)

            if not lt_list:
                message = f"There ara no loading types"
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                lt_list_obj = []
                for lt in lt_list:
                    lt_list_obj.append(LoadingTypeOutSchema.parse_obj(lt))
                message = f"There are '{len(lt_list_obj)}' loading types"
                result = EndpointAnswer(status="success", message=message, result=lt_list_obj)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def create_loading_type(self, lt: LoadingTypeInSchema) -> EndpointAnswer:
        query = loading_type.insert().values(
            loading_type=lt.loading_type,
            description=lt.description)
        try:
            new_id = await self.database.execute(query)

            query = loading_type.select().where(loading_type.c.id == new_id)
            new_item = await self.database.fetch_one(query)

            if not new_item:
                message: str = "Loading type can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = f"New loading type with id:'{new_id}' was created."
                result = EndpointAnswer(status="success", message=message, result=new_item)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_loading_type(self, lt_id: int, lt: LoadingTypeInSchema) -> EndpointAnswer:
        # insert new values
        query = loading_type.update().where(loading_type.c.id == lt_id).values(
            loading_type=lt.loading_type,
            description=lt.description)

        try:
            await self.database.execute(query)

            # get updated row
            query = loading_type.select().where(loading_type.c.id == lt_id)
            updated_lt = await self.database.fetch_one(query)
            message: str = f"Loading type with id:{lt_id} was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_lt)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def delete_loading_type(self, lt_id: int) -> EndpointAnswer:
        query = loading_type.delete().where(loading_type.c.id == lt_id)
        try:
            await self.database.execute(query)
            message: str = f"Loading type with id:{lt_id} was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result
