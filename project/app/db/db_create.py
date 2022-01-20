from project.app.db.database import metadata, engine

# functional tables
from project.app.db.tables.customer import customer_data, customer_contract, customer_contact, customer_order
from project.app.db.tables.references import physical_property
from project.app.db.tables.transporter import \
    transporter_data, \
    transporter_contact, \
    transporter_vehicle, \
    transporter_contract
from project.app.db.tables.deal import deal

# archive tables
from project.app.db.tables_archive.customer import \
    arc_customer_data, \
    arc_customer_contract, \
    arc_customer_contact, \
    arc_customer_order
from project.app.db.tables_archive.references import arc_physical_property
from project.app.db.tables_archive.transporter import \
    arc_transporter_data, \
    arc_transporter_contact, \
    arc_transporter_vehicle, \
    arc_transporter_contract
from project.app.db.tables_archive.deal import arc_deal

metadata.create_all(bind=engine)