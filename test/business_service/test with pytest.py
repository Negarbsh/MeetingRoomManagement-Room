import pytest as pytest

from business_service import business_handler
from model.action import Action
from model.office import Office
from model.response import Response
from model.room import Room
from data_access import room_repository


@pytest.mark.asyncio
async def test_add_room():
    room = Room('test room', 12, Office.TEHRAN, features=None)
    is_admin = True
    response, message = await business_handler.add_room(Action.add_room, is_admin, room)
    room = await room_repository.get_room_by_name('test room')

    assert response is Response.created
    assert room is not None
    # self.assertEqual(response, Response.created, 'Should create a room!')
    # self.assertIsNotNone(room)


# @pytest.mark.asyncio
# async def test_add_existing_room(self):
#     room = Room('test room', 12, Office.TEHRAN, features=None)
#     duplicate_room = Room('test room', 14, Office.TEHRAN, features=None)
#     is_admin = True
#     await business_handler.add_room(Action.add_room, is_admin, room)
#     response, message = await business_handler.add_room(Action.add_room, is_admin, duplicate_room)
#
#     room = await room_repository.get_room_by_name('test room')
#
#     self.assertEqual(response, Response.invalid_request, 'Should reject creating an existing room!')
#     self.assertEqual(room.capacity, 12, 'Should not overwrite the room information.')
#
#
# @pytest.mark.asyncio
# async def test_update_room(self):
#     pass
#
#
# @pytest.mark.asyncio
# async def test_delete_room(self):
#     pass
#
#
# @pytest.mark.asyncio
# async def test_(self):
#     pass
