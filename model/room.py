class Room:
    def __init__(self, room_id, name, capacity, office='Tehran', features=None):
        if features is None:
            features = []
        self.id = room_id
        self.name = name
        self.capacity = capacity
        self.office = office
        self.features = features
