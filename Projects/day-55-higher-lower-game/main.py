from flask import Flask
import random

app = Flask(__name__)
random_num = 0


@app.route("/")
def hello_world():
    global random_num

    random_num = random.randint(0, 9)
    return "<h1> that says Guess a number between 0 and 9" \
           "<br>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def greet(guess: int):
    if guess == random_num:
        return '<h1>You found me!</h1>' \
               '<br>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess < random_num:
        return '<h1>Too Low, Try Again!</h1>' \
               '<br>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > random_num:
        return '<h1>Too High, Try Again!</h1>' \
               '<br>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    return f"Goto Home Route"


if __name__ == "__main__":
    app.run(debug=True)
