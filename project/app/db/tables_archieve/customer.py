from sqlalchemy import Table, Column, String, Date, DateTime, Integer, Float, Boolean
from project.app.db.database import metadata


customer_data_arc = Table(
    "customer_data_arc",
    metadata,
    Column("inn", String),
    Column("kpp", String),
    Column("ogrn", String),
    Column("name", String),
    Column("date_of_formation", Date),
    Column("director", String),
    Column("legal_address", String),
    Column("address", String),
    Column("email", String),
    Column("telephone", String),
    Column("payment_account", String),
    Column("corporate_account"),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

customer_order_arc = Table(
    "customer_order_arc",
    metadata,
    Column("id", Integer),
    Column("inn_customer", String),
    Column("physical_property", Integer),
    Column("weight", Integer),
    Column("dimension", Float),
    Column("loading_type", Integer),
    Column("loading_address", String),
    Column("loading_coordinate", String),
    Column("delivery_address", String),
    Column("delivery_coordinate", String),
    Column("distance_km", Integer),
    Column("price", Float),
    Column("is_active", Boolean),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

customer_contract_arc = Table(
    "customer_contract_arc",
    metadata,
    Column("contract_number", String),
    Column("inn_customer", String),
    Column("customer_order_id", Integer),
    Column("start_date", DateTime),
    Column("end_date", DateTime),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

customer_contact_arc = Table(
    "customer_contact_arc",
    metadata,
    Column("id", Integer),
    Column("inn_customer", String),
    Column("name", String),
    Column("surname", String),
    Column("patronymic", String),
    Column("position", String),
    Column("telephone", String),
    Column("email", String),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)
