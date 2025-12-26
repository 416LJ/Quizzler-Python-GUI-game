from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_NAME = "Arial"
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20,bg=THEME_COLOR)

        self.true_graphic = PhotoImage(file="images/true.png")
        self.false_graphic = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}",fg="white", bg=THEME_COLOR,font=(FONT_NAME, 16,"bold"))
        self.score_label.grid(column=1, row=0)

        self.questions_label = Label(text=f"Questions : {len(self.quiz.question_list)}", fg="white",bg=THEME_COLOR, font=(FONT_NAME, 16, "bold"))
        self.questions_label.grid(column=0, row=0)

        self.mid_canvas = Canvas(width=400, height=450, bg="White", highlightthickness=0)
        self.question_field = self.mid_canvas.create_text(200, 225, text="", width=300,fill="black",font=(FONT_NAME, 20, "italic"),justify="center")
        self.mid_canvas.grid(column=0, row=1, columnspan=2,pady=50)

        self.false_button = Button(image=self.false_graphic, highlightthickness=0, highlightbackground=THEME_COLOR, padx=20, pady=20,command=self.check_false)
        self.false_button.image = self.false_graphic  # Keep a reference!
        self.false_button.grid(column=0, row=2)

        self.true_button = Button(image=self.true_graphic, highlightthickness=0, highlightbackground=THEME_COLOR, padx=20, pady=20,command=self.check_tru)
        self.true_button.image = self.true_graphic  # Keep a reference!
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.mid_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.mid_canvas.itemconfig(self.question_field,text=q_text)
        else:
            self.mid_canvas.itemconfig(self.question_field,text =f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def check_tru(self):
        if self.quiz.check_answer("True"):
            self.score_label.config(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}")
            self.mid_canvas.config(bg="green")
        else:
            self.score_label.config(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}")
            self.mid_canvas.config(bg="red")
        self.window.after(250,self.get_next_question)

    def check_false(self):
        if self.quiz.check_answer("False"):
            self.score_label.config(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}")
            self.mid_canvas.config(bg="green")
        else:
            self.score_label.config(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}")
            self.mid_canvas.config(bg="red")

        self.window.after(250,self.get_next_question)






