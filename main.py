import tkinter as tk

import random

names = []
global questions_answers
asked = [] 
score = 0

root = tk.Tk()
root.title("Anime Quiz")

Welcome = tk.Canvas(root, width=500, height=500)
Welcome.pack()

label1 = tk.Label(root, text="The Glorious Anime Quiz!")
label1.config(font=("courier new", 20))
Welcome.create_window(200, 35, window=label1)

label2 = tk.Label(root, text="Enter Your Name Here")
label2.config(font=("courier new", 10))
Welcome.create_window(200, 100, window=label2)

entry = tk.Entry(root)
Welcome.create_window(200, 140, window=entry)

root.mainloop()