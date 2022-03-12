import math
from config import credentials, reduction
import requests


def requests_search(name: str) -> list:
    url = f"https://api.themoviedb.org/3/search/movie?api_key={credentials.API_KEY}&query={name}&language=en-US"
    res = requests.get(url).json()
    movies = dict()
    movies["response"] = dict()
    for el in res["results"]:
        movies["response"][el["id"]] = el["original_title"]
    return movies


def requests_movie(movie_id: int):
    try:
        movie_endpoint = (
            f"{credentials.API_BASE_URL}/movie/{movie_id}?api_key={credentials.API_KEY}"
        )
        credential_endpoint = f"{credentials.API_BASE_URL}/movie/{movie_id}/credits?api_key={credentials.API_KEY}"
        movie = requests.get(movie_endpoint)
        if movie.status_code != 200:
            mess = "the movie with {} does not exist".format(movie_id)
            raise Exception(mess)
        movie = movie.json()
        title = movie["title"]
        budget = movie["budget"]

        runtime = movie["runtime"]

        r = requests.get(credential_endpoint)
        if r.status_code != 200:
            mess = "the movie with {} does not exist".format(movie_id)
            raise Exception(mess)
        cast = r.json()["cast"]
        try:
            actors = [cast[i] for i in range(5)]
        except IndexError:
            actors = [cast[i] for i in range(len(cast))]
        pop_actors = sum([el["popularity"] for el in actors])
        crew = r.json()["crew"]

        directors = [
            crew[i] for i in range(len(crew)) if crew[i].get("job") == "Director"
        ]
        pop_directors = sum([el["popularity"] for el in directors])
        print(pop_directors)
        producers = [
            crew[i] for i in range(len(crew)) if crew[i].get("job") == "Producer"
        ]
        pop_producers = sum([el["popularity"] for el in producers])

        # reduction

        inputs = dict(
            movie_id=movie_id,
            title=title,
            budget=budget,
            runtime=runtime,
            pop_actors=pop_actors,
            pop_directors=pop_directors,
            pop_producer=pop_producers,
        )
        print(inputs)
        for key in reduction.AVERAGES.keys():
            inputs[key] = (inputs[key] - reduction.AVERAGES[key])/math.sqrt(reduction.VARIANCES[key])
        return {"response": inputs}
    except Exception as err:
        return {"error": str(err)}

requests_movie(557)