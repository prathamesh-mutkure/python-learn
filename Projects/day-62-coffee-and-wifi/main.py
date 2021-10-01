from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):

    scores = [0, 1, 2, 3, 4, 5]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open_time = StringField('Open', validators=[DataRequired()])
    close_time = StringField('Close', validators=[DataRequired()])

    rating = SelectField('Coffee', choices=["✘" if score == 0 else "☕"*score for score in scores], default=0, validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=["✘" if score == 0 else "💪"*score for score in scores], default=0, validators=[DataRequired()])
    power = SelectField('Power', choices=["✘" if score == 0 else "🔌"*score for score in scores], default=0, validators=[DataRequired()])

    submit = SubmitField('Submit')

    def get_data(self):
        data_list = [self.cafe.data, self.location.data, self.open_time.data, self.close_time.data, self.rating.data, self.wifi.data, self.power.data]

        return ",".join(data_list)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        new_entry = form.get_data()

        with open("cafe-data.csv", "a") as csv_file:
            csv_file.write("\n" + new_entry)

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
