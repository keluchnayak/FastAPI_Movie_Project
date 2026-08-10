from fastapi import FastAPI, Query, Body

app = FastAPI()

movies = [
    {
        "id": 1,
        "movie_name": "Inception",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 9
    },
    {
        "id": 2,
        "movie_name": "RRR",
        "genre": "Action",
        "language": "Telugu",
        "rating": 8
    },
    {
        "id": 3,
        "movie_name": "3 Idiots",
        "genre": "Comedy",
        "language": "Hindi",
        "rating": 9
    },
    {
        "id": 4,
        "movie_name": "Interstellar",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 10
    },
    {
        "id": 5,
        "movie_name": "Jersey",
        "genre": "Drama",
        "language": "Telugu",
        "rating": 8
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome to the Movie Explorer & Review Management System API",
        "status": "API is running successfully!"
    }

@app.get("/movies")
def get_all_movies():
    return movies

@app.post("/movies")
def add_movie(movie: dict = Body()):

    movies.append(movie)

    return {
        "message": "Movie added successfully",
        "movie": movie
    }



@app.get("/movies/filter")
def filter_movies(
    genre: str = Query(None),
    language: str = Query(None),
    rating: int = Query(None)
):
    filtered_movies = movies

    if genre:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie["genre"] == genre
        ]

    if language:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie["language"] == language
        ]

    if rating:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie["rating"] >= rating
        ]

    return filtered_movies



@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    return {"message": "Movie not found"}

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updated_movie: dict = Body()):

    for index, movie in enumerate(movies):

        if movie["id"] == movie_id:

            movies[index] = updated_movie

            return {
                "message": "Movie updated successfully",
                "movie": updated_movie
            }

    return {
        "message": "Movie not found"
    }


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    for index, movie in enumerate(movies):

        if movie["id"] == movie_id:

            deleted_movie = movies.pop(index)

            return {
                "message": "Movie deleted successfully",
                "movie": deleted_movie
            }

    return {
        "message": "Movie not found"
    }