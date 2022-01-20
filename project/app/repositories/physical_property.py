from typing import List
from fastapi import HTTPException, status

from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.physical_property import PhysicalPropertyOutSchema, PhysicalPropertyInSchema
from project.app.db.tables.references import physical_property


class PhysicalPropertyRepository(BaseRepository):

    @logger.catch
    async def get_physical_property(self) -> List[PhysicalPropertyOutSchema]:
        query = physical_property.select()
        pp_list = await self.database.fetch_all(query)

        pp_list_obj = []
        for pp in pp_list:
            pp_list_obj.append(PhysicalPropertyOutSchema.parse_obj(pp))

        return pp_list_obj

    @logger.catch
    async def create_physical_property(self, pp: PhysicalPropertyInSchema) -> PhysicalPropertyOutSchema:
        query = physical_property.insert().values(
            physical_property=pp.physical_property,
            description=pp.description)

        new_id = await self.database.execute(query)
        query = physical_property.select().where(physical_property.c.id == new_id)
        new_item = await self.database.fetch_one(query)

        if not new_item:
            message: str = "Physical property can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New physical property with id:'{new_id}' was created.")

        return PhysicalPropertyOutSchema.parse_obj(new_item)

    @logger.catch
    async def update_physical_property(
            self,
            pp_id: int,
            pp: PhysicalPropertyInSchema) -> PhysicalPropertyOutSchema:
        # insert new values
        query = physical_property. \
            update(). \
            where(physical_property.c.id == pp_id). \
            values(
                physical_property=pp.physical_property,
                description=pp.description
            )

        await self.database.execute(query)

        # get updated row
        query = physical_property.select().where(physical_property.c.id == pp_id)
        updated_pp = await self.database.fetch_one(query)

        logger.info(f"Physical property with id:'{pp_id}' was updated.")
        return PhysicalPropertyOutSchema.parse_obj(updated_pp)

    @logger.catch
    async def delete_physical_property(self, pp_id: int) -> dict:
        query = physical_property.delete().where(physical_property.c.id == pp_id)
        await self.database.execute(query)

        message = f"Physical property with id:'{pp_id}' was deleted."
        logger.info(message)
        return {"message": message}
