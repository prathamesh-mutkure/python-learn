from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def say_hello():
    return render_template("index.html")


@app.route("/angela")
def hello_angela():
    return render_template("angela.html")


if __name__ == "__main__":
    app.run(debug=True)
