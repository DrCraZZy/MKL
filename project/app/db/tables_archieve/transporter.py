from sqlalchemy import Table, Column, String, DateTime, Date, Integer, Float, Boolean
from project.app.db.database import metadata

transporter_data_arc = Table(
    "transporter_data_arc",
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
    Column("corporate_account", String),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

transporter_vehicle_arc = Table(
    "transporter_vehicle_arc",
    metadata,
    Column("id", Integer),
    Column("inn_transporter", String),
    Column("brand", String),
    Column("model", String),
    Column("dry_weight", Integer),
    Column("max_weight", Integer),
    Column("physical_property", Integer),
    Column("weight", Integer),
    Column("dimension", Float),
    Column("loading_type", Integer),
    Column("cost_up_to_100km", Float),
    Column("cost_up_to_500km", Float),
    Column("cost_up_to_1000km", Float),
    Column("is_available", Boolean),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

transporter_contract_arc = Table(
    "transporter_contract_arc",
    metadata,
    Column("contract_number", String),
    Column("inn_transporter", String),
    Column("transporter_vehicle_id", Integer),
    Column("start_date", DateTime),
    Column("end_date", DateTime),
    Column("loading_time", DateTime),
    Column("loading_address", String),
    Column("loading_coordinate", String),
    Column("delivery_address", String),
    Column("delivery_coordinate", String),
    Column("distance_km", Integer),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

transporter_contact_arc = Table(
    "transporter_contact_arc",
    metadata,
    Column("id", Integer),
    Column("inn_transporter", String),
    Column("name", String),
    Column("surname", String),
    Column("patronymic", String),
    Column("position", String),
    Column("telephone", String),
    Column("email", String),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)
