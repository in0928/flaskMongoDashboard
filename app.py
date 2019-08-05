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


@app.route("/")
def home():
    people_list = people_test.find()
    ba_list = ba_test.find()
    return render_template("home.html", people_list=people_list, ba_list = ba_list)


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
def schedule():  # will need to use scheduleScrapper to get data first, now it is working cuz there are data in DB
    # all_union_names = ss.get_unions() # This is used to update union names
    all_unions = union_test.find({})
    all_union_names = []
    for union in all_unions:
        all_union_names.append(union["union-name"])

    month_date = ["8."]*31
    for i in range(31):
        date = str(i+1)
        month_date[i] = month_date[i]+date

    event_list = []
    for day in month_date:
        aug_events = schedule_test.find({"date": day})
        merged = ds.merge_rows(aug_events)
        for item in merged:
            content = item["content"]
            date = item["date"]
            union_name = item["union_name"]
            time = item["time"]
            SP = item["SP"]
            MC_AC = item["MC_AC"]
            venue = item["venue"]
            if content == "" or content == "Invisible":  # not show groups with no events
                continue
            else:
                new_entry = [date, union_name, content, time, SP, MC_AC, venue]
                event_list.append(new_entry)
    return render_template("schedule.html", event_list=event_list, all_union_names=all_union_names)


@app.route("/people")
def people():
    return render_template("people.html")


if __name__ == "__main__":
    app.run(debug=True)
