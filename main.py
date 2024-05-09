import tkinter as tk #importing tkinter

import random #importing random module

import PIL #importing Python Image library Module

from PIL import Image, ImageTk #importing Image and ImageTk from Pillow


names = []
global questions_answers
asked = [] 
score = 0

root = tk.Tk()
root.title("Anime Quiz")

class Quiz:
    def __init__(Welcome, parent):
        Welcome.quiz_frame=Frame(parent, bg = '#FFAF45')
        Welcome.quiz_frame.grid()    

        Welcome = tk.Canvas(root, width=640, height=480)
        Welcome.configure(bg='#FFAF45')

        label1 = tk.Label(root, text="The Glorious Anime Quiz!")
        label1.config(font=("courier new", 20), bg=('#FFAF45'))
        Welcome.create_window(200, 35, window=label1)

        label2 = tk.Label(root, text="Enter Your Name Here")
        label2.config(font=("courier new", 10), bg=('#FFAF45'))
        Welcome.create_window(200, 100, window=label2)

        entry = tk.Entry(root)
        Welcome.create_window(200, 140, window=entry)
        Welcome.pack()

root.mainloop()