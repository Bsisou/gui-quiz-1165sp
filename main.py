from tkinter import *

from PIL import Image, ImageTk

import random

from quiz_questions import quiz_questions

collected_names = []
global questions_answers
questions=[]
current_score=0

class Quiz: 
  def __init__(main, parent): 
    background_color="OldLace"
    main.quiz_frame=Frame(parent, padx=100, pady=100) #"The Frame"
    main.quiz_frame.grid()
    main.bg_image = Image.open("Image1.png") # Background image
    main.bgimage = main.bg_image.resize((350, 500), Image.LANCZOS)
    main.bg_image = ImageTk.PhotoImage(main.bg_image)
    main.bg_image = PhotoImage(file="Image1.png")

    main.image_label = Label(main.quiz_frame, image=main.bg_image) # Label for background image
    main.image_label.place(x=0, y=0, relwidth=1, relheight=1)
   
    main.heading_label=Label(main.quiz_frame, text="The Glorious Anime Quiz!", bg="orange") #Title of quiz
    main.heading_label.grid(row=0, padx=20)

    #Entry Box Label
    main.user_label=Label(main.quiz_frame, text="Enter your name: ", bg="red") 
    main.user_label.grid(row=1, padx=20, pady=20)

    #The Entry Box
    main.entry_box=Entry(main.quiz_frame) 
    main.entry_box.grid(row=2, padx=20, pady=20)

    #The Continue Button
    main.continue_button = Button(main.quiz_frame, text="Continue", bg="yellow", command=collected_names)
    main.continue_button.grid(row=3, padx=20, pady=20)

    #value for radio buttons for questions
    main.var1=IntVar()

if __name__ == "__main__":
  WelcomeW = Tk()
  WelcomeW.title("Anime Quiz :)")
  WelcomeW.geometry("350x500")
  quiz_instance = Quiz(WelcomeW)
  quiz_starter_object = Quiz(WelcomeW) #instantiation, making an instance of the class Quiz
  WelcomeW.mainloop
  

  def collected_names(main):
    main=main.entry_box.get()
    main.append(collected_names) 
    main.quiz_frame.destroy()
    Quiz(WelcomeW)
  
  # So the window doesn't disappear
WelcomeW.mainloop() 

def randomiser():
  global questionnumber
  questionnumber = random.randint(1,10)
  if questionnumber not in asked:
    asked.append(questionnumber)
  elif questionnumber in asked:
    randomiser()

