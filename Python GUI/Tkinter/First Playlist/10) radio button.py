# Importing Tkinter module 
import tkinter as tk;
from tkinter import *;

win = Tk() 
win.geometry("450x400");
win.title("Radio button");
win.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# BUILD A FUCNTION TO RADIO BUTTON
def IsChoosing():
    result.configure(text=f"You are selected {v.get()}");


title = Label(win, text="Please select an item: ", font=("Ariabl", 16));
title.pack(side= TOP, ipady=5);


values = {
        "Python" : "Python",
        "Python Tkinter" : "Python Tkinter",
        "Python Gt" : "Python Gt",
	};

v = StringVar(); 

v.set(values["Python"]);

for (text, value) in values.items(): 
    RadioBtn = Radiobutton(win, text = text, variable = v, 
		value = value, command=IsChoosing);
    RadioBtn.pack(side= TOP, ipady=5);

result = Label(win, text="", font=("Ariabl", 16), relief="groove",width=30,height=1);
result.pack(side= TOP, ipady=5);

IsChoosing();

mainloop()