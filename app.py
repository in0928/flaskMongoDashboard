from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import scheduleScrapper as ss
import displaySchedule as ds
import mongoDBConnector

app = Flask(__name__)
title = "Sample form submission with MongoDB"
heading = "Form submission with Flask and MongoDB"

collections = mongoDBConnector.connect_mongo()
people_test = collections[0]
schedule_test = collections[1]
union_test = collections[2]
ba_test = collections[3]
fav_people = collections[8]
fav_ba = collections[9]


@app.route("/")
def home():
    t = "My Dashboard"
    people_list = people_test.find()
    ba_list = ba_test.find()
    fav_people_list = fav_people.find()
    fav_ba_list = fav_ba.find()
    return render_template("home.html", people_list=people_list, ba_list = ba_list, fav_people_list=fav_people_list, fav_ba_list=fav_ba_list, t=t)


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
    people_list = people_test.find()
    return render_template("ba.html", people_list=people_list, t=t)


if __name__ == "__main__":
    app.run(debug=True)
