from tkinter import *

import tkinter as tk

from tkinter import PhotoImage

from quiz_questions import quiz_questions

from tkinter import messagebox

#------------------------------------------------------
# Welcome Page

class welcomepage:
    def __init__(self, master):
#------------------------------------------------------
# Title
        welcome_title: Label = Label(master, text= "Anime Quiz!")
        welcome_title.place(x=230, y=100)
        welcome_title.config(font = "Courier 25 bold", 
                             foreground = "#FB6D48", 
                             background = "#FFAF45")

#------------------------------------------------------
# Entry box
        self.entrybox = Entry(master)
        self.entrybox.place(x= 270, y=195)
        self.entrybox.insert(0, "Enter your name here")

#------------------------------------------------------
# Continue Button

        continue_button: Button = Button(master, text= "Continue", command = instructions)
        continue_button.config(font = "Courier 9", 
                                background = "#D74B76", 
                                foreground = "#FB6D48", 
                                height = 1, 
                                width = 15)
        continue_button.place(x=275, y=240)

        name = self.entrybox.get()  
        
#------------------------------------------------------
#Main window for instruction page
def instructions():
        master.destroy()
        page = tk.Tk()
        page.title("Anime Quiz! (Instructions)")
        page.geometry("350x250")
        page.configure(background="#FFAF45")

#------------------------------------------------------
#Title for Instruction Page
        Title = tk.Label(page, 
                         text = "Welcome," + name +"!", 
                         background = "#FFAF45")
        Title.config(font = "Courier 17", 
                     foreground = "#FB6D48")
        Title.pack()

#------------------------------------------------------
# Users name (stored name from welcomepage class)
        name = tk.Label(page, 
                        text = "Users Name + (username)")
        name.config(font = "Courier 12", 
                    foreground = "#D74B76",
                    background = "#FFAF45")
        name.pack(pady = 10)

#------------------------------------------------------
# Main Quiz Instructions 
        steps = tk.Label(page, text = "Welcome to the Anime Quiz! \n You will be answering 25 randomised anime questions. \n These Questions will originate from popular Animes such as; \n One Piece, My Hero Acadamia and Naruto \n Good Luck! :)")
        steps.config(background = "#673F69", 
                     foreground = "#FB6D48")
        steps.pack(pady = 10)

#------------------------------------------------------
# Continue Button
        Continue = tk.Button(page, 
                             text = "Continue", 
                             command = questions)
        Continue.config(font = "Courier 9", 
                        background = "#D74B76", 
                        foreground = "#FB6D48", 
                        height = 1, 
                        width = 15)
        Continue.pack(pady = 10)

        page.mainloop

#------------------------------------------------------
# Start of questions

quiz_questions = quiz_questions
   

class Questions:
    def __init__(self, master):

        self.current_question = 0
        self.score = 0

        self.master = master
        self.master.title("Anime Quiz!")
        self.master.geometry("1900x360")
        self.master.configure(background="#FFAF45")

        self.question_label = Label(self.master, 
                                    text = "", 
                                    bg="#FFAF45", 
                                    font = "Courier 17",
                                    fg = "#FB6D48")
        self.question_label.pack(pady=20)

        self.choice_buttons = []
        for i in range(4):
            choices = Button(self.master, 
                                   text = "", 
                                   bg = "#673F69",
                                   fg = "#FB6D48", 
                                   command = lambda i=i: self.answer_check(i))
            choices.pack(pady=5)
            self.choice_buttons.append(choices)

        self.right_wrong = Label(self.master, 
                                 text = "", 
                                 bg = "#FFAF45", 
                                 fg = "#FB6D48")
        self.right_wrong.pack(pady=10)

        self.score_label = Label(self.master, 
                                 text="", 
                                 bg = "#FFAF45", 
                                 fg = "#FB6D48")
        self.score_label.pack()

        self.Continue = Button(self.master, 
                                  text="Continue", 
                                  command=self.next_question)
        self.Continue.pack(pady=10)

        self.show_next_question()

    def show_next_question(self):
        if self.current_question < len(quiz_questions):
            question_data = quiz_questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.choice_buttons[i].config(text=option)

            self.right_wrong.config(text="")
            self.Continue.config(font = "Courier 9", 
                        background = "#D74B76", 
                        foreground = "#FB6D48", 
                        height = 1, 
                        width = 15, 
                        state = DISABLED)
        else:
            self.show_result_page()

    def answer_check(self, choice_index):
        selected_answer = self.choice_buttons[choice_index].cget("text")
        correct_answer = quiz_questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            self.right_wrong.config(text="Correct!", 
                                    fg = "green", 
                                    font = "Courier 12")
        else:
            self.right_wrong.config(text="Incorrect!", 
                                    fg = "red", 
                                    font = "Courier 12")

        self.score_label.config(text = f"Score: {self.score}/{len(quiz_questions)}")
        self.Continue.config(state = NORMAL)

    def next_question(self):
        self.current_question += 1
        self.show_next_question()

    def show_result_page(self):
        result_page = tk.Toplevel(self.master)
        result_page.title("Quiz Result")
        result_page.geometry("300x150")
        result_page.configure(background="#FFAF45")

        result_label = Label(result_page, text=f"Quiz Completed!\nYour final score is: {self.score}/{len(quiz_questions)}", background="#FFAF45", foreground="#FB6D48", font="Courier 15")
        result_label.pack(pady=20)

        close_button = Button(result_page, text="Close", command=self.master.destroy)
        close_button.pack(pady=10)

#----------------------------------------------------
#Final page, score
def final_page():
    pass
      
#------------------------------------------------------
# ..

if __name__ == "__main__":
    master = Tk()
    master.title("Anime Quiz!")
    master.geometry("640x360")
    image_path = PhotoImage(file="Image1.png")
    bg_image = tk.Label(master, image = image_path)
    bg_image.place(relheight=1, relwidth=1)
    welcomepage(master)
    master.mainloop()
    root = tk.Tk()
    app = Questions(root)
    root.mainloop()



        