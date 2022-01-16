import uvicorn
from fastapi import FastAPI

from db.database import create_db, database
from project.app.endpoints import customer


def main():
    create_db()


app = FastAPI(title="MKL")
app.include_router(customer.router, prefix="/customers", tags=["customer"])


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
    uvicorn.run("main:app", reload=True)
