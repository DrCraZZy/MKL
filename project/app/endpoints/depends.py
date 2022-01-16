from project.app.repositories.customers import CustomerRepository
from project.app.db.database import database


def get_customer_repository() -> CustomerRepository:
    return CustomerRepository(database=database)
