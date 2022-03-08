from business_service import access_manager
from data_access import room_repository
from model.response import Response


def check_access(function):
    def wrapper(*args, **kwargs):
        action = args[0]
        is_admin = args[1]
        if access_manager.has_access(is_admin, action):
            return function(*args[2:], **kwargs)
        return Response.access_forbidden, None

    return wrapper


@check_access
async def add_room(room):
    if not await room_repository.exists_room(room.name, None):
        await room_repository.add_room(room)  # todo should we have the 'await'?
        return Response.created, 'Room created.'
    return Response.invalid_request, "Room with this name already exists."


@check_access
async def edit_room(room_id, new_room):
    if not await room_repository.exists_room(None, room_id):
        return Response.invalid_request, "No room with this name exists."
    await room_repository.update_room(room_id, new_room)
    return Response.updated, 'Room updated.'


@check_access
async def delete_room(room_id):
    if not await room_repository.exists_room(None, room_id):
        return Response.invalid_request, "No room with this name exists."
    await room_repository.delete_room(room_id, None)  # todo should we have the 'await'?
    return Response.ok, 'Room deleted.'


@check_access
async def get_rooms():
    return Response.ok, await room_repository.get_all_rooms()
