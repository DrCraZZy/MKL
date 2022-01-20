from sqlalchemy import Table, Column, String, DateTime, Date, Integer, ForeignKey, Float, Boolean
from datetime import datetime

from project.app.db.database import metadata

transporter_data = Table(
    "transporter_data",
    metadata,
    Column("inn", String, primary_key=True, unique=True, nullable=False),
    Column("kpp", String, unique=True, nullable=False),
    Column("ogrn", String, unique=True, nullable=False),
    Column("name", String, nullable=False),
    Column("date_of_formation", Date),
    Column("director", String),
    Column("legal_address", String),
    Column("address", String),
    Column("email", String, unique=True),
    Column("telephone", String),
    Column("payment_account", String),
    Column("corporate_account", String),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)

transporter_vehicle = Table(
    "transporter_vehicle",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("inn_transporter", String, ForeignKey("transporter_data.inn")),
    Column("brand", String),
    Column("model", String),
    Column("dry_weight", Integer),
    Column("max_weight", Integer),
    Column("physical_property", Integer, ForeignKey("physical_property.id")),
    Column("weight", Integer),
    Column("dimension", Float),
    Column("loading_type", Integer, ForeignKey("loading_type.id")),
    Column("cost_up_to_100km", Float),
    Column("cost_up_to_500km", Float),
    Column("cost_up_to_1000km", Float),
    Column("is_available", Boolean, default=True),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)

transporter_contract = Table(
    "transporter_contract",
    metadata,
    Column("contract_number", String, primary_key=True, unique=True),
    Column("inn_transporter", String, ForeignKey("transporter_data.inn")),
    Column("transporter_vehicle_id", Integer, ForeignKey("transporter_vehicle.id")),
    Column("start_date", DateTime),  # what does it mean
    Column("end_date", DateTime),  # what does it mean
    Column("loading_time", DateTime),
    Column("loading_address", String),
    Column("loading_coordinate", String),
    Column("delivery_address", String),
    Column("delivery_coordinate", String),
    Column("distance_km", Integer),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)

transporter_contact = Table(
    "transporter_contact",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("inn_transporter", String, ForeignKey("transporter_data.inn")),
    Column("name", String),
    Column("surname", String),
    Column("patronymic", String),
    Column("position", String),
    Column("telephone", String),
    Column("email", String),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)
