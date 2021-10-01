from flask import Flask, render_template, request
import requests


app = Flask(__name__)
api_url = "https://api.npoint.io/4af156202f984d3464c3"

response = requests.get(url=api_url)
response.raise_for_status()

all_posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    heading = "Contact Me" if request.method == "GET" else "Successfully sent message"

    return render_template("contact.html", heading=heading)


@app.route("/post/<int:_id>")
def post_page(_id):
    required_post = {}
    for post in all_posts:
        if post["id"] == _id:
            required_post = post
            break

    return render_template("post.html", post=required_post)


if __name__ == "__main__":
    app.run(debug=True)
