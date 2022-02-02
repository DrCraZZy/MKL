from sqlalchemy import Table, Column, Integer, String, Float
from project.app.db.database import metadata

physical_property = Table(
    "physical_property",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("physical_property", String),
    Column("description", String)
)

loading_type = Table(
    "loading_type",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("loading_type", String),
    Column("description", String)
)

load_capacity = Table(
    "load_capacity",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("weight_to", Float),
    Column("length_to", Float),
    Column("width_to", Float),
    Column("height_to", Float),
    Column("volume_to", Float)
)
