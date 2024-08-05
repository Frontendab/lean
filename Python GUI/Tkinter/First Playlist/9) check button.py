import tkinter as tk;
from tkinter import *;

root = tk.Tk();
root.title("Check button");
root.geometry("400x150");
# root.minsize(width=400, height=350);
# root.resizable(False,False);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# BUILD A FUNCTION TO WRITE ITEM IS SELECTED
def SelectedIt():
    if ValueItem1.get():
        Item1Select.configure(text="Item 1 is Selected");
    else : Item1Select.configure(text="Item 1 is (not) selected");
    if ValueItem2.get():
        Item2Select.configure(text="Item 2 is Selected");
    else : Item2Select.configure(text="Item 2 is (not) selected");

title = Label(root, text="Please Select an item: ", font=("Ariabl", 12));
title.place(x=50,y=15);

ValueItem1 = tk.IntVar();
item1 = Checkbutton(root, text="Item 1", variable=ValueItem1, command=SelectedIt);
item1.place(x=50,y=45);
# This line for Item 1 is selected direcly;
ValueItem1.set(1);

Item1Select = Label(root, text="Item 1 is (not) selected", background="#dfdfdf", relief="solid", padx=10);
Item1Select.place(x=150,y=45);

ValueItem2 = tk.IntVar();
item2 = Checkbutton(root, text="Item 2", variable=ValueItem2, command=SelectedIt);
item2.place(x=50,y=80);

Item2Select = Label(root, text="Item 2 is (not) selected", background="#dfdfdf", relief="solid", padx=10);
Item2Select.place(x=150,y=80);

SelectedIt();

root.mainloop();