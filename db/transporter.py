from sqlalchemy import Table, Column, String, DateTime, Integer, ForeignKey, Float
from datetime import datetime

from .database import metadata

transporter_data = Table(
    "transporter_data",
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
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

transporter_vehicles = Table(
    "transporter_vehicles",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("INN_KPP_TRANSPORTER", String, ForeignKey("transporter_data.INN_KPP")),
    Column("BRAND", String),
    Column("MODEL", String),
    Column("DRY_WEIGHT", Integer),
    Column("MAX_WEIGHT", Integer),
    Column("PHYSICAL_PROPERTIES", Integer, ForeignKey("references.ID")),
    Column("WEIGHT", Integer),
    Column("DIMENSION", Float),
    Column("LOADING_TYPE", String),  # possible in ref table
    Column("COST_UP_TO_100km", Float),
    Column("COST_UP_TO_500km", Float),
    Column("COST_UP_TO_1000km", Float),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)

transporter_contract = Table(
    "transporter_contract",
    metadata,
    Column("CONTRACT_NUMBER", String, primary_key=True, unique=True),
    Column("INN_KPP_TRANSPORTER", String, ForeignKey("transporter_data.INN_KPP")),
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

transporter_contact = Table(
    "transporter_contact",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("INN_KPP_TRANSPORTER", String, ForeignKey("transporter_data.INN_KPP")),
    Column("NAME", String),
    Column("SURNAME", String),
    Column("PATRONYMIC", String),
    Column("POSITION", String),
    Column("TELEPHONE", String),
    Column("EMAIL", String),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)
