from pymongo import MongoClient
import pymongo


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo

    CONNECTION_STRING = "mongodb+srv://negar:C4wxSpEQdpeTfG7@sandbox.lzqav.mongodb.net/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['tapsi_rooms_service']


db = get_database()

collection_name = db["rooms_collection"]

item_1 = {
    "name": "room1",
    "capacity": 6,
    "office": "Tehran",
    "features": {
        "projector": True,
        "white_board": True,
        "sound_proof": False
    }
}

item_2 = {
    "name": "room2",
    "capacity": 4,
    "office": "Tehran",
    "features": {
        "projector": False,
        "white_board": True,
        "sound_proof": False
    }
}