from tkinter import *
import random
from tkinter import messagebox


#Defining gui window
root = Tk()
root.title("Rock, Paper, Scissor by Gaurav")
root.geometry ("720x1080")

# Defining Frames
frame1 = Frame(root)
frame1.pack(side=TOP)

frame2 = Frame(root)
frame2.pack(side=TOP)

# defining functions 
def start():
    root.destroy()
    import gui

def Exit():
    ans=messagebox.askyesnocancel("Confirmation", "Are you sure want to exit")
    if (ans==True):
        root.destroy()


#LABELES AND BUTTONS
Label1=Label(frame1,fg="Dark blue",text="STONE PAPER SCISSOR",font=('algerian',20,'bold'))
Label1.grid(row=1,column=1)

Start_button=Button(frame2,text="START",fg="Yellow",bg="Black",activebackground="Green",command=start)
Start_button.grid(row=1,column=1)

Exit_button=Button(frame2,text="EXIT",fg="YELLOW",bg="BLACK",activebackground="GREEN",command=Exit)
Exit_button.grid(row=2,column=1)

root.mainloop()