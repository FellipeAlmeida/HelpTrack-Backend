from pydantic import BaseModel
from typing import List

class CreateCategoryRequest(BaseModel):
    valor: str

class GetCategoryResponse(BaseModel):
    id: int
    valor: str

class ListCategoryResponse(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    items: List[GetCategoryResponse]

class EditCategoryRequest(BaseModel):
    valor: str