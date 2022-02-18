from fastapi import APIRouter

from project.app.schema.token import Token, Login

router = APIRouter()


@router.post("/", response_model=Token)
async def login(login: Login, ):
    return
