from typing import List
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy import and_

from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.transporter_contact import TransporterContactInSchema, TransporterContactOutSchema
from project.app.db.tables.transporter import transporter_contact


class TransporterContactRepository(BaseRepository):

    @logger.catch
    async def get_transporter_contacts_by_inn(self, transporter_inn: str) -> List[TransporterContactOutSchema]:
        query = transporter_contact.select().where(transporter_contact.c.inn_transporter == transporter_inn)
        contact_list = await self.database.fetch_all(query)

        if not contact_list:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"There is no contacts for transporter with inn:'{transporter_inn}'."
            )

        contact_list_obj = []
        for c in contact_list:
            contact_list_obj.append(TransporterContactOutSchema.parse_obj(c))

        return contact_list_obj

    @logger.catch
    async def create_transporter_contact(self, contact: TransporterContactInSchema) -> TransporterContactOutSchema:
        query = transporter_contact.insert().values(
            inn_transporter=contact.inn_transporter,
            name=contact.name,
            surname=contact.surname,
            patronymic=contact.patronymic,
            position=contact.position,
            telephone=contact.telephone,
            email=contact.email,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        new_id = await self.database.execute(query)
        query = transporter_contact.select().where(transporter_contact.c.id == new_id)
        new_contact = await self.database.fetch_one(query)

        if not new_contact:
            message: str = "Contact can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New contact with id:'{new_id}' for transporter with inn:'{contact.inn_transporter}' was created.")

        return TransporterContactOutSchema.parse_obj(new_contact)

    @logger.catch
    async def update_contact(
            self,
            contact_id: int,
            transporter_inn: str,
            contact: TransporterContactInSchema) -> TransporterContactOutSchema:
        query = transporter_contact. \
            update(). \
            where(and_(transporter_contact.c.id == contact_id,
                       transporter_contact.c.inn_transporter == transporter_inn)). \
            values(
                inn_transporter=contact.inn_transporter,
                name=contact.name,
                surname=contact.surname,
                patronymic=contact.patronymic,
                position=contact.position,
                telephone=contact.telephone,
                email=contact.email,
                updated_at=datetime.utcnow()
            )

        await self.database.execute(query)

        query = transporter_contact.select().where(
            and_(
                transporter_contact.c.inn_transporter == transporter_inn,
                transporter_contact.c.id == contact_id)
        )
        updated_contact = await self.database.fetch_one(query)

        logger.info(f"Contact with id:{contact_id} for transporter with inn:'{transporter_inn}' was updated.")
        return TransporterContactOutSchema.parse_obj(updated_contact)

    @logger.catch
    async def delete_transporter_contact_by_id(self, contact_id: int) -> dict:
        query = transporter_contact.delete().where(transporter_contact.c.id == contact_id)
        await self.database.execute(query)

        message = f"Contact with id:'{contact_id}' was deleted."
        logger.info(message)
        return {"message": message}
