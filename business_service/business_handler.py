from business_service import access_manager
from data_access import room_repository
from model.response import Response
from bson.json_util import dumps


def check_access(function):
    def wrapper(*args, **kwargs):
        action = args[0]
        is_admin = args[1]
        if access_manager.has_access(is_admin, action):
            return function(*args[2:], **kwargs)
        return Response.access_forbidden, None

    return wrapper


@check_access
async def add_room(name, capacity, office, features):
    if not room_repository.exists_room(name, None):
        await room_repository.add_room(name, capacity, office, features)
        return Response.created, 'room created'
    return Response.invalid_request, None


@check_access
async def edit_room(room_id, new_name, capacity, office, features):
    if not await room_repository.exists_room(None, room_id):
        return Response.invalid_request, None
    await room_repository.update_room(room_id, new_name, capacity, office, features)
    return Response.updated, 'room updated'


@check_access
async def delete_room(room_id):
    if room_repository.exists_room(None, room_id):
        return Response.invalid_request, None
    await room_repository.delete_room(room_id, None)
    return Response.ok, 'room deleted'


@check_access
async def get_rooms():
    return Response.ok, dumps(list(await room_repository.get_all_rooms()), indent=2)
    # todo the json dumps method should be called in another layer

# async def func():
#     # return await get_rooms(Action.get_rooms, True)
#     return await edit_room(Action.modify_room, True, "622342b721c3b3c1d72fdc1c", "room one", None, "The Tehran!", None)
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# result, message = loop.run_until_complete(func())
#
# print(message)
