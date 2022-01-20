from sqlalchemy import Table, Column, Integer, String
from project.app.db.database import metadata

physical_property = Table(
    "physical_property",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("physical_properties", String),
    Column("description", String)
)

loading_type = Table(
    "loading_type",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("loading_type", String),
    Column("description", String)
)
