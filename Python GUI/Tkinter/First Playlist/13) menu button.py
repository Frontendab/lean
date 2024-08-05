import tkinter as tk;
from tkinter import *;
from tkinter.messagebox import showinfo;

win = Tk();
win.title("Menu button");
win.geometry("400x350");
win.minsize(width=400,height=350);
# win.resizable(False,False);
win.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

#? Creating button menu
BtnMenu = Menubutton(win, text="Menu button", relief="solid", background="#dfdfdf",padx=5);
BtnMenu.place(x=150,y=50);

MainMenu = Menu(BtnMenu, tearoff=0);
BtnMenu["menu"] = MainMenu;

def first():
    showinfo(title="Message", message="You are choosed First");
MainMenu.add_command(label="First", command=first);

def Second():
    showinfo(title="Message", message="You are choosed Second");
MainMenu.add_command(label="Second", command=Second);

def Third():
    showinfo(title="Message", message="You are choosed Third");
MainMenu.add_command(label="Third", command=Third);






mainloop();