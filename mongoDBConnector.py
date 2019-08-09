from pymongo import MongoClient


def connect_mongo():
    client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
    db = client.test  # Select the database
    people_test = db.peopleTest #0
    schedule_test = db.scheduleTest #1
    union_test = db.unionTest #2 this is used with schedule
    ba_test = db.baTest #3
    my_dreams_test = db.myDreamsTest #4
    place_test = db.placeTest #5
    my_dlines_test = db.myDlinesTest #7 TODO: add d-lines management someday
    users_test = db.usersTest  #7 TODO: add user management someday
    notes_test = db.notesTest#8
    return people_test, schedule_test, union_test, ba_test, my_dreams_test, place_test, my_dlines_test, users_test, notes_test
