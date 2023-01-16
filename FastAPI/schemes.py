from pydantic import BaseModel, Field
from typing import Optional

class Movies(BaseModel):
    id: Optional[int] = None
    title: str = Field(default = "alguna pelicula", min_length = 5, max_length = 15)
    overview: str = Field(default = "alguna descripcion", min_length = 15, max_length = 100)
    year: int = Field(default = 2022, le = 2022)
    rating: float = Field(default = 0.0, le = 5.0, ge = 0.0 )
    category: str = Field(default = "otras")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "mi pelicula",
				"overview": "descripcion de mi pelicula",
				"year": 2022,
				"rating": 9.8,
				"category": "ciencia ficcion"
            }
        }

