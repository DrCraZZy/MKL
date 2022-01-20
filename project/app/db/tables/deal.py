from sqlalchemy import Table, Column, String, ForeignKey, Integer, Boolean, DateTime
from datetime import datetime
from project.app.db.database import metadata


deal = Table(
    "deal",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, nullable=False),
    Column("transporter_vehicle_id", Integer, ForeignKey("transporter_vehicle.id")),
    Column("customer_order_id", Integer, ForeignKey("customer_order.id"), unique=True),
    Column("customer_contract_id", String, ForeignKey("customer_contract.contract_number"), unique=True),
    Column("transporter_contract_id", String, ForeignKey("transporter_contract.contract_number"), unique=True),
    Column("is_finished", Boolean),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)
