from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import scheduleScrapper as ss

app = Flask(__name__)
title = "Sample form submission with MongoDB"
heading = "Form submission with Flask and MongoDB"

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.test  # Select the database
people_test = db.peopleTest  # Select the collection name

# use for COM schedule
date_list = list(range(0, 32))

@app.route("/")
def home():
    people_list = people_test.find()
    return render_template("home.html", people_list=people_list)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/people")
def people():
    return render_template("people.html")


@app.route("/action", methods=["POST"])
def action():
    # get data
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
    new_session = ss.login()
    row_data = ss.get_row_data(new_session)
    # Aug now
    # currentMonth = datetime.now().strftime("%m")
    # month = currentMonth.replace("0", "")
    month = "8"
    all_dates = []
    for date in date_list[1:]:
        all_dates.append(month+" / "+str(date))
    return render_template("schedule.html", row_data=row_data, all_dates=all_dates)


if __name__ == "__main__":
    app.run(debug=True)
