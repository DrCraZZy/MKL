from typing import List
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import and_

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer_order import CustomerOrderOutSchema, CustomerOrderInSchema
from project.app.db.tables.customer import customer_order
from project.app.helper.log import logger


class CustomerOrderRepository(BaseRepository):

    @logger.catch
    async def create_customer_order(self, order: CustomerOrderInSchema) -> CustomerOrderOutSchema:
        query = customer_order.insert().values(
            inn_customer=order.inn_customer,
            physical_properties=order.physical_properties,
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
        new_id = await self.database.execute(query)

        query = customer_order.select().where(customer_order.c.id == new_id)
        new_order = await self.database.fetch_one(query)

        if not new_order:
            message: str = "Order can't be inserted. Please try it again."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )

        logger.info(f"New order with id:'{new_id}' for customer with inn:'{order.inn_customer}' was created.")

        return CustomerOrderOutSchema.parse_obj(new_order)

    @logger.catch
    async def get_all_orders(self, limit: int = 100, skip: int = 0) -> List[CustomerOrderOutSchema]:
        query = customer_order.select().limit(limit).offset(skip)
        customer_list = await self.database.fetch_all(query)
        customer_list_object = []
        for c in customer_list:
            customer_list_object.append(CustomerOrderOutSchema.parse_obj(c))

        return customer_list_object

    @logger.catch
    async def get_customer_orders(self, customer_inn: str, limit: int = 100, skip: int = 0) -> \
            List[CustomerOrderOutSchema]:
        query = \
            customer_order. \
                select(). \
                where(customer_order.c.inn_kpp_customer == customer_inn). \
                limit(limit). \
                offset(skip)
        order_list = await self.database.fetch_all(query=query)

        if not order_list:
            message = f"Orders for customer with inn:'{customer_inn}' does not exists."
            logger.error(message)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message
            )

        order_list_object = []
        for o in order_list:
            order_list_object.append(CustomerOrderOutSchema.parse_obj(o))

        return order_list_object

    @logger.catch
    async def update_order_by_id_by_inn(self,
                                        order_id: int,
                                        customer_inn: str,
                                        order: CustomerOrderInSchema) -> CustomerOrderOutSchema:
        query = customer_order.update().where(
            and_(customer_order.c.inn_kpp_customer == customer_inn, customer_order.c.id == order_id)). \
            values(
            inn_customer=customer_inn,
            physical_properties=order.physical_properties,
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
        await self.database.execute(query)

        query = customer_order.select().where(
            and_(
                customer_order.c.inn_kpp_customer == customer_inn,
                customer_order.c.id == order_id)
        )
        updated_order = await self.database.fetch_one(query)

        logger.info(f"Order with id:{order_id} for customer with inn:'{customer_inn}' was updated.")
        return CustomerOrderOutSchema.parse_obj(updated_order)

    @logger.catch
    async def delete_order_by_id(self, order_id: int) -> dict:
        query = customer_order.delete().where(customer_order.c.id == order_id)
        await self.database.execute(query)

        message = f"Order with id:'{order_id}' was deleted."
        logger.info(message)
        return {"message": message}
