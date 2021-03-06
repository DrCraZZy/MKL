from datetime import datetime
from sqlalchemy import and_

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer_order import CustomerOrderOutSchema, CustomerOrderInSchema, CustomerOrderUpdateSchema
from project.app.db.tables.customer import customer_order
from project.app.helper.log import logger
from project.app.helper.endpoint_answer import EndpointAnswer


class CustomerOrderRepository(BaseRepository):

    @logger.catch
    async def create_customer_order(self, order: CustomerOrderInSchema) -> EndpointAnswer:
        query = customer_order.insert().values(
            inn_customer=order.inn_customer,
            physical_property=order.physical_property,
            weight=order.weight,
            dimension=order.dimension,
            loading_type=order.loading_type,
            loading_address=order.loading_address,
            loading_coordinate=order.loading_coordinate,
            delivery_address=order.delivery_address,
            delivery_coordinate=order.delivery_coordinate,
            distance_km=order.distance_km,
            price=order.price,
            is_active=order.is_active,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow())

        try:
            new_id = await self.database.execute(query)
            query = customer_order.select().where(customer_order.c.id == new_id)
            new_order = await self.database.fetch_one(query)

            if not new_order:
                message: str = "Order can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = f"New order with id:'{new_id}' for customer with inn:'{order.inn_customer}' was created."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_all_orders(self, limit: int = 100, skip: int = 0) -> EndpointAnswer:
        query = customer_order.select().limit(limit).offset(skip)

        try:
            customer_list = await self.database.fetch_all(query)
            customer_list_object = []
            for c in customer_list:
                customer_list_object.append(CustomerOrderOutSchema.parse_obj(c))
            message: str = "List of orders is created."
            result = EndpointAnswer(status="success", message=message, result=customer_list_object)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_customer_orders(self, customer_inn: str, limit: int = 100, skip: int = 0) -> \
            EndpointAnswer:
        query = customer_order.select().where(customer_order.c.inn_customer == customer_inn).limit(limit).offset(skip)
        try:
            order_list = await self.database.fetch_all(query=query)
            if not order_list:
                message = f"Orders for customer with inn:'{customer_inn}' does not exists."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                order_list_object = []
                for o in order_list:
                    order_list_object.append(CustomerOrderOutSchema.parse_obj(o))
                message = f"There are '{len(order_list_object)}' order(s) for customer with inn:'{customer_inn}'"
                result = EndpointAnswer(status="success", message=message, result=order_list_object)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_order_by_id_by_inn(self,
                                        order_id: int,
                                        customer_inn: str,
                                        order: CustomerOrderUpdateSchema) -> EndpointAnswer:
        query = customer_order.update().where(
            and_(customer_order.c.inn_customer == customer_inn, customer_order.c.id == order_id)). \
            values(
                inn_customer=customer_inn,
                physical_property=order.physical_property,
                weight=order.weight,
                dimension=order.dimension,
                loading_type=order.loading_type,
                loading_address=order.loading_address,
                loading_coordinate=order.loading_coordinate,
                delivery_address=order.delivery_address,
                delivery_coordinate=order.delivery_coordinate,
                distance_km=order.distance_km,
                price=order.price,
                is_active=order.is_active,
                updated_at=datetime.utcnow()
            )
        try:
            await self.database.execute(query)

            query = customer_order.select().where(
                and_(
                    customer_order.c.inn_customer == customer_inn,
                    customer_order.c.id == order_id)
            )
            updated_order = await self.database.fetch_one(query)

            message: str = f"Order with id:{order_id} for customer with inn:'{customer_inn}' was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_order)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def delete_order_by_id(self, order_id: int) -> EndpointAnswer:
        query = customer_order.delete().where(customer_order.c.id == order_id)
        try:
            await self.database.execute(query)
            message: str = f"Order with id:'{order_id}' was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result
