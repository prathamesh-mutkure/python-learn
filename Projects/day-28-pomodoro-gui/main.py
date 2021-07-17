from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    global reps

    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_marks.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_time = 15
    short_break_time = 5
    long_break_time = 10

    # work_time = WORK_MIN * 60
    # short_break_time = SHORT_BREAK_MIN * 60
    # long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_time)
        reps = 0
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_time)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_time)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    global timer
    count_min = count // 60
    count_sec = count % 60

    count_min = f"0{count_min}" if count_min < 10 else count_min
    count_sec = f"0{count_sec}" if count_sec < 10 else count_sec

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(500, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text="✔"*(reps//2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro GUI")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

check_marks = Label(text="", fg=PINK, bg=YELLOW)
check_marks.grid(column=1, row=3)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)


window.mainloop()
