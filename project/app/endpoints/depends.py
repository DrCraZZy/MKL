from project.app.repositories.customer import CustomerRepository
from project.app.repositories.customer_order import CustomerOrderRepository
from project.app.repositories.customer_contact import CustomerContactRepository
from project.app.repositories.loading_type import LoadingTypeRepository
from project.app.repositories.physical_property import PhysicalPropertyRepository

from project.app.db.database import database


def get_customer_repository() -> CustomerRepository:
    return CustomerRepository(database=database)


def get_customer_order_repository() -> CustomerOrderRepository:
    return CustomerOrderRepository(database=database)


def get_customer_contact_repository() -> CustomerContactRepository:
    return CustomerContactRepository(database=database)


def get_loading_type_repository() -> LoadingTypeRepository:
    return LoadingTypeRepository(database=database)


def get_physical_property_repository() -> PhysicalPropertyRepository:
    return PhysicalPropertyRepository(database=database)
