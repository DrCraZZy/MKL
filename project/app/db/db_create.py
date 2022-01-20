from project.app.db.database import metadata, engine

from project.app.db.tables.customer import customer_data, customer_contract, customer_contact, customer_order
from project.app.db.tables.references import physical_property
from project.app.db.tables.transporter import transporter_data, transporter_contact, transporter_vehicle, \
    transporter_contract
from project.app.db.tables.deal import deal

metadata.create_all(bind=engine)