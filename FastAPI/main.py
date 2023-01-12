from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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
    }
]


@app.get('/', tags=['home'])  # ruta de la API
def message():
    return HTMLResponse('<h1>Hello World</h1>')  # mensaje


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movies(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return []


@app.get('/movies/', tags=['movies'])
def get_movies(category: str, year: int):
    for item in movies:
        if item['category'] == category and item['year'] == year:
            return item
    return []


@app.post('/movies', tags=['movies'])
# La funcion Body() permite enviar los datos como un payload o json en vez de campos query independientes
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({"id": id,
                   "title": title,
                   "overview": overview,
                   "year": year,
                   "rating": rating,
                   "category": category})

    return movies

@app.put('/movies', tags=['movies'])
def update_movie(id: int,
	title: str = Body(), 
	overview: str = Body(), 
	year: int = Body(), 
	rating: float = Body(), 
	category: str = Body()):

	for item in movies:
		if item['id'] == id:
			item["title"] =  title
			item["overview"] = overview
			item["year"] = year
			item["rating"] = rating
			item["category"] = category
			return movies

@app.delete('/movies', tags=['movies'])
def delete_movie(id: int):
	for item in movies:
		if item['id'] == id:
			movies.remove(item)
			return movies
