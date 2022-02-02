from project.app.repositories.customer import CustomerRepository
from project.app.repositories.customer_order import CustomerOrderRepository
from project.app.repositories.customer_contact import CustomerContactRepository
from project.app.repositories.loading_type import LoadingTypeRepository
from project.app.repositories.physical_property import PhysicalPropertyRepository
from project.app.repositories.transporter import TransporterRepository
from project.app.repositories.transporter_contact import TransporterContactRepository
from project.app.repositories.transporter_vehicle import TransporterVehicleRepository
from project.app.repositories.load_capacity import LoadCapacityRepository


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


def get_load_capacity_repository() -> LoadCapacityRepository:
    return LoadCapacityRepository(database=database)

def get_transporter_repository() -> TransporterRepository:
    return TransporterRepository(database=database)


def get_transporter_contact_repository() -> TransporterContactRepository:
    return TransporterContactRepository(database=database)


def get_transporter_vehicle_repository() -> TransporterVehicleRepository:
    return TransporterVehicleRepository(database=database)
