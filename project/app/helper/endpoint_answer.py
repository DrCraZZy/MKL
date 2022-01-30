from pydantic import BaseModel


class EndpointAnswer(BaseModel):
    status: str # success | fail
    message: str
    result: object
