class Room:
    def __init__(self, name, capacity, office='Tehran', features=None):
        if features is None:
            features = []
        # self.number = room_number
        self.name = name
        self.capacity = capacity
        self.office = office
        self.features = features
