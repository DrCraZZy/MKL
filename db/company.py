from datetime import datetime
from sqlalchemy import Table, Column, String, DateTime, Integer, ForeignKey
from database import metadata

company_data = Table(
    "company_data",
    metadata,
    Column("INN_KPP", String, primary_key=True, unique=True, nullable=False),
    Column("OGRN", String, unique=True, nullable=False),
    Column("NAME", String, nullable=False),
    Column("DATE_OF_FORMATION", DateTime),
    Column("DIRECTOR", String),
    Column("LEGAL_ADDRESS", String, nullable=False),
    Column("ADDRESS", String, nullable=False),
    Column("EMAIL", String, unique=True, nullable=False),
    Column("TELEPHONE", String, nullable=False),
    Column("PAYMENT_ACCOUNT", String, nullable=False),
    Column("CORPORATE_ACCOUNT", String, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

company_contracts = Table(
    "transporter_contracts",
    metadata,
    Column("CONTRACT_NUMBER", String, primary_key=True, unique=True, nullable=False),
    Column("ORDER_ID", String, ForeignKey("customer_orders.ID"), nullable=False),
    Column("TRANSPORTER_VEHICLE_ID", Integer, ForeignKey("transporter_vehicles.ID"), nullable=False),
    Column("START_DATE", DateTime),  # what does it mean
    Column("END_DATE", DateTime),  # what does it mean
    Column("LOADING_TIME", DateTime, nullable=False),
    Column("LOADING_ADDRESS", String, nullable=False),
    Column("LOADING_COORDINATE", String),
    Column("DELIVERY_ADDRESS", String, nullable=False),
    Column("DELIVERY_COORDINATE", String),
    Column("DISTANCE_KM", Integer, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

company_contact = Table(
    "customer_contacts",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("INN_KPP_COMPANY", String, ForeignKey("company_data.INN_KPP"), nullable=False),
    Column("NAME", String, nullable=False),
    Column("SURNAME", String, nullable=False),
    Column("PATRONYMIC", String),
    Column("POSITION", String),
    Column("TELEPHONE", String),
    Column("EMAIL", String, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)
