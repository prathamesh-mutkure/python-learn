from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests as req

API_KEY = "e33bab3c118437512fbffc315279d013"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False,)


db.create_all()


class EditMovieForm(FlaskForm):
    rating = FloatField("Your rating out of 10, e.g. 7.5")
    review = StringField("Review")
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")

    def get_movies(self) -> []:

        params = {
            "api_key": API_KEY,
            "query": self.title.data,
        }

        response = req.get("https://api.themoviedb.org/3/search/movie", params=params)
        response.raise_for_status()

        return response.json()["results"]


def get_movie_details(movie_id):
    params = {
        "api_key": API_KEY,
    }

    response = req.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=params)
    response.raise_for_status()

    return response.json()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    movie_id = request.args.get("movie_id")

    if movie_id is not None:
        movie_details = get_movie_details(movie_id)

        movie = Movie()
        movie.id = movie_details["id"]
        movie.title = movie_details["title"]
        movie.description = movie_details["overview"]
        movie.year = movie_details["release_date"]
        movie.img_url = movie_details["poster_path"]

        movie.review = ""
        movie.rating = 0.0

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("edit", movie_id=movie_id))

    if form.validate_on_submit():

        movies = form.get_movies()

        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=["POST"])
def delete():
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
