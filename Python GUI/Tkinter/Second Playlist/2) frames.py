from tkinter import *;

root = Tk();
root.title("App");
root.geometry("600x400+700+200");
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

divLeft = Frame(root, width=298,height=400, background="green");
divLeft.place(x=1,y=1);

divRight = Frame(root, width=298,height=400, background="orange");
divRight.place(x=300,y=0);

btn1 = Button(divLeft, text="Into first frame", background="#dfdfdf");
btn1.place(x=10,y=10);

btn10 = Button(divLeft, text="Into first frame", background="#dfdfdf");
btn10.place(x=10,y=40);

btn2 = Button(divRight, text="Into first frame", background="#dfdfdf");
btn2.place(x=10,y=10);

mainloop();