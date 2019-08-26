import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient

import displaySchedule as ds
from mongoDBConnector import PyMongo
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

connector = PyMongo()
people_data = connector.people
schedule_this_month_data = connector.schedule_this_month
unions_data = connector.unions
ba_data = connector.ba
my_dreams_data = connector.my_dreams
places_data = connector.places
my_dlines_data = connector.my_dlines
users_data = connector.users
notes_data = connector.notes

@app.route("/confirm")
def favorite():
    print("123333")
    return redirect("/")

@app.route("/")
def home():
    t = "My Dashboard"
    people_list = people_data.find()
    ba_list = ba_data.find()
    fav_people_list = people_data.find({"favorite": True})
    fav_ba_list = ba_data.find({"favorite": True})
    fav_notes_list = notes_data.find({"favorite": True})
    return render_template("home.html", people_list=people_list, ba_list=ba_list,\
                           fav_people_list=fav_people_list, fav_ba_list=fav_ba_list, fav_notes_list=fav_notes_list, t=t)


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/updatepeopleform")
def form_u():
    id = request.values.get("_id")
    print(id)
    person = people_data.find({"_id": ObjectId(id)})
    return render_template("updateForm.html", person=person)

@app.route("/updatedpeople", methods=['POST'])
def update_form():
    id = str(request.values.get("_id"))
    full_name = request.form.get("full-name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    status = request.form.get("status")
    other_status = request.form.get("other-status")
    description = request.form.get("description")
    needs = request.form.get("needs")
    character = request.form.get("character")
    relation = request.form.get("relation")
    job = request.form.get("job")
    company = request.form.get("company")
    company_loc = request.form.get("company-loc")
    home = request.form.get("home")
    hometown = request.form.get("hometown")
    source = request.form.get("source")
    remarks = request.form.get("remarks")
    fav = request.form.get("fav")
    if fav:
        favorite = True
    else:
        favorite = False
    people_data.find_one_and_update({"_id": ObjectId(id)},
                                    {'$set': {
                                        "favorite": favorite,
                                        "full-name": full_name,
                                        "age": age,
                                        "gender": gender,
                                        "status": status,
                                        "other-status": other_status,
                                        "description": description,
                                        "needs": needs,
                                        "character": character,
                                        "relation": relation,
                                        "job": job,
                                        "company": company,
                                        "company-loc": company_loc,
                                        "home": home,
                                        "hometown": hometown,
                                        "source": source,
                                        "remarks": remarks,
                                        "last-updated": datetime.now()
                                    }})

    return redirect("/submitted")


@app.route("/submit_form", methods=["POST"])
def submit_form():
    # get data from form
    target_list = request.form.get("submit-to-list")
    full_name = request.form.get("full-name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    status = request.form.get("status")
    other_status = request.form.get("other-status")
    description = request.form.get("description")
    needs = request.form.get("needs")
    character = request.form.get("character")
    relation = request.form.get("relation")
    job = request.form.get("job")
    company = request.form.get("company")
    company_loc = request.form.get("company-loc")
    home = request.form.get("home")
    hometown = request.form.get("hometown")
    source = request.form.get("source")
    remarks = request.form.get("remarks")
    fav = request.form.get("fav")
    if fav:
        favorite = True
    else:
        favorite = False

    if target_list == "ba-list":
        cursor = ba_data
    else:
        cursor = people_data
    cursor.insert_one({
        "favorite": favorite,
        "full-name": full_name,
        "age": age,
        "gender": gender,
        "status": status,
        "other-status": other_status,
        "description": description,
        "needs": needs,
        "character": character,
        "relation": relation,
        "job": job,
        "company": company,
        "company-loc": company_loc,
        "home": home,
        "hometown": hometown,
        "source": source,
        "remarks": remarks,
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
        aug_events = schedule_this_month_data.find({"date": day})
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
    people_list = people_data.find()
    return render_template("people.html", people_list=people_list, t=t)

@app.route("/ba")
def ba():
    t = "BA List"
    ba_list = ba_data.find()
    return render_template("ba.html", ba_list=ba_list, t=t)


if __name__ == "__main__":
    app.run(debug=True)
