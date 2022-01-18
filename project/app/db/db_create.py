from project.app.db.database import metadata, engine

from project.app.db.tables.customer import customer_data, customer_contract, customer_contact, customer_order
from project.app.db.tables.references import physical_properties
from project.app.db.tables.transporter import transporter_data, transporter_contact, transporter_vehicles, \
    transporter_contracts

metadata.create_all(bind=engine)