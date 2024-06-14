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
        self.entrybox.get()
        self.entrybox.place(x= 270, y=195)
        self.entrybox.insert(0, "Enter your name here")

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

def questions():
        master.destroy
        questions = tk.Tk()
        questions.title("Anime Quiz! (Questions)")
        questions.geometry("640x360")
        questions.configure(background="#FFAF45")

#------------------------------------------------------
# Start of questions:

        def check():
              pass

        question_label = tk.Label(questions, 
                             text = "Question #XX", 
                             bg = "#FFAF45")
        question_label.config(font = "Courier 17", 
                         fg = "#FB6D48")
        question_label.pack(pady = 10)

#Question options: 
        op_1 = IntVar()
        op_2 = IntVar()
        op_3 = IntVar()
        op_4 = IntVar()

#Question options:
        option_1 = tk.Checkbutton(questions, 
                               text = "(Option #1)", 
                               variable=op_1)
        option_1.config(font = "Courier 9", 
                        bg = "#673F69",
                        fg = "#FB6D48")
        option_1.pack(pady = 10)

        option_2 = tk.Checkbutton(questions, 
                               text = "(Option #2)", 
                               variable=op_2)
        option_2.config(font = "Courier 9", 
                        bg = "#673F69",
                        fg = "#FB6D48")
        option_2.pack(pady = 10)
        
        option_3 = tk.Checkbutton(questions, 
                               text = "(Option #3)", 
                               variable=op_3)
        option_3.config(font = "Courier 9", 
                        bg = "#673F69",
                        fg = "#FB6D48")
        option_3.pack(pady = 10)

        option_4 = tk.Checkbutton(questions, 
                               text = "(Option #4)", 
                               command = lambda:check(1),
                               variable=op_4)
        option_4.config(font = "Courier 9", 
                        bg = "#673F69",
                        fg = "#FB6D48")
        option_4.pack(pady = 10)

#Next button: 
        next_button = tk.Button(questions, 
                                text = "Next Question", 
                                command = final_page)
        next_button.config(font = "Courier 9", 
                        background = "#D74B76", 
                        foreground = "#FB6D48", 
                        height = 1, 
                        width = 15)
        next_button.pack()

        questions.mainloop()


#------------------------------------------------------
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



        