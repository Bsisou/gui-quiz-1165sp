from tkinter import *

import tkinter as tk

from tkinter import PhotoImage

from quiz_questions import quiz_questions

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
        global username
        username = self.entrybox.get()

#------------------------------------------------------
# Continue Button
        continue_button: Button = Button(master, text= "Continue", 
                                         command = instructions)
        continue_button.config(font = "Courier 9", 
                                background = "#D74B76", 
                                foreground = "#FB6D48", 
                                height = 1, 
                                width = 15)
        continue_button.place(x=275, y=240)
        
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
                         text = "Welcome", 
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

def answer_check():
      pass

def next():
      pass

def questions():
        master.destroy
        questions = tk.Tk()
        questions.title("Anime Quiz! (Questions)")
        questions.geometry("640x360")
        questions.configure(background="#FFAF45")

#------------------------------------------------------
# Start of questions

        questions = tk.Label(questions, 
                             text = "Question #1", 
                             bg = "#FFAF45")
        questions.config(font = "Courier 17", 
                     foreground = "#FB6D48")
        questions.pack()

        choices = []
        for i in range(4):
              choice_button = tk.Button(questions, 
                                        command = lambda i=i: answer_check(i)
                                        )
              choice_button.pack(pady = 10)
              choices.append(choice_button)
        
        correct_incorrect = tk.Label(questions)
        correct_incorrect.pack(pady = 10)

        scoreL = tk.Label(questions, 
                          text = "score: 0/{}".format(len(questions))
                          )
        scoreL.pack()
        
        next_question = tk.Button(questions, 
                                  text = "Next Question", 
                                  command = next)
        next_question.pack(pady = 10)
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



        