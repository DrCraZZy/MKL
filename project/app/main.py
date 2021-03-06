import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project.app.db.database import database
from project.app.db import db_create  # crete all tables
from project.app.endpoints import customer, customer_order, customer_contact, loading_type, physical_property, \
    transporter, transporter_contact, transporter_vehicle, load_capacity

app = FastAPI(title="MKL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer.router, prefix="/customers", tags=["Customer"])
app.include_router(customer_order.router, prefix="/orders", tags=["Customer order"])
app.include_router(customer_contact.router, prefix="/customer_contact", tags=["Customer contact"])
app.include_router(loading_type.router, prefix="/loading_type", tags=["Loading type"])
app.include_router(physical_property.router, prefix="/physical_property", tags=["Physical property"])
app.include_router(transporter.router, prefix="/transporter", tags=["Transporter"])
app.include_router(transporter_contact.router, prefix="/transporter_contact", tags=["Transporter contact"])
app.include_router(transporter_vehicle.router, prefix="/transporter_vehicle", tags=["Transporter vehicle"])
app.include_router(load_capacity.router, prefix="/load_capacity", tags=["Load capacity"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
