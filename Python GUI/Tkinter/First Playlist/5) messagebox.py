import tkinter as tk;
from tkinter import *;
from tkinter import messagebox;

root = tk.Tk();
root.title("Message box");
root.geometry("650x400");
root.minsize(width=400, height=350);
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

# root.resizable(False,False);

def showinfo():
    messagebox.showinfo(title="Information ..", message="You can do it what you want but just today in this system..");

btn1 = Button(root, text="Show an information", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=showinfo);
btn1.place(x=110,y=10);
#######################################################
def showwarning():
    messagebox.showwarning(title="Warning ..", message="You have just 5 minutes!");

btn2 = Button(root, text="Click warning", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=showwarning);
btn2.place(x=155,y=60);
#######################################################
def showerror():
    messagebox.showerror(title="Error ..", message="Sorry, but time is end!");

btn3 = Button(root, text="Click error", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=showerror);
btn3.place(x=155,y=110);
#######################################################
def askquestion():
    answer = messagebox.askquestion(title="Question ..", message="Do you work now ?");
    if answer == "yes":
        btn4.configure(text="Ask question, answer is " + answer);
    else: btn4.configure(text="Ask question, answer is " + answer);

btn4 = Button(root, text="Ask question", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=askquestion);
btn4.place(x=155,y=160);
#######################################################
def askokcancel():
    answer = messagebox.askokcancel(title="Question .. ok or cancel", message="Do you work now ?");
    if answer:
        btn5.configure(text="Ask question ok or cancel, answer is " + str(answer));
    else: btn5.configure(text="Ask question ok or cancel, answer is " + str(answer));

btn5 = Button(root, text="Ask question ok or cancel", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=askokcancel);
btn5.place(x=155,y=210);
#######################################################
def askyesnocancel():
    answer = messagebox.askyesnocancel(title="Question .. ok or no or cancel", message="Do you work now ?");
    if answer:
        btn6.configure(text="Ask question ok or no or cancel, answer is " + str(answer));
    elif answer == False: btn6.configure(text="Ask question ok or no or cancel, answer is " + str(answer));
    else: btn6.configure(text="Ask question ok or no or cancel, answer is Cancel");


btn6 = Button(root, text="Ask question ok or no or cancel", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=askyesnocancel);
btn6.place(x=155,y=260);
#######################################################
def askretrycancel():
    answer = messagebox.askretrycancel(title="Question .. retry or cancel", message="Do you work now ?");
    if answer:
        btn7.configure(text="Ask question retry or cancel, answer is " + str(answer));
    else: btn7.configure(text="Ask question retry or cancel, answer is Cancel");

btn7 = Button(root, text="Ask question retry or cancel", background="#dfdfdf",bd=1,relief="solid",
            font=("Ariab", 17),foreground="green", command=askretrycancel);
btn7.place(x=155,y=310);

root.mainloop();