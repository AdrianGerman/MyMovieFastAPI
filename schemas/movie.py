from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default='Película',min_length=5, max_length=30)
    overview: str = Field(default='Descripción de la película', min_length=5, max_length=50)
    year: int = Field(default='2023', le=2023)
    rating: float = Field(examples=[3.2], ge=1.0, le=10.0)
    category: str = Field(default='Ciencia ficción', min_length=3, max_length=20)
    
    # Se ha comentado este codigo, ya que son 2 modos de hacer lo mismo que el default, pero mas
    # sencillo de editar, pero no ha funcionado como se espera, tiene un pequeño error visual,
    # estoy usando pydantic v2 y python 3.11.5
    
    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "id": 1,
    #                 "title": "Película",
    #                 "overview": "Descripción de la película",
    #                 "year": 2023,
    #                 "rating": 9.0,
    #                 "category": "Ciencia ficción",
    #             }
    #         ]
    #     }
    # }
    
    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "id": 1,
    #             "title": "Película",
    #             "overview": "Descripción de la película",
    #             "year": 2023,
    #             "rating": 9.0,
    #             "category": "Ciencia ficción",
    #         }
    #     }
