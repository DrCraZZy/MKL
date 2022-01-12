from sqlalchemy import Table, String, DateTime, Column
from .database import metadata
import datetime

customer = Table(
    "customer",
    metadata,
    Column("INN_KPP", String, primary_key=True, unique=True),
    Column("OGRN", String, unique=True),
    Column("NAME", String),
    Column("DATE_OF_FORMATION", DateTime),
    Column("DIRECTOR", String),
    Column("LEGAL_ADDRESS", String),
    Column("ADDRESS", String),
    Column("EMAIL", String, unique=True),
    Column("TELEFONE", String),
    Column("TELEFONE", String),
    Column("PAYMENT_ACCOUNT", String),
    Column("Corporate Account", String),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)


