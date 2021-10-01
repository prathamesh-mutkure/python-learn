from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "secret"


Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///day-63-books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


class AddBookForm(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField("Add Book")


class UpdateBookForm(FlaskForm):
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField("Update Rating")


db.create_all()


@app.route('/')
def home():
    all_books = Book.query.all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBookForm()

    if form.validate_on_submit():

        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html", form=form)


@app.route("/update", methods=["GET", "POST"])
def update():
    form = UpdateBookForm()
    book = Book.query.get(request.args.get('book_id'))

    if form.validate_on_submit():
        book.rating = form.rating.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("update.html", book=book, form=form)


@app.route("/delete")
def delete():
    book_id = request.args.get("book_id")
    book = Book.query.get(book_id)

    db.session.delete(book)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

