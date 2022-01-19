from typing import List
from fastapi import HTTPException, status
from datetime import datetime

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer import CustomerSchema
from project.app.db.tables.customer import customer_data
from project.app.helper.log import logger


class CustomerRepository(BaseRepository):

    @logger.catch
    async def create_customer(self, customer: CustomerSchema) -> CustomerSchema:
        values = {**customer.dict()}
        query = customer_data.insert().values(**values)
        await self.database.execute(query)

        # check for data insertion, is data with new inn_kpp in the table
        query = customer_data.select().where(customer_data.c.inn_kpp == customer.inn_kpp)
        data_set = await self.database.execute(query)

        if not data_set:
            message: str = "Customer can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New customer with inn:'{customer.inn_kpp}' was created.")
        return customer

    @logger.catch
    async def get_all_customers(self, limit: int = 100, skip: int = 0) -> List[CustomerSchema]:
        query = customer_data.select().limit(limit).offset(skip)
        customer_list = await self.database.fetch_all(query)
        customer_list_object = []
        for c in customer_list:
            customer_list_object.append(CustomerSchema.parse_obj(c))

        return customer_list_object

    @logger.catch
    async def get_customer_by_inn(self, customer_inn: str) -> CustomerSchema | None:
        query = customer_data.select().where(customer_data.c.inn_kpp == customer_inn).first()
        customer = await self.database.fetch_one(query=query)

        if customer:
            customer_obj = CustomerSchema.parse_obj(customer)
            return customer_obj

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with inn:'{customer_inn}' does not exists."
        )

    @logger.catch
    async def get_customer_by_email(self, customer_email: str) -> CustomerSchema | None:
        query = customer_data.select().where(customer_data.c.email == customer_email).first()
        customer = await self.database.fetch_one(query=query)

        if customer:
            customer_obj = CustomerSchema.parse_obj(customer)
            return customer_obj

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with email:'{customer_email}' does not exists."
        )

    @logger.catch
    async def update_customer_by_inn(self, customer_inn: str, customer: CustomerSchema) -> CustomerSchema:
        updated_customer = CustomerSchema(
            inn_kpp=customer_inn,
            ogrn=customer.ogrn,
            name=customer.name,
            date_of_formation=customer.date_of_formation,
            director=customer.director,
            legal_address=customer.legal_address,
            address=customer.address,
            email=customer.email,
            telephone=customer.telephone,
            payment_account=customer.payment_account,
            corporate_account=customer.corporate_account,
            updated_at=datetime.utcnow()
        )

        values = {**updated_customer.dict()}
        values.pop("created_at")
        values.pop("inn_kpp")
        query = customer_data.update().where(customer_data.c.inn_kpp == customer_inn).values(**values)
        await self.database.execute(query)

        logger.info(f"Customer with inn:'{customer_inn}' was updated.")
        return updated_customer

    @logger.catch
    async def delete_customer_by_inn(self, customer_inn: str) -> dict:
        query = customer_data.delete().where(customer_data.c.inn_kpp == customer_inn)
        await self.database.execute(query)

        logger.info(f"Customer with inn:'{customer_inn}' was deleted.")
        return {"message": f"Customer with inn:'{customer_inn}' was deleted."}
