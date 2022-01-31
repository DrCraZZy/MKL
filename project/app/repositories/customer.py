from datetime import datetime

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer import CustomerSchema, CustomerOutSchema
from project.app.db.tables.customer import customer_data
from project.app.helper.log import logger
from project.app.helper.endpoint_answer import EndpointAnswer


class CustomerRepository(BaseRepository):

    @logger.catch
    async def create_customer(self, customer: CustomerSchema) -> EndpointAnswer:
        query = customer_data.insert().values(
            inn=customer.inn,
            kpp=customer.kpp,
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
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        try:
            await self.database.execute(query)
            # check for data insertion, is data with new inn in the table
            query = customer_data.select().where(customer_data.c.inn == customer.inn)
            new_customer = await self.database.fetch_one(query)
            message = f"New customer with inn:'{customer.inn}' was created."
            result = EndpointAnswer(status="success", message=message, obj=CustomerOutSchema.parse_obj(new_customer))
            logger.info(message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))

        return result

    @logger.catch
    async def get_all_customers(self, limit: int = 100, skip: int = 0) -> EndpointAnswer:
        query = customer_data.select().limit(limit).offset(skip)
        try:
            customer_list = await self.database.fetch_all(query)
            customer_list_object = []
            for c in customer_list:
                customer_list_object.append(CustomerSchema.parse_obj(c))
            result = EndpointAnswer(status="success",
                                    message=f"Customer list was returned. ({len(customer_list_object)})",
                                    result=customer_list_object)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))

        return result

    @logger.catch
    async def get_customer_by_inn(self, customer_inn: str) -> EndpointAnswer:
        query = customer_data.select().where(customer_data.c.inn == customer_inn)
        try:
            customer = await self.database.fetch_one(query=query)
            if customer:
                customer_obj = CustomerSchema.parse_obj(customer)
                result = EndpointAnswer(status="success", message=f"Customer with {customer_inn} was found'",
                                        result=customer_obj)
            else:
                result = EndpointAnswer(status="success", message=f"Customer with '{customer_inn}' was not found")
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
        return result

    @logger.catch
    async def get_customer_by_email(self, customer_email: str) -> EndpointAnswer:
        query = customer_data.select().where(customer_data.c.email == customer_email).first()
        result = None
        try:
            customer = await self.database.fetch_one(query=query)

            if customer:
                message = f"Return customer with email {customer_email}"
                customer_obj = CustomerSchema.parse_obj(customer)
                result = EndpointAnswer(status="success", message=message, result=customer_obj)
                logger.info(message)
            else:
                message = f"There is no customer with email {customer_email}"
                result = EndpointAnswer(status="success", message=message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))
        return result

    @logger.catch
    async def update_customer_by_inn(self, customer_inn: str, customer: CustomerSchema) -> EndpointAnswer:
        updated_customer = CustomerSchema(
            inn=customer_inn,
            kpp=customer.kpp,
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
        values.pop("inn")
        query = customer_data.update().where(customer_data.c.inn == customer_inn).values(**values)

        try:
            await self.database.execute(query)
            message = f"Customer with inn:'{customer_inn}' was updated."
            logger.info(message)
            result = EndpointAnswer(status="success",
                                    message=message,
                                    result=updated_customer)
            logger.info(message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
            logger.error(str(e))
        return result

    @logger.catch
    async def delete_customer_by_inn(self, customer_inn: str) -> EndpointAnswer:
        query = customer_data.delete().where(customer_data.c.inn == customer_inn)
        try:
            await self.database.execute(query)
            message = f"Customer with inn:'{customer_inn}' was deleted."
            logger.info(message)
            result = EndpointAnswer(status="success", message=message)
        except Exception as e:
            result = EndpointAnswer(status="fail", message=str(e))
        return result
