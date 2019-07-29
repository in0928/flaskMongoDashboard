from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import scheduleScrapper
from bs4 import BeautifulSoup as bs
from requests import Session

app = Flask(__name__)
title = "Sample form submission with MongoDB"
heading = "Form submission with Flask and MongoDB"

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.test  # Select the database
people_test = db.peopleTest  # Select the collection name


@app.route("/")
def home():
    people_list = people_test.find()
    row = get_row_data()
    return render_template("home.html", people_list=people_list, row=row)

def get_row_data():
    with Session() as s:
        # To login
        site = s.get("https://www.improveonline.jp/")
        login_data = {"loginid": "in0928", "password": "54hanghang"}
        s.post("https://www.improveonline.jp/", login_data)

        # Create a list of IDs for all groups


        # Test with IDEA August schedule
        idea_aug = s.get("https://www.improveonline.jp/mypage/union/schedule_detail.php?date=2019-08&group=20&mc=8")
        idea_aug_content = bs(idea_aug.content, "html.parser")
        schedule = idea_aug_content.find("table", attrs={"class": "schedule"}) # get the full schedule

        aug3 = schedule[3]
        row_data = aug3.find_all("td")
        row_list = []
        for item in row_data:
            val = item.text
            row_list.append(val)
        return row_list


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

if __name__ == "__main__":
    app.run(debug=True)
