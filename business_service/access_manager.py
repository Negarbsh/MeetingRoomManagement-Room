from model.action import Action


def has_access(is_admin, action):
    if action == Action.add_room or action == Action.delete_room or action == Action.modify_room:
        return is_admin
    if action == Action.get_rooms:
        return True
    return False

