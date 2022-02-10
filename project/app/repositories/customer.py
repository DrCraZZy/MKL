from datetime import datetime

from project.app.helper.message_parser import parse_message
from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer import CustomerSchema, CustomerOutSchema
from project.app.db.tables.customer import customer_data
from project.app.helper.log import logger
from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.helper.check_data import is_inn_exists


class CustomerRepository(BaseRepository):

    @logger.catch
    async def create_customer(self, customer: CustomerSchema) -> EndpointAnswer:
        if not await is_inn_exists(customer.inn, customer_data, self.database):
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
                result = EndpointAnswer(status="success",
                                        message=message,
                                        result=CustomerOutSchema.parse_obj(new_customer))
                logger.info(message)
            except Exception as e:
                message: str = parse_message(str(e))
                result = EndpointAnswer(status="fail", message=message)
                logger.error(message)
        else:
            message = f"There is already customer with inn:'{customer.inn}' in the table."
            result = EndpointAnswer(status="fail", message=message)
            logger.info(message)
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
            message: str = parse_message(str(e))
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_customer_by_inn(self, customer_inn: str) -> EndpointAnswer:
        query = customer_data.select().where(customer_data.c.inn == customer_inn)
        try:
            customer = await self.database.fetch_one(query=query)
            if customer:
                customer_obj = CustomerSchema.parse_obj(customer)
                message: str = f"Customer with {customer_inn} was found'"
                result = EndpointAnswer(status="success", message=message, result=customer_obj)
                logger.info(message)
            else:
                message: str = f"Customer with '{customer_inn}' was not found"
                result = EndpointAnswer(status="fail", message=message)
                logger.info(message)
        except Exception as e:
            message: str = parse_message(str(e))
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)
        return result

    @logger.catch
    async def get_customer_by_email(self, customer_email: str) -> EndpointAnswer:
        query = customer_data.select().where(customer_data.c.email == customer_email).first()
        try:
            customer = await self.database.fetch_one(query=query)

            if customer:
                customer_obj = CustomerSchema.parse_obj(customer)
                message = f"Return customer with email {customer_email}"
                result = EndpointAnswer(status="success", message=message, result=customer_obj)
                logger.info(message)
            else:
                message = f"There is no customer with email {customer_email}"
                result = EndpointAnswer(status="fail", message=message)
                logger.info(message)
        except Exception as e:
            message: str = parse_message(str(e))
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)
        return result

    @logger.catch
    async def update_customer_by_inn(self, customer_inn: str, customer: CustomerSchema) -> EndpointAnswer:
        if await is_inn_exists(customer.inn, customer_data, self.database):
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
                result = EndpointAnswer(status="success", message=message, result=updated_customer)
                logger.info(message)
            except Exception as e:
                message: str = parse_message(str(e))
                result = EndpointAnswer(status="fail", message=message)
                logger.error(message)
        else:
            message = f"There is no customer with inn:'{customer_inn}' for update in the table."
            result = EndpointAnswer(status="fail", message=message)
            logger.info(message)
        return result

    @logger.catch
    async def delete_customer_by_inn(self, customer_inn: str) -> EndpointAnswer:
        if await is_inn_exists(customer_inn, customer_data, self.database):
            query = customer_data.delete().where(customer_data.c.inn == customer_inn)
            try:
                await self.database.execute(query)
                message = f"Customer with inn:'{customer_inn}' was deleted."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            except Exception as e:
                message: str = parse_message(str(e))
                result = EndpointAnswer(status="fail", message=message)
                logger.info(message)
        else:
            message = f"There is no customer with inn:'{customer_inn}' in the table."
            result = EndpointAnswer(status="fail", message=message)
            logger.info(message)
        return result
