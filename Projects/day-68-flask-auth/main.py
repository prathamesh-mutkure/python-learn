from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class RegisterUserForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    submit = SubmitField()


# Line below only required once, when creating DB.
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":

        password = request.form.get('password')
        password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)

        try:
            user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=password
            )

            db.session.add(user)
            db.session.commit()

        except:
            flash("User already exists!")
        else:

            login_user(user=user, remember=True)

            return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(pwhash=user.password, password=password):
            login_user(user=user)

            return redirect(url_for('secrets'))
        else:
            flash("Incorrect username or password!")

    return render_template("login.html")


@app.route('/secrets/')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_manager.unauthorized_handler
def unauthorized():
    return "Access Denied"


if __name__ == "__main__":
    app.run(debug=True)
