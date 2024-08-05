import tkinter as tk;
from tkinter import *;

win = Tk();
win.title("Text");
win.geometry("450x500");
win.minsize(width=400,height=350);
# win.resizable(False,False);
win.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

#? ======= Creating space Text ========
text = Text(win);
text.place(width=350,height=180,x=50,y=50);

#? ======= Inserting default text ========
text.insert("1.0", "Hello world");
text.insert(END, "\nI like the Morocoo");

#? ======== Creating label to save text ========
lbl = Label(win, text="", relief="groove");
lbl.place(width=350,height=120,x=50,y=250);

#? ======== Creating btn for clear text and label ========
def IsClear(): 
    text.delete("1.0", "end");
    text.focus();
    IsSave();
    
BtnClear = Button(win,text="Clear", command=IsClear);
BtnClear.place(width=100,height=30,x=50,y=380);

#? ======== Creating btn for save text in label ========
def IsSave(): 
    valueText = text.get("1.0", "end");
    lbl.config(text=valueText);

BtnSave = Button(win,text="Save", command=IsSave);
BtnSave.place(width=100,height=30,x=300,y=380);

mainloop();