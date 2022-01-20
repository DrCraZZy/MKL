from typing import List
from fastapi import HTTPException, status

from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.loading_type import LoadingTypeInSchema, LoadingTypeOutSchema
from project.app.db.tables.references import loading_type


class LoadingTypeRepository(BaseRepository):

    @logger.catch
    async def get_loading_types(self) -> List[LoadingTypeOutSchema]:
        query = loading_type.select()
        lt_list = await self.database.fetch_all(query)

        lt_list_obj = []
        for lt in lt_list:
            lt_list_obj.append(LoadingTypeOutSchema.parse_obj(lt))

        return lt_list_obj

    @logger.catch
    async def create_loading_type(self, lt: LoadingTypeInSchema) -> LoadingTypeOutSchema:
        query = loading_type.insert().values(
            loading_type=lt.loading_type,
            description=lt.description)

        new_id = await self.database.execute(query)
        query = loading_type.select().where(loading_type.c.id == new_id)
        new_order = await self.database.fetch_one(query)

        if not new_order:
            message: str = "Loading type can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New loading type with id:'{new_id}' was created.")

        return LoadingTypeOutSchema.parse_obj(new_order)

    @logger.catch
    async def update_loading_type(
            self,
            lt_id: int,
            lt: LoadingTypeInSchema) -> LoadingTypeOutSchema:
        # insert new values
        query = loading_type. \
            update(). \
            where(loading_type.c.id == lt_id). \
            values(
            loading_type=lt.loading_type,
            description=lt.description
        )

        await self.database.execute(query)

        # get updated row
        query = loading_type.select().where(loading_type.c.id == lt_id)
        updated_lt = await self.database.fetch_one(query)

        logger.info(f"Loading type with id:{lt_id} was updated.")
        return LoadingTypeOutSchema.parse_obj(updated_lt)

    @logger.catch
    async def delete_loading_type(self, lt_id: int) -> dict:
        query = loading_type.delete().where(loading_type.c.id == lt_id)
        await self.database.execute(query)

        message = f"Loading type with id:{lt_id} was deleted."
        logger.info(message)
        return {"message": message}
