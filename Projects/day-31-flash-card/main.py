from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, timer
    window.after_cancel(timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=image_front)

    timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card, timer
    window.after_cancel(timer)
    english_word = current_card["English"]

    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=image_back)

    timer = window.after(3000, func=next_card)


def save_new_data():
    new_data = pandas.DataFrame(data=to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)


def remove_word():
    to_learn.remove(current_card)
    save_new_data()
    next_card()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title(string="Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthicknes=0)

image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
image_wrong = PhotoImage(file="images/wrong.png")
image_right = PhotoImage(file="images/right.png")

canvas_image = canvas.create_image(400, 263, image=image_front)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = Button(image=image_wrong, highlightthicknes=0, bd=0, width=95, height=95, command=next_card)
right_btn = Button(image=image_right, highlightthicknes=0, bd=0, width=95, height=95, command=remove_word)
wrong_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

timer = window.after(3000, func=flip_card)
next_card()

window.mainloop()
