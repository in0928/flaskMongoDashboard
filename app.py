from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import displaySchedule as ds
from mongoDBConnector import PyMongo
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
title = "Sample form submission with MongoDB"
heading = "Form submission with Flask and MongoDB"

connector = PyMongo()
people_test = connector.people_test
schedule_test = connector.schedule_test
union_test = connector.union_test
ba_test = connector.ba_test
my_dreams_test = connector.my_dreams_test
place_test = connector.place_test
my_dlines_test = connector.my_dlines_test
users_test = connector.users_test
notes_test = connector.notes_test


def add_favorite(cursor, this):
    text = bs(this).text
    # cursor.find_one_and_update( $and: [{"full-name": text}, {"description": desc}], {$set})


@app.route("/")
def home():
    t = "My Dashboard"
    people_list = people_test.find()
    ba_list = ba_test.find()
    fav_people_list = people_test.find({"favorite": "True"})
    fav_ba_list = ba_test.find({"favorite": "True"})
    fav_notes_list = notes_test.find({"favorite": "True"})
    return render_template("home.html", people_list=people_list, ba_list=ba_list,\
                           fav_people_list=fav_people_list, fav_ba_list=fav_ba_list, fav_notes_list=fav_notes_list, t=t)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/action", methods=["POST"])
def action():
    # get data from form
    full_name = request.form.get("full-name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    status = request.form.get("status")
    description = request.form.get("description")
    people_test.insert_one({
        "full-name": full_name,
        "age": age,
        "gender": gender,
        "status": status,
        "description": description,
        "last-updated": datetime.now()
    })
    return redirect("/submitted")


@app.route("/submitted")
def submitted():
    return render_template("submitted.html")

@app.route("/schedule")
def schedule():
    t = "Monthly Schudule Scrapped from COM"

    month_date = ["8."]*31
    for i in range(31):
        date = str(i+1)
        month_date[i] = month_date[i]+date

    event_list = []
    for day in month_date:
        aug_events = schedule_test.find({"date": day})
        merged = ds.merge_rows(aug_events)

        for i in merged:
            if i["content"] == "" or i["content"] == "Invisible":  # not show groups with no events
                continue
            else:
                event_list.append(i)
    return render_template("schedule.html", event_list=event_list, t=t)


@app.route("/people")
def people():
    t = "People List"
    people_list = people_test.find()
    return render_template("people.html", people_list=people_list, t=t)

@app.route("/ba")
def ba():
    t = "BA List"
    ba_list = ba_test.find()
    return render_template("ba.html", ba_list=ba_list, t=t)


if __name__ == "__main__":
    app.run(debug=True)
