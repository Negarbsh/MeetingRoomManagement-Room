from bson import ObjectId

from data_access.initiate_db import get_database
from model.feature import Feature

room_db = get_database()
room_collection = room_db["rooms_collection"]


async def add_room(name, capacity, office, features):
    room_collection.insert_one({
        "name": name,
        "capacity": capacity,
        "office": office,
        "features": {
            "projector": Feature.projector in features,
            "white_board": Feature.white_board in features,
            "sound_proof": Feature.sound_proof in features
        }
    })


async def get_room_by_room_id(room_id):
    return room_collection.find({"_id": ObjectId(room_id)})


async def get_room_by_name(name):
    return await room_collection.find({"name": name})


async def delete_room(room_id, name):
    if room_id is not None:
        room_collection.delete_many({"_id": ObjectId(room_id)})
    else:
        room_collection.delete_many({"name": name})


def get_features(new_features):
    return {
        "projector": Feature.projector in new_features,
        "white_board": Feature.white_board in new_features,
        "sound_proof": Feature.sound_proof in new_features
    }


async def update_room(room_id, new_name, new_capacity, new_office, new_features):
    if new_name is not None:
        room_collection.update_one({"_id": ObjectId(room_id)}, {"$set": {"name": new_name}})
    if new_capacity is not None:
        room_collection.update_one({"_id": ObjectId(room_id)}, {"$set": {"capacity": new_capacity}})
    if new_office is not None:
        room_collection.update_one({"_id": ObjectId(room_id)}, {"$set": {"office": new_office}})
    if new_features is not None:
        new_features_json = get_features(new_features)
        room_collection.update_one({"_id": ObjectId(room_id)}, {"$set": {"features": new_features_json}})


async def exists_room(name, room_id):
    if room_id is not None:
        return room_collection.count_documents({"_id": ObjectId(room_id)}, skip=0) > 0
    if name is not None:
        return room_collection.count_documents({"name": name}) > 0
    return False


async def get_all_rooms():
    return room_collection.find()
