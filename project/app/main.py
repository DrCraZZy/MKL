import uvicorn
from fastapi import FastAPI

from project.app.db.database import database
from project.app.db import db_create  # crete all tables
from project.app.endpoints import customer, customer_order, customer_contact, loading_type, physical_property, \
    transporter



app = FastAPI(title="MKL")
app.include_router(customer.router, prefix="/customers", tags=["Customer"])
app.include_router(customer_order.router, prefix="/orders", tags=["Customer order"])
app.include_router(customer_contact.router, prefix="/customer_contact", tags=["Customer contact"])
app.include_router(loading_type.router, prefix="/loading_type", tags=["Loading type"])
app.include_router(physical_property.router, prefix="/physical_property", tags=["Physical property"])
app.include_router(transporter.router, prefix="/transporter", tags=["Transporter"])



@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
