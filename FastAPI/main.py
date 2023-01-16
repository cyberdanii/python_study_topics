from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from schemes import Movies
from typing import List

app = FastAPI()  # instanciacion
app.title = "Mi primera aplicacion con FastAPI"
app.version = "1.0.0"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
                "rating": 7.8,
                "category": "Acción"
    },
	{
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]


@app.get('/', tags=['home'])  # ruta de la API
def message():
    return HTMLResponse('<h1>Hello World</h1>')  # mensaje


@app.get('/movies', 
        tags=['movies'],
        response_model= List[Movies]) # indica que retorna una lista de objetos (json)
def get_movies():
    # return movies
    return JSONResponse(content=movies, status_code=200)


@app.get('/movies/{id}', tags=['movies'], response_model=Movies)
def get_movies(id: int = Path(ge = 1, le = 2000)):
    for item in movies:
        if item['id'] == id:
            # return item
            return JSONResponse(content=item)
    # return []
    return JSONResponse(content=[], status_code=404)


@app.get('/movies/', tags=['movies'])
def get_movies(category: str = Query(min_length = 5, max_length= 15)):
    for item in movies:
        if item['category'] == category:
            return item
    return []


# @app.post('/movies', tags=['movies'])
# # La funcion Body() permite enviar los datos como un payload o json en vez de campos query independientes
# def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     movies.append({"id": id,
#                    "title": title,
#                    "overview": overview,
#                    "year": year,
#                    "rating": rating,
#                    "category": category})

#     return movies

# @app.put('/movies', tags=['movies'])
# def update_movie(id: int,
# 	title: str = Body(), 
# 	overview: str = Body(), 
# 	year: int = Body(), 
# 	rating: float = Body(), 
# 	category: str = Body()):

# 	for item in movies:
# 		if item['id'] == id:
# 			item["title"] =  title
# 			item["overview"] = overview
# 			item["year"] = year
# 			item["rating"] = rating
# 			item["category"] = category
# 			return movies

@app.delete('/movies', tags=['movies'])
def delete_movie(id: int):
	for item in movies:
		if item['id'] == id:
			movies.remove(item)
			return movies

# ----------------------------------------
# Usando Esquemas para la manipulacion de datos

@app.post('/movies', tags=['movies'])
# La funcion Body() permite enviar los datos como un payload o json en vez de campos query independientes
def create_movie(movie: Movies):
    movies.append(movie)
    return movies

@app.put('/movies', tags=['movies'])
def update_movie(id: int, movie: Movies):

	for item in movies:
		if item['id'] == id:
			item["title"] =  movie.title
			item["overview"] = movie.overview
			item["year"] = movie.year
			item["rating"] = movie.rating
			item["category"] = movie.category
			return movies
