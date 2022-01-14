from sqlalchemy import Table, Column, ForeignKey, Integer, Boolean, DateTime
from datetime import datetime
from project.app.db.database import metadata


deals = Table(
    "deals",
    metadata,
    Column("ID", Integer, primary_key=True, unique=True, nullable=False),
    Column("TRANSPORTER_VEHICLE_ID", Integer, ForeignKey("transporter_vehicles.ID")),
    Column("CUSTOMER_ORDER_ID", Integer, ForeignKey("customer_orders.ID"), unique=True),
    Column("CUSTOMER_CONTRACT_ID", Integer, ForeignKey("customer_contracts.ID"), unique=True),
    Column("TRANSPORTER_CONTRACT_ID", Integer, ForeignKey("transporter_contracts.ID"), unique=True),
    Column("IS_FINISHED", Boolean),
    Column("CREATED_AT", DateTime, default=datetime.utcnow),
    Column("UPDATED_AT", DateTime, default=datetime.utcnow)
)
