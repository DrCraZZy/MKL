from fastapi import APIRouter, Depends, status

from project.app.helper.endpoint_answer import EndpointAnswer
from project.app.repositories.customer_order import CustomerOrderRepository
from project.app.schema.customer_order import CustomerOrderInSchema, CustomerOrderUpdateSchema
from .depends import get_customer_order_repository

router = APIRouter()


@router.post("/", response_model=EndpointAnswer, status_code=status.HTTP_201_CREATED)
async def create_customer_order(
        order: CustomerOrderInSchema,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    answer: EndpointAnswer = await orders.create_customer_order(order)

    return answer


@router.get("/", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_all_order(
        limit: int = 100,
        skip: int = 0,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    answer: EndpointAnswer = await orders.get_all_orders(limit=limit, skip=skip)

    return answer


@router.get("/{customer_inn}", response_model=EndpointAnswer, status_code=status.HTTP_200_OK)
async def get_customer_orders_by_inn(
        customer_inn: str,
        limit: int = 100,
        skip: int = 0,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    answer: EndpointAnswer = await orders.get_customer_orders(customer_inn=customer_inn, limit=limit, skip=skip)

    return answer


@router.put("/", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def update_order(
        order_id: int,
        customer_inn: str,
        order: CustomerOrderUpdateSchema,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    answer: EndpointAnswer = await orders.update_order_by_id_by_inn(order_id=order_id, customer_inn=customer_inn,
                                                                    order=order)

    return answer


@router.delete("/{order_id}", response_model=EndpointAnswer, status_code=status.HTTP_202_ACCEPTED)
async def delete_customer_by_inn(
        order_id: int,
        orders: CustomerOrderRepository = Depends(get_customer_order_repository)):
    answer: EndpointAnswer = await orders.delete_order_by_id(order_id=order_id)

    return answer
