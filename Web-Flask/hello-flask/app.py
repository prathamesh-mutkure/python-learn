from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye"


@app.route("/greet/<name>/<int:age>")
def greet(name: str, age: int):
    return f"Hello {name}, your age is {age}!"


if __name__ == "__main__":
    app.run(debug=True)
