import unittest

import pytest as pytest

from business_service import business_handler
from model.action import Action
from model.office import Office
from model.response import Response
from model.room import Room


class TestBusiness(unittest.TestCase):

    @pytest.mark.asyncio
    async def test_add_room(self):
        room = Room('test room', 12, Office.TEHRAN, features=None)
        is_admin = True
        response, message = await business_handler.add_room(Action.add_room, is_admin, room)
        self.assertEqual(response, Response.created,
                         'Should create a room!')
