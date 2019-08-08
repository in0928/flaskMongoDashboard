from pymongo import MongoClient


def connect_mongo():
    client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
    db = client.test  # Select the database
    people_test = db.peopleTest
    schedule_test = db.scheduleTest
    union_test = db.unionTest # this is used with schedule
    ba_test = db.baTest
    my_dreams_test = db.myDreamsTest
    place_test = db.placeTest
    my_dlines_test = db.myDlinesTest #TODO: add d-lines management someday
    users_test = db.usersTest  #TODO: add user management someday
    fav_people = db.favPeople
    fav_ba = db.favBA
    return people_test, schedule_test, union_test, ba_test, my_dreams_test, place_test, my_dlines_test, users_test, fav_people, fav_ba
