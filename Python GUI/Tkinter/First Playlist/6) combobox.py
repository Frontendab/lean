import tkinter as tk;
from tkinter import *;
from tkinter import ttk;
from tkinter.messagebox import showinfo;

root = tk.Tk();
root.title("Combo Box");
root.geometry("500x400");
root.minsize(width=400,height=350);
# root.resizable(False,False);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# BUIDL FUNCTION FOR WRITE THE CHOOSING COMBO BOX IN MESSAGE BOX
def IsChoosing(event):
    showinfo(title="Information", message=f"You are selecting {textVariable.get()}")

lbl = Label(root, text="Please select what u want!", font=("Ariabl", 17));
lbl.place(x=120,y=20);

# CREATE ARRAY FOR COMBO BOX
ListComboBox = ["Html","Css","Bootstrap","Scss","Js","React Js","Python","Tkinter"];
textVariable = tk.StringVar();
ComboBox = ttk.Combobox(textvariable=textVariable, values=ListComboBox);
ComboBox.place(height=30,x=170,y=60);
# ComboBox['value'] = ListComboBox;
ComboBox.current(7);
ComboBox.bind("<<ComboboxSelected>>", IsChoosing);

root.mainloop();