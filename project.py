import requests
import json

def main():
    data_movie()
    data_book()
    data_hobby()


def data_movie():
    try:
        with open('data/movie_data.json') as movie_data_json:
            movie_data = json.loads(movie_data_json.read())
        movie_genre_action_title = {element['title']: element['image'] for element in movie_data if element['genre'] == 'action'}
        movie_genre_fantasy_title = {element['title']: element['image'] for element in movie_data if element['genre'] == 'fantasy'}
        movie_genre_drama_title = {element['title']: element['image'] for element in movie_data if element['genre'] == 'drama'}
        movie_genre_romance_title = {element['title']: element['image'] for element in movie_data if element['genre'] == 'romance'}
        movie_genre_animation_title = {element['title']: element['image'] for element in movie_data if element['genre'] == 'animation'}
        return (movie_genre_action_title, movie_genre_fantasy_title, movie_genre_drama_title,
                movie_genre_romance_title, movie_genre_animation_title)
    except TypeError:
        print('TypeError')
def data_book():
    try:
        with open('data/book_data.json') as book_data_json:
            book_data = json.loads(book_data_json.read())
        book_genre_novel_title = {element['title']: element['author'] for element in book_data if element['genre'] == 'novel'}
        book_genre_childrens_lit_title = {element['title']: element['author'] for element in book_data if element['genre'] == "children's literature"}
        book_genre_poetry_title = {element['title']: element['author'] for element in book_data if element['genre'] == 'poetry'}
        book_genre_tragedy_title = {element['title']: element['author'] for element in book_data if element['genre'] == 'tragedy'}
        return (book_genre_childrens_lit_title,book_genre_novel_title,  book_genre_poetry_title,
                book_genre_tragedy_title)
    except TypeError:
        print('TypeError')
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
