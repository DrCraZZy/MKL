from sqlalchemy import Table, Column, Integer, String, Float
from project.app.db.database import metadata

arc_physical_property = Table(
    "arc_physical_property",
    metadata,
    Column("id", Integer),
    Column("physical_properties", String),
    Column("description", String)
)

arc_loading_type = Table(
    "arc_loading_type",
    metadata,
    Column("id", Integer),
    Column("loading_type", String),
    Column("description", String)
)

arc_load_capacity = Table(
    "arc_load_capacity",
    metadata,
    Column("id", Integer),
    Column("weight_to", Float),
    Column("length_to", Float),
    Column("width_to", Float),
    Column("height_to", Float),
    Column("volume_to", Float)
)
