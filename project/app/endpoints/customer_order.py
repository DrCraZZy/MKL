from typing import List
from fastapi import APIRouter, Depends, status

from .depends import get_customer_order_repository
from project.app.schema.customer_order import CustomerOrderOutSchema, CustomerOrderInSchema, CustomerOrderUpdateSchema
from project.app.repositories.customer_order import CustomerOrderRepository

router = APIRouter()


@router.post("/", response_model=CustomerOrderOutSchema, status_code=status.HTTP_201_CREATED)
async def create_customer_order(
        order: CustomerOrderInSchema,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    return await orders.create_customer_order(order)


@router.get("/", response_model=List[CustomerOrderOutSchema], status_code=status.HTTP_200_OK)
async def get_all_order(
        limit: int = 100,
        skip: int = 0,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    return await orders.get_all_orders(limit=limit, skip=skip)


@router.get("/{customer_inn}", response_model=List[CustomerOrderOutSchema], status_code=status.HTTP_200_OK)
async def get_customer_orders_by_inn(
        customer_inn: str,
        limit: int = 100,
        skip: int = 0,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    return await orders.get_customer_orders(customer_inn=customer_inn, limit=limit, skip=skip)


@router.put("/{order_id}/customer/{customer_inn}", response_model=CustomerOrderOutSchema, status_code=status.HTTP_201_CREATED)
async def update_order(
        order_id: int,
        customer_inn: str,
        order: CustomerOrderUpdateSchema,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    return await orders.update_order_by_id_by_inn(order_id=order_id, customer_inn=customer_inn, order=order)


@router.delete("/{order_id}", response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def delete_customer_by_inn(
        order_id: int,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    return await orders.delete_order_by_id(order_id=order_id)
