from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)
agify_url = "https://api.agify.io"
genderize_url = "https://api.genderize.io?"


def get_age(name):
    response = requests.get(url=agify_url, params={"name": name})
    response.raise_for_status()

    age = response.json()["age"]
    return int(age)


def get_gender(name):
    response = requests.get(url=genderize_url, params={"name": name})
    response.raise_for_status()

    gender = response.json()["gender"]
    return gender


@app.route("/<name>")
def say_hello(name):
    year = date.today().year
    return render_template("index.html", name=name, year=year)


@app.route("/guess/<name>")
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():

    blog_posts = [
        {
            "id": 1,
            "title": "Apple hits $2 Trillion Market Cap",
            "subtitle": "Apple becomes first American corp to hit this milestone!",
        },
        {
            "id": 2,
            "title": "Bitcoin hits ATH at $60,000",
            "subtitle": "Bitcoin market cap now exceeds $1 Trillion",
        },
        {
            "id": 3,
            "title": "Reliance at ATH, drives NIFTY upward of of 17,000",
            "subtitle": "NIFTY at all time high",
        }
    ]

    return render_template("blog.html", blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
