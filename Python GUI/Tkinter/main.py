import tkinter
from tkinter import *;

root = tkinter.Tk();
root.title("My app");
root.geometry("500x500");
root.minsize(width=400,height=300);
# root.resizable(False,False);
# lbl = Label(root,text="Hello World", background="orange");

# lbl.pack();
# lbl.place(width=100,height=50,x=50,y=50);

# lbl.configure(foreground="green");

lblFlat = Label(root,text="flat",bd=3, relief="flat");
lblFlat.place(width=100,height=50,x=200,y=0);

lblGroove = Label(root,text="groove",bd=3, relief="groove");
lblGroove.place(width=100,height=50,x=200,y=70);

lblRaised = Label(root,text="raised",bd=3, relief="raised");
lblRaised.place(width=100,height=50,x=200,y=140);

lblRidge = Label(root,text="ridge",bd=3, relief="ridge");
lblRidge.place(width=100,height=50,x=200,y=210);

lblSolid = Label(root,text="solid",bd=3, relief="solid");
lblSolid.place(width=100,height=50,x=200,y=280);

lblSunken = Label(root,text="sunken",bd=3, relief="sunken");
lblSunken.place(width=100,height=50,x=200,y=350);

root.mainloop();