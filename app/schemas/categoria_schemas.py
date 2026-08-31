from pydantic import BaseModel

class CreateCategoryRequest(BaseModel):
    id: int
    valor: str