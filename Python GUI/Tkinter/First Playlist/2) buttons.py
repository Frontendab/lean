
import tkinter;
from tkinter import *;

root = tkinter.Tk();
root.title("Buttons");
root.geometry("450x400");
# root.minsize(width=400,height=350);
root.resizable(False,False);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

def clickToChangeText():
    title.configure(text="YOU ARE WIN, INCHALAH...");
    btn.configure(state="disabled");

btn = Button(root, text="Click here!", bg="#dfdfdf",activebackground="#dfdfcf",
            fg="red",activeforeground="orange",bd=0,command=clickToChangeText);
btn.place(width=100,height=35,x=180,y=10);

title = Label(root, text="HELLO WORDL", background="#dfdfdf");
title.place(width=200,height=35,x=130,y=50);

def clickToExit():
    root.destroy();

btnExit = Button(root, text="Exit!", bg="#dfdfdf",activebackground="#dfdfcf",
            fg="red",activeforeground="orange",bd=0,command=clickToExit);
btnExit.place(width=100,height=35,x=180,y=100);

root.mainloop();