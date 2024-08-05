import tkinter as tk;
from tkinter import *;

root = tk.Tk();
root.title("Spind box");
root.geometry("850x400");
root.minsize(width=400,height=350);
# root.resizable(False,False);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# BUILD A FUNCTION TO WRITE MY AGE
def WriteMyAge():
    lblAges.configure(text= f"How old are u? I have {variableAge.get()} years old");

lblAges = Label(root,text="How old are u?",font=("Ariabl", 17));
variableAge = tk.IntVar(); 
ListAges = list(range(18,99));
SpinBoxA = Spinbox(root,textvariable=variableAge,values=ListAges,font=("Ariabl", 15), command=WriteMyAge);

lblAges.place(x=150,y=30);
SpinBoxA.place(x=150,y=70,width=150,height=25);

# BUILD A FUNCTION TO WRITE MY FAVORITE SEASON
def WriteMySeason():
    lblSeason.configure(text= f"What's your favorate season ? My favorate season is {variableS.get()}");

lblSeason = Label(root,text="What's your favorate season ?",font=("Ariabl", 17));
variableS = tk.StringVar();
arrListSeason = ["spring","summer","fall","winter"] 
SpinBoxS = Spinbox(root,textvariable=variableS,values=arrListSeason,font=("Ariabl", 15), command=WriteMySeason);

lblSeason.place(x=150,y=120);
SpinBoxS.place(x=150,y=160,width=150,height=25);



root.mainloop();