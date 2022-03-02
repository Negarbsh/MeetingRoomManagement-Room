from model.room import Room

all_rooms = {}
last_id = 0


def get_room_by_id(room_id):
    return all_rooms[room_id]


def get_room_by_name(name):
    for room in all_rooms.values():
        if room.name == name:
            return room
    return None


def add_room(name, capacity, office, features):
    global last_id
    room = Room(last_id, name, capacity, office, features)
    all_rooms[last_id] = room
    last_id += 1


def delete_room(room_id, name):
    if room_id is None:
        room_id = get_room_by_name(name)
    del all_rooms[room_id]


def update_room(room_id, new_name, new_capacity, new_office, new_features):
    room = get_room_by_id(room_id)
    if new_name is not None:
        room.name = new_name
    if new_capacity is not None:
        room.capacity = new_capacity
    if new_office is not None:
        room.office = new_office
    if new_features is not None:
        room.features = new_features


def exists_room(name, room_id):
    if room_id is None:
        return get_room_by_name(name) is not None
    return get_room_by_id(room_id) is not None


def get_all_rooms():
    return all_rooms
