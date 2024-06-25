from tkinter import *

import tkinter as tk

from tkinter import PhotoImage

from quiz_questions import quiz_questions
#------------------------------------------------------
# Welcome Page

class Welcomepages: #start of quiz
    def __init__(self, master):
        self.master = master
#------------------------------------------------------
# Title
        welcome_title = Label(master, text= "Anime Quiz!") # displays text "Anime Quiz!" in gui
        welcome_title.place(x=150, y=100)
        welcome_title.config(font = "Courier 40 bold", 
                             foreground = "#FB6D48", 
                             background = "#673F69") # Conifgures the colour and dimensions of the welcome title

#------------------------------------------------------
# Entry box
        self.entrybox = Entry(master) # entry box for user to enter their name
        self.entrybox.place(x= 270, y=195)
        self.entrybox.insert(0, "Enter your name here")# text that displays "Enter your name here" in entry box

#------------------------------------------------------
# Continue Button

        continue_button = Button(master, text= "Continue", 
                                         command = self.instructions)# continue button that commands the next component to run
        continue_button.config(font = "Courier 9", 
                                background = "#D74B76", 
                                foreground = "#FB6D48", 
                                height = 1, 
                                width = 15) # Conifgures the colour and dimensions of continue button
        continue_button.place(x=275, y=240)# places the orientation, (x and y) for continue button

    def entry_boundary(self, input_text):
        if len(input_text) <=15:
            return True 
        else:
            return False
        
#------------------------------------------------------
#Main window for instruction page
    def instructions(self): # start of instructions component
        username = self.entrybox.get()# gets users name inputted from entry box


        username = self.entrybox.get().strip()  
        if username == "" or username == "Enter your name here": # checks if username is correct or not
          
            error = Label(self.master, 
                          text="Please enter your name! (Name must be 15 characters or less)", 
                          fg="red", 
                          bg = "#673F69") # displays text in red "Please enter your name!"
            error.place(x=170, y=300)
            return

        self.master.destroy()# destroys previous component 
        page = tk.Tk()
        page.title("Anime Quiz! (Instructions)") # displays "Anime Quiz! (Instructions)" on the tab (outside of the gui) 
        page.geometry("350x250")# changes the size of the window
        page.configure(background="#FFAF45") # changes colour of the window

#------------------------------------------------------
#Title for Instruction Page
        Title = tk.Label(page, 
                         text = "Welcome!", 
                         background = "#673F69") # displays welcome title at top of the page
        Title.config(font = "Courier 17", 
                     foreground = "#FB6D48") # changes font and colour of welcome title
        Title.pack()

#------------------------------------------------------
# Users name (stored name from welcomepage class)
        name = tk.Label(page, 
                        text = f"Hello, {username}!") # displays "Hello, (Users name)" in text
        name.config(font = "Courier 12", 
                    foreground = "#D74B76",
                    background = "#FFAF45") # changes colours and font of text 
        name.pack(pady = 10)

#------------------------------------------------------
# Main Quiz Instructions 
        steps = tk.Label(page, text = "Welcome to the Anime Quiz! \n You will be answering randomised anime questions. \n These Questions will originate from popular Animes such as; \n One Piece, My Hero Acadamia and Naruto \n Good Luck! :)")
        steps.config(background = "#673F69", 
                     foreground = "#FB6D48") # changes colours of instructions
        steps.pack(pady = 10)

#------------------------------------------------------
# Continue Button
        continueB = tk.Button(page, 
                             text = "Continue", 
                             command = lambda: self.start_quiz(page, username)) # Command to start the next component (start quiz) 
        continueB.config(font = "Courier 9", 
                        background = "#D74B76", 
                        foreground = "#FB6D48", 
                        height = 1, 
                        width = 15) # changes colours and font of continue button
        continueB.pack(pady = 10)

        page.mainloop()

    
    def start_quiz(self, page, username): # start of quiz component 
        page.destroy()  # Close the instruction window
        root = tk.Tk()
        app = Questions(root, username) # starts questions class to display this component
        root.mainloop()

#------------------------------------------------------
# Start of questions

quiz_questions = quiz_questions
   
