
import tkinter as tk;
from tkinter import *;

root = tk.Tk();
root.title("ListBoxs");
root.geometry("450x400");
root.minsize(width=400,height=350);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# CREATE SPACE TO WRITE NUMBER CHOOSE ITEM
item = Label(root, text="Select is : ", font=("Arial", 15));
item.place(x=170,y=10);

# BUILD FUNCTION TO WRITE NUMBER IS CHOOSING
def WriteNumChoosing(event): 
    result = ListBox.curselection()[0];
    # This code get an id of lag id choosing
    # item.configure(text="Select is : " + str(result));
  
    # This code get a lags is choosing
    item.configure(text="Select is : " + lags[result]);

# CREATE LANGS LIST BOX

lags = ["Html","Css","Bootstrap","Scss","Js","React Js", "Python", "Tkinter", "PyGt"];
listLags = tk.StringVar(value=lags);
ListBox = Listbox(root, listvariable=listLags,font=("Arial",14));
ListBox.place(x=110,y=50);

# IF YOU WANT USE DOUBLE CLICK ON EVENT
# ListBox.bind("<Double-1>", WriteNumChoosing);

# IF YOU WANT USE SENGLE CLICK ON EVENT
ListBox.bind("<<ListboxSelect>>", WriteNumChoosing);



root.mainloop();