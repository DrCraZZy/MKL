from fastapi import APIRouter

router = APIRouter()

@router.get("/") # , response_model=list[Customer]
async def read_users():
    # users: CustomerRepository = Depends(get_user_repository),
    # limit: int = 100,
    # skip: int = 0):
    # return await users.get_all(limit=limit, skip=0)
    return {"Hello":"World"}