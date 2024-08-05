import tkinter as tk;
from tkinter import *;

root = tk.Tk();
root.title("Inputs");
root.geometry("700x400");
root.minsize(width=400,height=350);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# THIS FUNCTION FOR WRITE NAME FROM INPUT;
def WriteName(): 
    name.configure(text="Hello, " + StrName.get());

def ClickToExit():
    root.destroy();

h1 = Label(root,text="Enter your name!", font=("Arial", 15));
h1.place(x=180,y=10);

StrName = tk.StringVar();
EnterYourName = Entry(root,textvariable=StrName,bd=0,relief="solid", highlightthickness=2);
EnterYourName.place(width=170,height=25,x=180,y=50);
EnterYourName.focus();

submitBtn = Button(root, text="Send ..", background="#dfdfdf",bd=0,command=WriteName);
submitBtn.place(width=170,height=25,x=180,y=100);

BtnExit = Button(root, text="Exit!", background="#dfdfdf",foreground="red",bd=1,relief="solid",command=ClickToExit);
BtnExit.place(width=100,height=25,x=10,y=10);

name = Label(root,text="Hello,");
name.place(height=20,x=500,y=10);

root.mainloop();