from datetime import datetime
from sqlalchemy import Table, Column, String, DateTime, Integer, ForeignKey
from project.app.db.database  import metadata

company_data = Table(
    "company_data",
    metadata,
    Column("inn_kpp", String, primary_key=True, unique=True, nullable=False),
    Column("ogrn", String, unique=True, nullable=False),
    Column("name", String, nullable=False),
    Column("date_of_formation", DateTime),
    Column("director", String),
    Column("legal_address", String, nullable=False),
    Column("address", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("telephone", String, nullable=False),
    Column("payment_account", String, nullable=False),
    Column("corporate_account", String, nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)

company_contracts = Table(
    "transporter_contracts",
    metadata,
    Column("contract_number", String, primary_key=True, unique=True, nullable=False),
    Column("order_id", String, ForeignKey("customer_orders.id"), nullable=False),
    Column("transporter_vehicle_id", Integer, ForeignKey("transporter_vehicles.id"), nullable=False),
    Column("start_date", DateTime),  # what does it mean
    Column("end_date", DateTime),  # what does it mean
    Column("loading_time", DateTime, nullable=False),
    Column("loading_address", String, nullable=False),
    Column("loading_coordinate", String),
    Column("delivery_address", String, nullable=False),
    Column("delivery_coordinate", String),
    Column("DISTANCE_KM", Integer, nullable=False),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

company_contact = Table(
    "customer_contacts",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True, nullable=False),
    Column("inn_kpp_company", String, ForeignKey("company_data.inn_kpp"), nullable=False),
    Column("name", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("patronymic", String),
    Column("position", String),
    Column("telephone", String),
    Column("email", String, nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)
