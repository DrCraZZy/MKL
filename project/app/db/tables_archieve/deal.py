from sqlalchemy import Table, Column, String, Integer, Boolean, DateTime
from project.app.db.database import metadata


deal_arc = Table(
    "deal_arc",
    metadata,
    Column("id", Integer),
    Column("transporter_vehicle_id", Integer),
    Column("customer_order_id", Integer),
    Column("customer_contract_id", String),
    Column("transporter_contract_id", String),
    Column("is_finished", Boolean),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)
