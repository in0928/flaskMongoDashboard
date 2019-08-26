from pymongo import MongoClient


class PyMongo:

    def __init__(self):
        # # tests
        # self.client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
        # self.db = self.client.test  # Select the database
        # self.people_test = self.db.peopleTest  # 0
        # self.schedule_test = self.db.scheduleTest  # 1
        # self.union_test = self.db.unionTest  # 2 this is used with schedule
        # self.ba_test = self.db.baTest  # 3
        # self.my_dreams_test = self.db.myDreamsTest  # 4
        # self.place_test = self.db.placeTest  # 5
        # self.my_dlines_test = self.db.myDlinesTest  # 7 TODO: add d-lines management someday
        # self.users_test = self.db.usersTest  # 7 TODO: add user management someday
        # self.notes_test = self.db.notesTest  # 8

        # real DB
        self.client = MongoClient("mongodb+srv://in0928:trybest920928LAISAI@cluster0-nfgyd.gcp.mongodb.net/test?retryWrites=true&w=majority")  # host uri
        self.db = self.client.NSDB  # Select the database
        self.people = self.db.people  # 0
        self.schedule_this_month = self.db.scheduleThisMonth  # 1
        self.schedule_next_month = self.db.scheduleNextMonth
        self.unions = self.db.unions  # 2 this is used with schedule
        self.ba = self.db.ba  # 3
        self.my_dreams = self.db.myDreams  # 4
        self.places = self.db.places  # 5
        self.my_dlines = self.db.myDlines  # 7 TODO: add d-lines management someday, can be premium feature
        self.users = self.db.users  # 7 TODO: add user management someday
        self.notes = self.db.notes  # 8
