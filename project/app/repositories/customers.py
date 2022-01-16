from project.app.repositories.base_repository import BaseRepository
from project.app.models.customer import CustomerIn, CustomerOut
from project.app.db.tables.customer import customer_contact

class CustomerRepository(BaseRepository):
    
    async def create_customer(self, c: CustomerIn) -> CustomerOut:
        customer = CustomerOut(
            inn_kpp=c.inn_kpp,
            ogrn=c.ogrn,
            name=c.name,
            date_of_formation=c.date_of_formation,
            director=c.director,
            legal_address=c.legal_address,
            address=c.address,
            email=c.email,
            telephone=c.telephone,
            payment_account=c.payment_account,
            corporate_account=c.corporate_account
        )
        values = {**customer.dict()}
        query = customer_contact.insert().values(**values)
        await self.database.execute(query)

        return customer
