from typing import List
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy import and_

from project.app.helper.log import logger
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer_contact import CustomerContactInSchema, CustomerContactOutSchema
from project.app.db.tables.customer import customer_contact


class CustomerContactRepository(BaseRepository):

    @logger.catch
    async def get_customer_contacts_by_inn(self, customer_inn: str) -> List[CustomerContactOutSchema]:
        query = customer_contact.select().where(customer_contact.c.inn_kpp_customer == customer_inn)
        contact_list = await self.database.fetch_all(query)

        if not contact_list:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"There is no contacts for customer with inn:'{customer_inn}'."
            )

        contact_list_obj = []
        for c in contact_list:
            contact_list_obj.append(CustomerContactOutSchema.parse_obj(c))

        return contact_list_obj

    @logger.catch
    async def create_customer_contact(self, contact: CustomerContactInSchema) -> CustomerContactOutSchema:
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
        new_id = await self.database.execute(query)
        query = customer_contact.select().where(customer_contact.c.id == new_id)
        new_order = await self.database.fetch_one(query)

        if not new_order:
            message: str = "Contact can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New contact with id:'{new_id}' for customer with inn:'{contact.inn_kpp_customer}' was created.")

        return CustomerContactOutSchema.parse_obj(new_order)

    @logger.catch
    async def update_contact(
            self,
            contact_id: int,
            customer_inn: str,
            contact: CustomerContactInSchema) -> CustomerContactOutSchema:
        query = customer_contact. \
            update(). \
            where(and_(customer_contact.c.id == contact_id, customer_contact.c.inn_kpp_customer == customer_inn)). \
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

        await self.database.execute(query)

        query = customer_contact.select().where(
            and_(
                customer_contact.c.inn_kpp_customer == customer_inn,
                customer_contact.c.id == contact_id)
        )
        updated_contact = await self.database.fetch_one(query)

        logger.info(f"Contact with id:{contact_id} for customer with inn:'{customer_inn}' was updated.")
        return CustomerContactOutSchema.parse_obj(updated_contact)

    @logger.catch
    async def delete_customer_contact_by_id(self, contact_id: int) -> dict:
        query = customer_contact.delete().where(customer_contact.c.id == contact_id)
        await self.database.execute(query)

        message = f"Contact with id:'{contact_id}' was deleted."
        logger.info(message)
        return {"message": message}
