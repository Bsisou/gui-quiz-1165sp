from tkinter import *

import tkinter as tk

#------------------------------------------------------
# main window for instruction page
if __name__ == "__main__":
    page = tk.Tk()
    page.title("Anime Quiz! (Instructions)")
    page.geometry("350x180")
    page.configure(background="#FFAF45")
    
#------------------------------------------------------
#Title for Instruction Page
    Title = tk.Label(page, 
                  text="Welcome!", 
                  background="#FFAF45"
                  )
    Title.config(font = "Courier 17", 
                 foreground = "#FB6D48")
    Title.pack()

#------------------------------------------------------
# Users name (stored name from main)
    name = tk.Label(page, 
                    text = "(Users Name)", 
     )
    name.config(font = "Courier 12", 
                foreground = "#D74B76", 
                background="#FFAF45")
    name.pack(pady = 10)

#------------------------------------------------------
# Main Quiz Instructions
    instructions = tk.Label(page, 
                            text = 
    "Welcome to the Anime Quiz! \n You will be answering 25 randomised questions. \n These Questions will originate from popular Animes such as; \n One Piece, My Hero Acadamia and Naruto")
    instructions.config(font = "Courier 7", 
                        foreground = "#FB6D48", 
                        background = "#673F69")
    instructions.pack()

#------------------------------------------------------
# Continue Button

Continue = tk.Button(page, 
                     text = "Continue", 
                     )
Continue.config(font = "Courier 9", 
                background = "#D74B76", 
                foreground = "#FB6D48", 
                height = 1, 
                width = 15)
Continue.pack(pady = 10)


page.mainloop()