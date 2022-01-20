from sqlalchemy import Table, Column, String, DateTime, Date, Integer
from project.app.db.database  import metadata

company_data_arc = Table(
    "company_data_arc",
    metadata,
    Column("inn", String),
    Column("kpp", String),
    Column("ogrn", String),
    Column("name", String),
    Column("date_of_formation", Date),
    Column("director", String),
    Column("legal_address", String),
    Column("address", String),
    Column("email", String),
    Column("telephone", String),
    Column("payment_account", String),
    Column("corporate_account", String),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)

company_contract_arc = Table(
    "transporter_contract_arc",
    metadata,
    Column("contract_number", String),
    Column("order_id", String),
    Column("transporter_vehicle_id", Integer),
    Column("start_date", DateTime),
    Column("end_date", DateTime),
    Column("loading_time", DateTime),
    Column("loading_address", String),
    Column("loading_coordinate", String),
    Column("delivery_address", String),
    Column("delivery_coordinate", String),
    Column("DISTANCE_KM", Integer),
    Column("CREATED_AT", DateTime),
    Column("UPDATED_AT", DateTime)
)

company_contact_arc = Table(
    "customer_contact_arc",
    metadata,
    Column("id", Integer),
    Column("inn_company", String,),
    Column("name", String),
    Column("surname", String),
    Column("patronymic", String),
    Column("position", String),
    Column("telephone", String),
    Column("email", String),
    Column("created_at", DateTime),
    Column("updated_at", DateTime)
)
