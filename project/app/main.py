import uvicorn
from fastapi import FastAPI

from db.customer import customer_data, customer_contract, customer_contact, customer_order
from db.references import physical_properties
from db.transporter import transporter_data, transporter_contact, transporter_vehicles, transporter_contracts

from db.database import create_db, database


def main():
    create_db()


app = FastAPI(title="Employment exchange")


# app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    main()
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
