from pydantic import BaseModel


class LoadingTypeInSchema(BaseModel):
    loading_type: str
    description: str


class LoadingTypeOutSchema(LoadingTypeInSchema):
    id: int
