from project.app.repositories.base_repository import BaseRepository
from project.app.schema.customer import CustomerSchema
from project.app.db.tables.customer import customer_data


class CustomerRepository(BaseRepository):

    async def create_customer(self, customer: CustomerSchema) -> CustomerSchema:
        values = {**customer.dict()}
        query = customer_contact.insert().values(**values)
        await self.database.execute(query)

        return customer
