import os

from sympy import EX
from config import credentials
import requests
import re


def find_file(fullname, extension, path=""):
    """find a notebook, given its name and an optional path
    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.
    """
    name = fullname.rsplit(".", 1)[-1]
    FILE_PATH = file_path(name, extension, path=path)
    if os.path.isfile(FILE_PATH):
        print("The file was found: ")
        return FILE_PATH
    # let import Notebook_Name find "Notebook Name.ipynb"

    name = name.replace("_", " ")
    FILE_PATH = file_path(name, extension, path=path)
    if os.path.isfile(FILE_PATH):
        print("The file was found: ")
        return FILE_PATH
    print("no such file")


def file_path(name, extension=".ipynb", path=""):
    fullpath = path + "%s" % (name + extension)
    ROOT_PATH = os.path.dirname(os.path.abspath(fullpath))
    return os.path.join(ROOT_PATH, name + extension)


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
        revenue = movie["revenue"]
        genres = [movie["genres"][i].get("name") for i in range(len(movie["genres"]))]
        # original_language = movie["original_language"]
        overview = movie["overview"]
        # production_companies = [
        #     movie["production_companies"][i].get("name")
        #     for i in range(len(movie["production_companies"]))
        # ]
        # release_date = movie["release_date"]

        runtime = movie["runtime"]
        vote_average = movie["vote_average"]
        vote_count = movie["vote_count"]

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
        producers = [
            crew[i] for i in range(len(crew)) if crew[i].get("job") == "Producer"
        ]
        pop_producers = sum([el["popularity"] for el in producers])
        inputs = dict(
            movie_id=movie_id,
            title=title,
            budget=budget,
            genres=genres,
            revenue=revenue,
            runtime=runtime,
            vote_average=vote_average,
            vote_count=vote_count,
            pop_actors=pop_actors,
            pop_directors=pop_directors,
            pop_producers=pop_producers,
        )

        return {"response": inputs}
    except Exception as err:
        return {"error": str(err)}
