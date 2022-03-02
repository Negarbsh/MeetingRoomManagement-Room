import access_manager
from data_access import room_repository
from model.response import Response


def check_access(function):
    def wrapper(*args, **kwargs):
        action = args[0]
        is_admin = args[1]
        if access_manager.has_access(is_admin, action):
            return function(*args[2:], **kwargs)
        return Response.access_forbidden

    return wrapper


@check_access
def add_room(name, capacity, office, features):
    if not room_repository.exists_room(name):
        room_repository.add_room(name, capacity, office, features)
        return Response.created
    return Response.invalid_request


@check_access
def edit_room(name, capacity, office, features):
    if not room_repository.exists_room(name):
        return Response.invalid_request
    room_repository.update_room(room_repository.get_room_by_name(name).id, name, capacity, office, features)
    return Response.updated


@check_access
def delete_room(name, room_id):
    if room_id is None:
        room = room_repository.get_room_by_name(name)
        if room is None:
            return Response.invalid_request
        room_id = room.id
    if room_repository.exists_room(None, room_id):
        return Response.invalid_request
    room_repository.delete_room(room_id)
    return Response.ok


@check_access
def get_rooms():
    return Response.ok, room_repository.get_all_rooms()
