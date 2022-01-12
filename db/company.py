from datetime import datetime
from sqlalchemy import Table, Column, String, DateTime, Integer, ForeignKey
from database import metadata

company_data = Table(
    "company_data",
    metadata,
    Column("INN_KPP", String, primary_key=True, unique=True),
    Column("OGRN", String, unique=True),
    Column("NAME", String),
    Column("DATE_OF_FORMATION", DateTime),
    Column("DIRECTOR", String),
    Column("LEGAL_ADDRESS", String),
    Column("ADDRESS", String),
    Column("EMAIL", String, unique=True),
    Column("TELEPHONE", String),
    Column("PAYMENT_ACCOUNT", String),
    Column("CORPORATE_ACCOUNT", String),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

company_contracts = Table(
    "transporter_contracts",
    metadata,
    Column("CONTRACT_NUMBER", String, primary_key=True, unique=True),
    Column("ORDER_ID", String, ForeignKey("customer_orders.ID")),
    Column("TRANSPORTER_VEHICLE_ID", Integer, ForeignKey("transporter_vehicles.ID")),
    Column("START_DATE", DateTime),  # what does it mean
    Column("END_DATE", DateTime),  # what does it mean
    Column("LOADING_TIME", DateTime),
    Column("LOADING_ADDRESS", String),
    Column("LOADING_COORDINATE", String),
    Column("DELIVERY_ADDRESS", String),
    Column("DELIVERY_COORDINATE", String),
    Column("DISTANCE_KM", Integer),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

company_contact = Table(
    "customer_contacts",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("INN_KPP_COMPANY", String, ForeignKey("company_data.INN_KPP")),
    Column("NAME", String),
    Column("SURNAME", String),
    Column("PATRONYMIC", String),
    Column("POSITION", String),
    Column("TELEPHONE", String),
    Column("EMAIL", String),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)
