from pymongo import MongoClient


class PyMongo:

    def __init__(self):
        self.client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
        self.db = self.client.test  # Select the database
        self.people_test = self.db.peopleTest  # 0
        self.schedule_test = self.db.scheduleTest  # 1
        self.union_test = self.db.unionTest  # 2 this is used with schedule
        self.ba_test = self.db.baTest  # 3
        self.my_dreams_test = self.db.myDreamsTest  # 4
        self.place_test = self.db.placeTest  # 5
        self.my_dlines_test = self.db.myDlinesTest  # 7 TODO: add d-lines management someday
        self.users_test = self.db.usersTest  # 7 TODO: add user management someday
        self.notes_test = self.db.notesTest  # 8
