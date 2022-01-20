from sqlalchemy import Table, Column, Integer, String
from project.app.db.database import metadata

physical_property_arc = Table(
    "physical_property_arc",
    metadata,
    Column("id", Integer),
    Column("physical_properties", String),
    Column("description", String)
)

loading_type_arc = Table(
    "loading_type_arc",
    metadata,
    Column("id", Integer),
    Column("loading_type", String),
    Column("description", String)
)
