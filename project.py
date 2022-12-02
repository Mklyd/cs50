import requests
import json


def main():
    data_movie()
    data_anime()
    data_book()
    data_hobby()


def data_movie():
    url = "https://movies-and-serials-torrent.p.rapidapi.com/movies/latest"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "movies-and-serials-torrent.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    response_text = json.loads(response.text)
    response_text_title = []
    response_text_genres = []
    response_text_genre_action_title = []
    response_text_genre_romance_title = []
    response_text_genre_drama_title = []
    response_text_genre_any_title = []
    response_text_img = []
    response_text_action_img = []
    response_text_romance_img = []
    response_text_drama_img = []

    for i in response_text['data']['movies']:
        response_text_title.append(i['title'])
        response_text_genres.append(i['genres'])
        response_text_img.append(i['small_cover_image'])

    for j in range(len(response_text_genres)):
        if 'Action' in response_text_genres[j]:
            response_text_genre_action_title.append(response_text_title[j])
            response_text_action_img.append(response_text_img[j])
        if 'Romance' in response_text_genres[j]:
            response_text_genre_romance_title.append(response_text_title[j])
            response_text_romance_img.append(response_text_img[j])
        if 'Drama' in response_text_genres[j]:
            response_text_genre_drama_title.append(response_text_title[j])
            response_text_drama_img.append(response_text_img[j])
        else:
            response_text_genre_any_title.append(response_text_title[j])

    return [response_text_title, response_text_genre_action_title, response_text_genre_romance_title,
            response_text_genre_drama_title, response_text_genre_any_title, response_text_action_img,
            response_text_romance_img, response_text_drama_img]


def data_anime():
    url_romance = "https://animes3.p.rapidapi.com/romance"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "animes3.p.rapidapi.com"
    }

    response_text_genre_romance = requests.request("GET", url_romance, headers=headers)
    response_text_genre_romance = json.loads(response_text_genre_romance.text)

    url_drama = "https://animes3.p.rapidapi.com/drama"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "animes3.p.rapidapi.com"
    }

    response_text_genre_drama = requests.request("GET", url_drama, headers=headers)
    response_text_genre_drama = json.loads(response_text_genre_drama.text)

    url_action = "https://animes3.p.rapidapi.com/action"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "animes3.p.rapidapi.com"
    }

    response_text_genre_action = requests.request("GET", url_action, headers=headers)
    response_text_genre_action = json.loads(response_text_genre_action.text)

    response_text_genre_romance_title = [element['title'] for element in response_text_genre_romance]
    response_text_genre_drama_title = [element['title'] for element in response_text_genre_drama]
    response_text_genre_action_title = [element['title'] for element in response_text_genre_action]

    response_text_genre_romance_img = [element['img'] for element in response_text_genre_romance]
    response_text_genre_drama_img = [element['img'] for element in response_text_genre_drama]
    response_text_genre_action_img = [element['img'] for element in response_text_genre_action]

    return [[response_text_genre_romance_title, response_text_genre_drama_title, response_text_genre_action_title],
            [response_text_genre_romance_img, response_text_genre_drama_img, response_text_genre_action_img]]


def data_book():
    url_romance = "https://hapi-books.p.rapidapi.com/week/Romance"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    response_text_genre_romance = requests.request("GET", url_romance, headers=headers)
    response_text_genre_romance = json.loads(response_text_genre_romance.text)

    url_horror = "https://hapi-books.p.rapidapi.com/week/horror"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    response_text_genre_horror = requests.request("GET", url_horror, headers=headers)
    response_text_genre_horror = json.loads(response_text_genre_horror.text)

    url_detective = "https://hapi-books.p.rapidapi.com/week/detective"

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    response_text_genre_detective = requests.request("GET", url_detective, headers=headers)
    response_text_genre_detective = json.loads(response_text_genre_detective.text)

    response_text_genre_romance_title = [element['name'] for element in response_text_genre_romance]
    response_text_genre_horror_title = [element['name'] for element in response_text_genre_horror]
    response_text_genre_detective_title = [element['name'] for element in response_text_genre_detective]

    response_text_genre_romance_img = [element['cover'] for element in response_text_genre_romance]
    response_text_genre_horror_img = [element['cover'] for element in response_text_genre_horror]
    response_text_genre_detective_img = [element['cover'] for element in response_text_genre_detective]

    return [[response_text_genre_romance_title, response_text_genre_horror_title, response_text_genre_detective_title],
            [response_text_genre_romance_img, response_text_genre_horror_img, response_text_genre_detective_img]]


def data_hobby():
    url_general = "https://hobbies-by-api-ninjas.p.rapidapi.com/v1/hobbies"

    querystring = {"category": "general"}

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hobbies-by-api-ninjas.p.rapidapi.com"
    }

    response_text_genre_general = requests.request("GET", url_general, headers=headers, params=querystring)
    response_text_genre_general = json.loads(response_text_genre_general.text)

    url_education = "https://hobbies-by-api-ninjas.p.rapidapi.com/v1/hobbies"

    querystring = {"category": "education"}

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hobbies-by-api-ninjas.p.rapidapi.com"
    }

    response_text_genre_education = requests.request("GET", url_education, headers=headers, params=querystring)
    response_text_genre_education = json.loads(response_text_genre_education.text)

    url_competition = "https://hobbies-by-api-ninjas.p.rapidapi.com/v1/hobbies"

    querystring = {"category": "competition"}

    headers = {
        "X-RapidAPI-Key": "64bdc001f8msh7dbadeed104717ap10f90fjsnad82447fbf98",
        "X-RapidAPI-Host": "hobbies-by-api-ninjas.p.rapidapi.com"
    }

    response_text_genre_competition = requests.request("GET", url_competition, headers=headers, params=querystring)
    response_text_genre_competition = json.loads(response_text_genre_competition.text)

    return [response_text_genre_general, response_text_genre_education, response_text_genre_competition]


if __name__ == "__main__":
    main()
