from sqlalchemy import Table, Column, Integer, String
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
