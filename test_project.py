import project
import requests

def test_movie_is_available():
    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "movies-and-serials-torrent.p.rapidapi.com"
    }
    response = requests.get("https://movies-and-serials-torrent.p.rapidapi.com/movies/latest", headers=headers)
    assert response.ok


def test_anime_is_available():
    response_romance = requests.get("https://animes3.p.rapidapi.com/romance")
    response_drama = requests.get("https://animes3.p.rapidapi.com/drama")
    response_action = requests.get("https://animes3.p.rapidapi.com/action")

    assert response_romance.ok
    assert response_drama.ok
    assert response_action.ok


def test_book_is_available():
    pass


def test_hobby_is_available():
    pass


def test_data_movie():
    pass


def test_data_anime():
    pass


def test_data_book():
    pass

def test_data_hobby():
    pass