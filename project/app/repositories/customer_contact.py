from datetime import datetime
from sqlalchemy import and_

from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer_contact import CustomerContactInSchema, CustomerContactOutSchema
from project.app.db.tables.customer import customer_contact
from project.app.helper.endpoint_answer import EndpointAnswer


class CustomerContactRepository(BaseRepository):

    @logger.catch
    async def get_customer_contacts_by_inn(self, customer_inn: str) -> EndpointAnswer:
        query = customer_contact.select().where(customer_contact.c.inn_customer == customer_inn)
        try:
            contact_list = await self.database.fetch_all(query)
            if contact_list:
                contact_list_obj = []
                for c in contact_list:
                    contact_list_obj.append(CustomerContactOutSchema.parse_obj(c))
                message = f"Contact with inn {customer_inn} was found."
                result = EndpointAnswer(status="success", message=message, result=contact_list_obj)
                logger.info(message)
            else:
                message = f"Contact with inn {customer_inn} was not found."
                result = EndpointAnswer(status="success", message=message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))

        return result

    @logger.catch
    async def create_customer_contact(self, contact: CustomerContactInSchema) -> EndpointAnswer:
        query = customer_contact.insert().values(
            inn_customer=contact.inn_customer,
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
            query = customer_contact.select().where(customer_contact.c.id == new_id)
            new_contact = await self.database.fetch_one(query)
            if not new_contact:
                message: str = "Contact can't be inserted. Please try it again."
                logger.info(message)
                result = EndpointAnswer(status="success", message=message)
            else:
                message: str = \
                    f"New contact with id:'{new_id}' for customer with inn:'{contact.inn_customer}' was created."
                logger.info(message)
                result = EndpointAnswer(status="success", message=message, result=new_contact)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))

        return result

    @logger.catch
    async def update_contact(
            self,
            contact_id: int,
            customer_inn: str,
            contact: CustomerContactInSchema) -> EndpointAnswer:
        query = customer_contact. \
            update(). \
            where(and_(customer_contact.c.id == contact_id, customer_contact.c.inn_customer == customer_inn)). \
            values(
                inn_customer=contact.inn_customer,
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

            query = customer_contact.select().where(
                and_(
                    customer_contact.c.inn_customer == customer_inn,
                    customer_contact.c.id == contact_id)
            )
            updated_contact = await self.database.fetch_one(query)
            message = f"Contact with id:{contact_id} for customer with inn:'{customer_inn}' was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_contact)
            logger.info(message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))

        return result

    @logger.catch
    async def delete_customer_contact_by_id(self, contact_id: int) -> EndpointAnswer:
        query = customer_contact.delete().where(customer_contact.c.id == contact_id)
        try:
            await self.database.execute(query)
            message = f"Contact with id:'{contact_id}' was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))
        return result
