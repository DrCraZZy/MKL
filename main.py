from db.customer import customer_data, customer_contract, customer_contact, customer_order
from db.references import physical_properties
from db.transporter import transporter_data, transporter_contact, transporter_vehicles, transporter_contracts

from db.database import create_db

def main():
    create_db()

if __name__ == '__main__':
    main()
