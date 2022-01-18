from sqlalchemy import Table, Column, ForeignKey, Integer, Boolean, DateTime
from datetime import datetime
from project.app.db.database import metadata


deals = Table(
    "deals",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, nullable=False),
    Column("transporter_vehicle_id", Integer, ForeignKey("transporter_vehicles.id")),
    Column("customer_order_id", Integer, ForeignKey("customer_orders.id"), unique=True),
    Column("customer_contract_id", Integer, ForeignKey("customer_contracts.id"), unique=True),
    Column("transporter_contract_id", Integer, ForeignKey("transporter_contracts.id"), unique=True),
    Column("is_finished", Boolean),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)
