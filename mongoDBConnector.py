from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient


def connect_mongo():
    client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
    db = client.test  # Select the database
    people_test = db.peopleTest  # Select the collection name
    schedule_test = db.scheduleTest
    union_test = db.unionTest
    return people_test, schedule_test, union_test
