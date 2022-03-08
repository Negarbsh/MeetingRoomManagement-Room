import json

from bson import json_util

from model.action import Action
from business_service import business_handler
from model.response import Response
from model.room import Room


def validate_id(function):
    async def wrapper(input_data, is_admin):
        if 'room_id' not in input_data:
            return Response.invalid_request, "No field 'room_id' specified"
        room_id = input_data.get('room_id')
        if not isinstance(room_id, str):
            return Response.invalid_request, "Field 'room_id' should be of type string," \
                                             " but received " + str(type(room_id))
        return await function(input_data, is_admin, room_id)

    # wrapper.__name__ = function.__name__
    return wrapper


async def get_all(input_data, is_admin):
    action = Action.get_rooms
    response, result = await business_handler.get_rooms(action, is_admin)
    result = json.loads(json_util.dumps(result))
    return response, result


@validate_id
async def update(input_data, is_admin, room_id):
    name = input_data.get('name')
    capacity = input_data.get('capacity')
    office = input_data.get('office')
    features = None
    if input_data.get('features') is not None:
        features = json.dumps(input_data.get('features'))
    # todo is any more data validation needed?

    action = Action.modify_room
    new_room = Room(name, capacity, office, features)
    response, result = await business_handler.edit_room(action, is_admin, room_id, new_room)
    return response, result


@validate_id
async def delete(input_data, is_admin, room_id):
    return await business_handler.delete_room(Action.delete_room, is_admin, room_id)


async def create(input_data, is_admin):
    if type(is_admin) is not bool:
        return Response.unauthorized, 'Invalid token payload'
    if 'name' not in input_data or 'capacity' not in input_data or 'office' not in input_data \
            or 'features' not in input_data:
        return Response.invalid_request, "All fields 'name', 'capacity', 'office' and 'features' should be given"
    name = input_data.get('name')
    capacity = input_data.get('capacity')
    office = input_data.get('office')
    features = input_data.get('features')
    # todo check the datatypes
    room = Room(name, capacity, office, features)
    return await business_handler.add_room(Action.add_room, is_admin, room)
