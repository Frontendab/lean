from tkinter import *;

home = Tk();

home.title("Home");
home.lift();
home.geometry("400x400+400+200");
home.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

private = Tk();

private.title("private");
private.geometry("400x400+820+200");
private.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");
# private.state("iconic");
# private.iconify();

#? We can use withdraw to hidden window
private.state("withdraw");


mainloop();
