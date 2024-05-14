from tkinter import *

from PIL import Image, ImageTk

import random

names = []
global questions_answers
asked=[]
score=0

class Quizstarter:
  def __init__(self, parent): 
    background_color="OldLace"
    self.quiz_frame=Frame(parent, bg = "grey", padx=100, pady=100) #"The Frame"
    self.quiz_frame.grid()

    self.heading_label=Label(self.quiz_frame, text="The Glorious Anime Quiz!", bg="yellow") #Title of quiz
    self.heading_label.grid(row=0, padx=20)

    #Entry Box Label
    self.user_label=Label(self.quiz_frame, text="Enter your name: ", bg="red")
    self.user_label.grid(row=1, padx=20, pady=20)

    #The Entry Box
    self.entry_box=Entry(self.quiz_frame) 
    self.entry_box.grid(row=2, padx=20, pady=20)

    #The Continue Button
    self.continue_button = Button(self.quiz_frame, text="Continue", bg="yellow")
    self.continue_button.grid(row=3, padx=20, pady=20)

if __name__ == "__main__":
  root = Tk()
  root.title("Quiz :)")
  root.geometry("350x500")
  quiz_instance = Quizstarter(root)
  quiz_starter_object = Quizstarter(root) #instantiation, making an instance of the class Quiz

  def name_collection(self):
    name=self.entry_box.get()
    name.append(name) 
    self.quiz_frame.destroy()
    Quiz(root)
  
  # So the window doesn't disappear
  root.mainloop() 

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

randomiser()

randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("Nz Road Rules Quiz")
  quiz_instance = Quizstarter(root)
  root.mainloop


    










