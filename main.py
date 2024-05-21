from tkinter import *

from PIL import Image, ImageTk

import random

names = []
global questions_answers
asked=[]
score=0

class Quizstarter: 
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
    main.continue_button = Button(main.quiz_frame, text="Continue", bg="yellow")
    main.continue_button.grid(row=3, padx=20, pady=20)

if __name__ == "__main__":
  WelcomeW = Tk()
  WelcomeW.title("Anime Quiz :)")
  WelcomeW.geometry("350x500")
  quiz_instance = Quizstarter(WelcomeW)
  quiz_starter_object = Quizstarter(WelcomeW) #instantiation, making an instance of the class Quiz
  WelcomeW.mainloop
  

  def name_collection(main):
    name=main.entry_box.get()
    name.append(name) 
    main.quiz_frame.destroy()
    Quiz(WelcomeW)
  
  # So the window doesn't disappear
WelcomeW.mainloop() 

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

