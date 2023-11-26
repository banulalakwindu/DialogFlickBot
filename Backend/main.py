from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import re
import db_helper
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

    intent_handler_dict = {
        'confirm-order': add_order
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
