import pymongo


def connect_to_MongoDB():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["StatesOfTheWorld"]
    collection = database["StatesOfTheWorld"]
    return collection