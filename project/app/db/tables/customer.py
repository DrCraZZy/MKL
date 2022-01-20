from sqlalchemy import Table, Column, String, Date, DateTime, Integer, ForeignKey, Float, Boolean
from project.app.db.database import metadata
import datetime


customer_data = Table(
    "customer_data",
    metadata,
    Column("inn", String, primary_key=True, unique=True, nullable=False),
    Column("kpp", String, unique=True, nullable=False),
    Column("ogrn", String, unique=True, nullable=False),
    Column("name", String, nullable=False),
    Column("date_of_formation", Date),
    Column("director", String),
    Column("legal_address", String, nullable=False),
    Column("address", String, nullable=False),
    Column("email", String, nullable=False),
    Column("telephone", String),
    Column("payment_account", String, nullable=False),
    Column("corporate_account", String, nullable=False),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)

customer_order = Table(
    "customer_order",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("inn_customer", String, ForeignKey("customer_data.inn"), nullable=False),
    Column("physical_property", Integer, ForeignKey("physical_property.id"), nullable=False),
    Column("weight", Integer),
    Column("dimension", Float),
    Column("loading_type", Integer, ForeignKey("loading_type.id"), nullable=False),
    Column("loading_address", String, nullable=False),
    Column("loading_coordinate", String),
    Column("delivery_address", String, nullable=False),
    Column("delivery_coordinate", String),
    Column("distance_km", Integer, nullable=False),
    Column("price", Float, nullable=False),
    Column("is_active", Boolean, default=True),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)

customer_contract = Table(
    "customer_contract",
    metadata,
    Column("contract_number", String, primary_key=True, unique=True, nullable=False),
    Column("inn_customer", String, ForeignKey("customer_data.inn"), nullable=False),
    Column("customer_order_id", Integer, ForeignKey("customer_order.id"), nullable=False),
    Column("start_date", DateTime, nullable=False),
    Column("end_date", DateTime, nullable=False),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)

customer_contact = Table(
    "customer_contact",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("inn_customer", String, ForeignKey("customer_data.inn"), nullable=False),
    Column("name", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("patronymic", String),
    Column("position", String),
    Column("telephone", String),
    Column("email", String, nullable=False),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)
