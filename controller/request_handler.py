import json

from bson import json_util

from model.action import Action
from business_service import business_handler
from model.response import Response


async def get_all(input_data, is_admin):
    action = Action.get_rooms
    response, result = await business_handler.get_rooms(action, is_admin)
    result = json.loads(json_util.dumps(result))
    return response, result


async def update(input_data, is_admin):
    if 'room_id' not in input_data:
        return Response.invalid_request, 'No field "room_id" specified'
    room_id = input_data.get('room_id')
    name = input_data.get('name')
    capacity = input_data.get('capacity')
    office = input_data.get('office')
    features = None
    if input_data.get('features') is not None:
        features = json.loads(input_data.get('features'))
    # todo is any more data validation needed?

    action = Action.modify_room
    response, result = business_handler.edit_room(action, is_admin, room_id, name, capacity, office, features)
    return response, result


async def delete(input_data, is_admin):
    if 'room_id' not in input_data:
        return Response.invalid_request, 'No field "room_id" specified'
    room_id = input_data.get('room_id')
    return business_handler.delete_room(Action.delete_room, is_admin, room_id)


async def create(input_data, is_admin):
    if 'name' not in input_data or 'capacity' not in input_data or 'office' not in input_data \
            or 'features' not in input_data:
        return Response.invalid_request, 'All fields "name", "capacity", "office" and "features" should be given'
    name = input_data.get('name')
    capacity = input_data.get('capacity')
    office = input_data.get('office')
    features = input_data.get('features')
    # todo check the datatypes
    return await business_handler.add_room(Action.add_room, is_admin, name, capacity, office, features)
