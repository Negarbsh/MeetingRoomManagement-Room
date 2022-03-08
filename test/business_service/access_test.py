import unittest
from model.action import Action
from business_service.access_manager import has_access


class TestAccess(unittest.TestCase):

    def test_create_admin(self):
        self.assertEqual(has_access(is_admin=True, action=Action.add_room), True,
                         'Admin should be able to create room')

    def test_create_emp(self):
        self.assertEqual(has_access(is_admin=False, action=Action.add_room), False,
                         'Employee should not be able to create room')

    def test_get(self):
        self.assertEqual(has_access(False, Action.get_rooms), True,
                         'Everyone should be able to get the list of rooms')

    def test_edit_emp(self):
        self.assertEqual(has_access(False, Action.modify_room), False,
                         'Employee should not be able to edit a room')

