from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import re
import db_helper
import requests
# import db_helper
# import generic_helper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Ensure this line specifies the correct URL and HTTP method


@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    output_contexts = payload['queryResult']['outputContexts']
    parameters = output_contexts[0]['parameters']
    parameters2 = payload['queryResult']['parameters']

    intent_handler_dict = {
        'confirm-order': add_order,
        'about-movie': about_movie
    }

    print(intent, parameters, sep="\n")
    return intent_handler_dict[intent](parameters)


def add_order(parameters):
    item = parameters['movie-item']
    quantity = parameters['number']
    type = parameters['disk-type']
    rcode = db_helper.insert_order(item, quantity, type)
    if rcode == -1:
        fulfillment_text = "Sorry, I couldn't process your order due to a backend error. " \
            "Please place a new order again"
    else:
        fulfillment_text = f"Awesome. We have placed your order. "

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def about_movie(parameters):
    movie = parameters['movie-item']
    movie_info = db_helper.get_movie_info(movie)
    api_key = "9998e0f2bd5fbb9af895b64d82223892"
    api_url = f"https://api.themoviedb.org/3/search/movie?query={movie}&api_key={api_key}"
    print(movie_info)
    if movie_info is None:
        print("TMDB")
        response = requests.get(api_url)
        data = response.json()
        movie_info_new = data['results'][0]
        movie_res = db_helper.insert_movie(movie_info_new['original_title'])
        fulfillment_text = f"This movie not found in our store. Below details I retrieved from TMDB website and I will request to admins to add this movie to store. \n {movie_info_new['original_title']} movie released in {movie_info_new['release_date']}. " \
            f"IMDB rating is {movie_info_new['vote_average']}. " \
            f"Story Line: \n {movie_info_new['overview']}"
    else:
        print("DB")
        fulfillment_text = f"You can buy this movie from our Store. \n {movie_info['mov_title']} is a {movie_info['age']} movie released in {movie_info['r_date']}. " \
            f"IMDB rating is {movie_info['rate']}/100. " \
            f"Story Line: \n {movie_info['s_line']}" \

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })
