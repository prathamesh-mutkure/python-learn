from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title(string="Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white", bd=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 130, text="Hello", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, bd=0, highlightthickness=0, height=95, width=98,
                               command=self.true_btn_tapped, )
        self.false_btn = Button(image=false_img, bd=0, highlightthickness=0, height=95, width=98,
                                command=self.false_btn_tapped, )
        self.true_btn.grid(column=0, row=2)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.change_bg("white")

        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            score = self.quiz_brain.score
            self.canvas.itemconfig(self.question_text, text=question)
            self.score_label.config(text=f"Score: {score}")
        else:
            self.canvas.itemconfig(self.question_text, text="The quiz has ended")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn_tapped(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_btn_tapped(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.change_bg("green")
        else:
            self.change_bg("red")

        self.window.after(1000, self.get_next_question)

    def change_bg(self, color):
        self.canvas.config(bg=color)
