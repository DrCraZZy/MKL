from project.app.repositories.customers import CustomerRepository
from project.app.repositories.customer_order import CustomerOrderRepository
from project.app.repositories.customer_contact import CustomerContactRepository
from project.app.db.database import database


def get_customer_repository() -> CustomerRepository:
    return CustomerRepository(database=database)


def get_customer_order_repository() -> CustomerOrderRepository:
    return CustomerOrderRepository(database=database)


def get_customer_contact_repository() -> CustomerContactRepository:
    return CustomerContactRepository(database=database)
