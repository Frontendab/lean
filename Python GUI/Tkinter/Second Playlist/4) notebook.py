from tkinter import *;
from tkinter import ttk;

root = Tk();
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico")
root.title("Notebook");
root.geometry("450x400+450+400");
root.maxsize(width=600,height=600);
root.minsize(width=400,height=350);

nb = ttk.Notebook(root);
nb.place(x=0,y=0);

tab1 = Frame(nb, width=298,height=400, background="green");
nb.add(tab1, text="Home");
lbl1 = Label(tab1, text="You are in first tab");
lbl1.place(x=20,y=20);

tab2 = Frame(nb, width=450,height=400, background="orange");
nb.add(tab2, text="About us");
lbl2 = Label(tab2, text="We are a compnay from Morocco..");
lbl2.place(x=20,y=20);

mainloop();
