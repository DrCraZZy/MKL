from typing import List
from fastapi import HTTPException, status
from datetime import datetime

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.transporter import TransporterOutSchema, TransporterSchema
from project.app.db.tables.transporter import transporter_data
from project.app.helper.log import logger


class TransporterRepository(BaseRepository):

    @logger.catch
    async def create_transporter(self, transporter: TransporterSchema) -> TransporterOutSchema:
        query = transporter_data.insert().values(
            inn=transporter.inn,
            kpp=transporter.kpp,
            ogrn=transporter.ogrn,
            name=transporter.name,
            date_of_formation=transporter.date_of_formation,
            director=transporter.director,
            legal_address=transporter.legal_address,
            address=transporter.address,
            email=transporter.email,
            telephone=transporter.telephone,
            payment_account=transporter.payment_account,
            corporate_account=transporter.corporate_account,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        await self.database.execute(query)

        # check for data insertion, is data with new inn in the table
        query = transporter_data.select().where(transporter_data.c.inn == transporter.inn)
        new_transporter = await self.database.fetch_one(query)

        if not new_transporter:
            message: str = "Transporter can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New transporter with inn:'{transporter.inn}' was created.")
        return TransporterOutSchema.parse_obj(new_transporter)

    @logger.catch
    async def get_all_transporters(self, limit: int = 100, skip: int = 0) -> List[TransporterSchema]:
        query = transporter_data.select().limit(limit).offset(skip)
        transporter_list = await self.database.fetch_all(query)
        transporter_list_object = []
        for c in transporter_list:
            transporter_list_object.append(TransporterSchema.parse_obj(c))

        return transporter_list_object

    @logger.catch
    async def get_transporter_by_inn(self, transporter_inn: str) -> TransporterSchema | None:
        query = transporter_data.select().where(transporter_data.c.inn == transporter_inn)
        transporter = await self.database.fetch_one(query=query)

        if transporter:
            transporter_obj = TransporterSchema.parse_obj(transporter)
            return transporter_obj

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transporter with inn:'{transporter_inn}' does not exists."
        )

    @logger.catch
    async def get_transporter_by_email(self, transporter_email: str) -> TransporterSchema | None:
        query = transporter_data.select().where(transporter_data.c.email == transporter_email).first()
        transporter = await self.database.fetch_one(query=query)

        if transporter:
            transporter_obj = TransporterSchema.parse_obj(transporter)
            return transporter_obj

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transporter with email:'{transporter_email}' does not exists."
        )

    @logger.catch
    async def update_transporter_by_inn(self, transporter_inn: str, transporter: TransporterSchema) -> TransporterSchema:
        updated_transporter = TransporterSchema(
            inn=transporter_inn,
            kpp=transporter.kpp,
            ogrn=transporter.ogrn,
            name=transporter.name,
            date_of_formation=transporter.date_of_formation,
            director=transporter.director,
            legal_address=transporter.legal_address,
            address=transporter.address,
            email=transporter.email,
            telephone=transporter.telephone,
            payment_account=transporter.payment_account,
            corporate_account=transporter.corporate_account,
            updated_at=datetime.utcnow()
        )

        values = {**updated_transporter.dict()}
        values.pop("created_at")
        values.pop("inn")
        query = transporter_data.update().where(transporter_data.c.inn == transporter_inn).values(**values)
        await self.database.execute(query)

        logger.info(f"Transporter with inn:'{transporter_inn}' was updated.")
        return updated_transporter

    @logger.catch
    async def delete_transporter_by_inn(self, transporter_inn: str) -> dict:
        query = transporter_data.delete().where(transporter_data.c.inn == transporter_inn)
        await self.database.execute(query)

        logger.info(f"Transporter with inn:'{transporter_inn}' was deleted.")
        return {"message": f"Transporter with inn:'{transporter_inn}' was deleted."}
