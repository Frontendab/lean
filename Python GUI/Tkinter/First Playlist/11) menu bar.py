import tkinter as tk;
from tkinter import *;
from tkinter.messagebox import showinfo;
from tkinter.messagebox import askyesno;


win = Tk();
win.title("Menu bar");
win.geometry("300x150");
# win.minsize(width=400,height=350);
# win.resizable(False,False);
win.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# Creating menu bar
menuBar = Menu(win);

# Adding main menu and commands
mainMenu = Menu(menuBar, tearoff=0);
menuBar.add_cascade(label="Main", menu=mainMenu);

# build a function for build 
def BuildIt(): 
    showinfo(title="Building", message="Done, it is build it!");
mainMenu.add_command(label="Build", command=BuildIt);

# build a function for reset
def ResetIt(): 
    showinfo(title="Reset", message="Done, it is reset it!");
mainMenu.add_command(label="Reset", command=ResetIt);

# build a function for remove 
def RemoveIt(): 
    showinfo(title="Remove", message="Done, it is removed it!");
mainMenu.add_command(label="Remove", command=RemoveIt);

mainMenu.add_separator();

# build a function to quit
def IsQuit(self = None):
    answer = askyesno(title="Quit", message="Are u sure u want to quit?");
    if answer: win.quit();

mainMenu.add_command(label="Quit!", command=IsQuit);

# Adding main menu and commands
AboutMenu = Menu(menuBar, tearoff=0);
menuBar.add_cascade(label="About us", menu=AboutMenu);

# build a function to information
def InformationIt(self = None): 
    showinfo(title="Informatino", message="We are a company from Morocco");
AboutMenu.add_command(label="Information", command=InformationIt, accelerator="Ctrl+I");

AboutMenu.add_separator();

# build a function to information
def InformationItM(): 
    showinfo(title="Country", message="We are living in Morocco.");
AboutMenu.add_command(label="Country", command=InformationItM);

win.bind_all("<Control-i>", InformationIt);

win.bind_all("<Control-q>", IsQuit);

win.config(menu= menuBar);

mainloop();