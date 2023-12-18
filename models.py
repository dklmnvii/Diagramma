from pydantic import BaseModel


class new_id(BaseModel):
    code: int
    id: int