class Questions:
    def __init__(self, master, username):

        self.current_question = 0 # initializes current_question index to 0
        self.score = 0 # initializes score index to 0
        self.username = username

        self.master = master
        self.master.title("Anime Quiz!") # displays "Anime Quiz! (Questions)" on the tab (outside of the gui) 
        self.master.geometry("1900x360") # changes size of quiz component
        self.master.configure(background="#FFAF45") # changes colour of background for component

        self.question_label = Label(self.master, 
                                    text = "", 
                                    bg="#673F69", 
                                    font = "Courier 17",
                                    fg = "#FB6D48") # displays question_label (taken from quiz_questions.py)
        self.question_label.pack(pady=20)

        self.choice_buttons = []
        for i in range(4):
            choices = Button(self.master, 
                                   text = "", 
                                   bg = "#673F69",
                                   fg = "#FB6D48", 
                                   command = lambda i=i: self.answer_check(i)) # displays choices under question, also changes colours of buttons
            choices.pack(pady=5)
            self.choice_buttons.append(choices)

        self.right_wrong = Label(self.master, 
                                 text = "", 
                                 bg = "#FFAF45", 
                                 fg = "#FB6D48") # displays a green or red, right or wrong below choice_buttons 
        self.right_wrong.pack(pady=10)

        self.score_label = Label(self.master, 
                                 text="", 
                                 bg = "#FFAF45", 
                                 fg = "#FB6D48") # displays current score below right_wrong label
        self.score_label.pack()

        self.Continue = Button(self.master, 
                                  text="Continue", 
                                  command=self.next_question) # Continue button to command the next question to start
        self.Continue.pack(pady=10)

        self.quiz_completed = False # checks if quiz is completed
        self.result_page = None #created placeholder for result page

        self.show_next_question()

    def show_next_question(self):
        if self.current_question < len(quiz_questions): # Checks from quiz_questions if there are more questions left
            question_data = quiz_questions[self.current_question]
            self.question_label.config(text=question_data["question"]) # displays "question" from "quiz_questions.py"

            for i, option in enumerate(question_data["options"]): # displays next set of questions from "options" in "quiz_questions.py"
                self.choice_buttons[i].config(text=option)

            self.right_wrong.config(text="") # clears right or wrong message from last question
            self.Continue.config(font = "Courier 9", 
                        background = "#D74B76", 
                        foreground = "#FB6D48", 
                        height = 1, 
                        width = 15, 
                        state = DISABLED) # displays continue button for next question
        else:
            if not self.quiz_completed:
                self.show_result_page() # in case all questions are finished it will display result page
                self.quiz_completed = True
           

    def answer_check(self, choice_index):# checks whether answer is correct or wrong
        selected_answer = self.choice_buttons[choice_index].cget("text") #checks which button user selected
        correct_answer = quiz_questions[self.current_question]["answer"] #checks if answer is correct from "answer" in "quiz_questions.py"

        if selected_answer == correct_answer: # checks if the selected button matches the answer in quiz_questions
            self.score += 1
            self.right_wrong.config(text="Correct!", 
                                    fg = "green", 
                                    font = "Courier 12") # displays correct in green
        else:
            self.right_wrong.config(text="Incorrect!", 
                                    fg = "red", 
                                    font = "Courier 12") # displays incorrect in red

        self.score_label.config(text = f"Score: {self.score}/{len(quiz_questions)}") # changes score label if question si correct
        self.Continue.config(state = NORMAL) # displays continue button again

    def next_question(self): # continues to next question 
        self.current_question += 1 # changes current_question index by +1 every question 
        self.show_next_question() # displays show_next_question 
    
        if self.current_question == len(quiz_questions): #checks if quiz is completed before displaying result page
            if not self.quiz_completed:
                self.show_result_page()  # in case all questions are finished it will display result page
                self.quiz_completed = True # changes placholder from False -> True
            
#----------------------------------------------------
# RESULTS/FINAL PAGE 
    def show_result_page(self): # creates window above questions to display result page
        if self.result_page is None:
                    result_page = tk.Toplevel(self.master) # "Toplevel" ensures that the window is above
        result_page.title("Quiz Result") # changes title to "Quiz Result"
        result_page.geometry("300x150") # changes size of window
        result_page.configure(background="#FFAF45") # changes background colour 

        result_label = Label(result_page, text=f"Quiz Completed!\nYour final score is: {self.score}/{len(quiz_questions)}", 
                             bg = "#673F69", 
                             fg = "#FB6D48", 
                             font="Courier 15")
        result_label.pack(pady=20) # displays "Quiz Completed!" and final score (taken from score index)

        close_button = Button(result_page, text = "Close", 
                              command=self.master.destroy) # close button, (commands self.master) destroy and closes entire program
        close_button.config(bg = "#D74B76", 
                            fg = "#FB6D48")
        close_button.pack(pady=10)

#------------------------------------------------------
# ..

if __name__ == "__main__":
    master = Tk() # creates window for the main "Anime Quiz!" 
    master.title("Anime Quiz!") # sets title "Anime Quiz!"
    master.geometry("640x360") # sets window size 
    image_path = PhotoImage(file="Image1.png") # sets Image1.png as background for "Anime Quiz!"
    bg_image = tk.Label(master, image = image_path) # points to path for background and displays background
    bg_image.place(relheight=1, relwidth=1) # places image to cover entire window
    Welcomepages(master) # calls welcomepage function
    master.mainloop()
    root = tk.Tk()
    app = Questions(root) # creates instance for Questions
    root.mainloop()