from datetime import datetime
from sqlalchemy import and_

from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.transporter_contact import TransporterContactInSchema, TransporterContactOutSchema
from project.app.db.tables.transporter import transporter_contact
from project.app.helper.endpoint_answer import EndpointAnswer


class TransporterContactRepository(BaseRepository):

    @logger.catch
    async def get_transporter_contacts_by_inn(self, transporter_inn: str) -> EndpointAnswer:
        query = transporter_contact.select().where(transporter_contact.c.inn_transporter == transporter_inn)
        try:
            contact_list = await self.database.fetch_all(query)
            if contact_list:
                contact_list_obj = []
                for c in contact_list:
                    contact_list_obj.append(TransporterContactOutSchema.parse_obj(c))
                message = f"Contact with inn {transporter_inn} was found."
                result = EndpointAnswer(status="success", message=message, result=contact_list_obj)
                logger.info(message)
            else:
                message = f"Contact with inn {transporter_inn} was not found."
                result = EndpointAnswer(status="success", message=message)

        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def create_transporter_contact(self, contact: TransporterContactInSchema) -> EndpointAnswer:
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
        try:
            new_id = await self.database.execute(query)
            query = transporter_contact.select().where(transporter_contact.c.id == new_id)
            new_contact = await self.database.fetch_one(query)
            if not new_contact:
                message: str = "Contact can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = \
                    f"New contact with id:'{new_id}' for transporter with inn:'{contact.inn_transporter}' was created."
                logger.info(message)
                result = EndpointAnswer(status="success", message=message, result=new_contact)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_contact(
            self,
            contact_id: int,
            transporter_inn: str,
            contact: TransporterContactInSchema) -> EndpointAnswer:
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
        try:
            await self.database.execute(query)

            query = transporter_contact.select().where(
                and_(
                    transporter_contact.c.inn_transporter == transporter_inn,
                    transporter_contact.c.id == contact_id)
            )
            updated_contact = await self.database.fetch_one(query)
            message = f"Contact with id:{contact_id} for transporter with inn:'{transporter_inn}' was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_contact)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def delete_transporter_contact_by_id(self, contact_id: int) -> EndpointAnswer:
        query = transporter_contact.delete().where(transporter_contact.c.id == contact_id)
        try:
            await self.database.execute(query)
            message = f"Contact with id:'{contact_id}' was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result
