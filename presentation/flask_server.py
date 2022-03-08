import json

from flask import Flask, request, jsonify, current_app

from controller import request_handler
from model.response import Response
from presentation.token_docoder import decode_token

app = Flask(__name__)


def check_token(function):
    def wrapper(*args, **kwargs):
        encoded_token = request.headers.get('token')
        if encoded_token is not None:
            decoded_token = decode_token(encoded_token)
            if decoded_token is not None and 'is_admin' in decoded_token:
                return current_app.ensure_sync(function)(decoded_token, *args, **kwargs)
        return {"message": 'Invalid token'}, Response.unauthorized.value

    wrapper.__name__ = function.__name__
    return wrapper


@app.route('/add_room', methods=['POST'])
@check_token
async def add_room(decoded_token):
    room_information = json.loads(request.data)
    response, message = await request_handler.create(room_information, decoded_token.get('is_admin'))
    return {"message": message}, response.value


@app.route('/edit_room', methods=['POST'])
@check_token
async def edit_room(decoded_token):
    room_information = json.loads(request.data)
    response, message = await request_handler.update(room_information, decoded_token.get('is_admin'))
    return {"message": message}, response.value


@app.route('/delete_room', methods=['POST'])
@check_token
async def delete_room(decoded_token):
    room_information = json.loads(request.data)
    response, message = await request_handler.delete(room_information, decoded_token.get('is_admin'))
    return {"message": message}, response.value


@app.route('/get_all', methods=['POST'])
@check_token
async def get_rooms(decoded_token):
    room_information = json.loads(request.data)
    response, message = await request_handler.get_all(room_information, decoded_token.get('is_admin'))
    return {"message": message}, response.value


if __name__ == '__main__':
    app.run()
