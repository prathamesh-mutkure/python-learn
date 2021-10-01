from flask import Flask, jsonify, render_template, request
from random import choice
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def random():
    cafes = Cafe.query.all()
    random_cafe = choice(cafes)

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()

    cafe_json = [cafe.to_dict() for cafe in cafes]

    return jsonify(cafes=cafe_json)


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():

    cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)

    if cafe:
        cafe.coffee_price = request.args.get("price")
        db.session.commit()

        return jsonify(success="successfully updated the price!")
    else:
        return jsonify(error={"Not Found": "Sorry no cafe with that ID was found in database"}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):

    api_key = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)

    if api_key != "TopSecretAPIKey":
        return jsonify(error="Sorry, permission denied!")

    if cafe:
        db.session.delete(cafe)
        db.session.commit()

        return jsonify(success="successfully deleted the cafe from database")
    else:
        return jsonify(error={"Not Found": "Sorry no cafe with that ID was found in database"}), 404


if __name__ == '__main__':
    app.run(debug=True)
