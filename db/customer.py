from sqlalchemy import Table, Column, String, DateTime, Integer, ForeignKey, Float, Boolean
from .database import metadata
import datetime


customer_data = Table(
    "customer_data",
    metadata,
    Column("INN_KPP", String, primary_key=True, unique=True, nullable=False),
    Column("OGRN", String, unique=True, nullable=False),
    Column("NAME", String, nullable=False),
    Column("DATE_OF_FORMATION", DateTime),
    Column("DIRECTOR", String),
    Column("LEGAL_ADDRESS", String, nullable=False),
    Column("ADDRESS", String, nullable=False),
    Column("EMAIL", String, unique=True, nullable=False),
    Column("TELEPHONE", String),
    Column("PAYMENT_ACCOUNT", String, nullable=False),
    Column("CORPORATE_ACCOUNT", String, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)

customer_order = Table(
    "customer_orders",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("INN_KPP_CUSTOMER", String, ForeignKey("customer_data.INN_KPP"), nullable=False),
    Column("PHYSICAL_PROPERTIES", Integer, ForeignKey("physical_properties.ID")),
    Column("WEIGHT", Integer),
    Column("DIMENSION", Float),
    Column("LOADING_TYPE", Integer, ForeignKey("loading_type.ID")),
    Column("LOADING_ADDRESS", String, nullable=False),
    Column("LOADING_COORDINATE", String),
    Column("DELIVERY_ADDRESS", String, nullable=False),
    Column("DELIVERY_COORDINATE", String),
    Column("DISTANCE_KM", Integer, nullable=False),
    Column("PRICE", Integer, nullable=False),
    Column("IS_ACTIVE", Boolean, default=True),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)

customer_contract = Table(
    "customer_contract",
    metadata,
    Column("CONTRACT_NUMBER", String, primary_key=True, unique=True, nullable=False),
    Column("INN_KPP_CUSTOMER", String, ForeignKey("customer_data.INN_KPP"), nullable=False),
    Column("CUSTOMER_ORDER_ID", Integer, ForeignKey("customer_orders.ID"), nullable=False),
    Column("START_DATE", DateTime, nullable=False),
    Column("END_DATE", DateTime, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)

customer_contact = Table(
    "customer_contacts",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("INN_KPP_CUSTOMER", String, ForeignKey("customer_data.INN_KPP"), nullable=False),
    Column("NAME", String, nullable=False),
    Column("SURNAME", String, nullable=False),
    Column("PATRONYMIC", String),
    Column("POSITION", String),
    Column("TELEPHONE", String),
    Column("EMAIL", String, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)
