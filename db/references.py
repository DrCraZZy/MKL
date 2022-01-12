from sqlalchemy import Table, Column, Integer, String
from .database import metadata

physical_properties = Table(
    "physical_properties",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("PHYSICAL_PROPERTIES", String),
    Column("Description", String)
)