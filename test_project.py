import pytest

from project import data_movie, data_book, data_hobby
import requests


def test_data_movie():
    assert data_movie() != Exception

    data = data_movie()
    assert type(data) == tuple

    assert data[0].values() != ''
    assert data[1].values() != ''
    assert data[2].values() != ''
    assert data[3].values() != ''
    assert data[4].values() != ''


    assert data[0].get('Aliens') == 'https://m.media-amazon.com/images/M/MV5BZGU2OGY5ZTYtMWNhYy00NjZiLWI0NjUtZmNhY2JhNDRmODU3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UX380_CR0,14,380,562_.jpg'
    data_action_keys = list(data[0].keys())
    assert data_action_keys[0] == 'The Dark Knight'
    assert data_action_keys == ['The Dark Knight',
                                'The Good, the Bad and the Ugly',
                                'Fight Club',
                                'Inception',
                                'Seven Samurai',
                                'Saving Private Ryan',
                                'Terminator 2: Judgment Day',
                                'Psycho',
                                'LГ©on: The Professional',
                                'Gladiator',
                                'American History X',
                                'Harakiri',
                                'Once Upon a Time in the West',
                                'Rear Window',
                                'Indiana Jones and the Raiders of the Lost Ark',
                                'Django Unchained',
                                'Avengers: Infinity War',
                                'Aliens',
                                'Spider-Man: Into the Spider-Verse',
                                'The Dark Knight Rises',
                                'Oldboy',
                                'Inglourious Basterds',
                                'Top Gun: Maverick',
                                'High and Low',
                                'The Hunt',
                                'North by Northwest']

def test_data_book():
    assert data_book() != Exception

    data = data_book()
    assert type(data) == tuple

    assert data[0].values() != ''
    assert data[1].values() != ''
    assert data[2].values() != ''
    assert data[3].values() != ''

    assert data[2].get('The Canterbury Tales') == 'Geoffrey Chaucer'
    data_childrens_lit_keys = list(data[0].keys())
    assert data_childrens_lit_keys == ['Fairy tales', 'Pippi Longstocking', "Gulliver's Travels"]
    assert data_childrens_lit_keys[2] != ''

def test_data_hobby():
    #API response status code test
    url_general = "https://hobbies-by-api-ninjas.p.rapidapi.com/v1/hobbies"

    querystring = {"category": "general"}

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hobbies-by-api-ninjas.p.rapidapi.com"
    }

    response_text_genre_general = requests.request("GET", url_general, headers=headers, params=querystring)
    assert response_text_genre_general.status_code == 200

    url_education = "https://hobbies-by-api-ninjas.p.rapidapi.com/v1/hobbies"

    querystring = {"category": "education"}

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hobbies-by-api-ninjas.p.rapidapi.com"
    }

    response_text_genre_education = requests.request("GET", url_education, headers=headers, params=querystring)
    assert response_text_genre_education.status_code == 200

    url_competition = "https://hobbies-by-api-ninjas.p.rapidapi.com/v1/hobbies"

    querystring = {"category": "competition"}

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hobbies-by-api-ninjas.p.rapidapi.com"
    }

    response_text_genre_competition = requests.request("GET", url_competition, headers=headers, params=querystring)
    assert response_text_genre_competition.status_code == 200

    #data_hobby return test
    assert data_hobby() != Exception

    data = data_hobby()

    assert data[0].values() != ''
    assert data[1].values() != ''
    assert data[2].values() != ''

    data_keys = list(data[0].keys())
    assert data_keys == (['hobby', 'link', 'category'])
