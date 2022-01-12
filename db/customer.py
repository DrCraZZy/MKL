from sqlalchemy import Table, Column, String, DateTime, Integer, ForeignKey, Float
from .database import metadata
import datetime


customer_data = Table(
    "customer_data",
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
    Column("Corporate Account", String),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)

customer_order = Table(
    "customer_orders",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True, ),
    Column("INN_KPP_CUSTOMER", String, ForeignKey("customer_data.INN_KPP")),
    Column("PHYSICAL_PROPERTIES", String),
    Column("WEIGHT", Integer),
    Column("DIMENSION", Float),
    Column("LOADING_TYPE", String),  # possible in ref table
    Column("LOADING_ADDRESS", String),
    Column("LOADING_COORDINATE", String),
    Column("DELIVERY_ADDRESS", String),
    Column("DELIVERY_COORDINATE", String),
    Column("DISTANCE_KM", Integer),
    Column("PRICE", Integer),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)

customer_contract = Table(
    "customer_contract",
    metadata,
    Column("CONTRACT_NUMBER", String, primary_key=True, unique=True),
    Column("INN_KPP_CUSTOMER", String, ForeignKey("customer_data.INN_KPP")),
    Column("CUSTOMER_ORDER_ID", Integer, ForeignKey("customer_orders.ID")),
    Column("START_DATE", DateTime),     # what does it mean
    Column("END_DATE", DateTime),       # what does it mean
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)

customer_contact = Table(
    "customer_contacts",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("INN_KPP_CUSTOMER", String, ForeignKey("customer_data.INN_KPP")),
    Column("NAME", String),
    Column("SURNAME", String),
    Column("PATRONYMIC", String),
    Column("POSITION", String),
    Column("TELEPHONE", String),
    Column("EMAIL", String),
    Column("CREATED_AT", DateTime, default=datetime.datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.datetime.utcnow)
)
