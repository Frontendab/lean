from tkinter import *;

root = Tk();
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");
root.title("Button with Image");
root.geometry("600x600");
root.maxsize(width=600,height=600);
root.minsize(width=400,height=350);
# root.resizable(False,False);

photo = PhotoImage(file="C:\\Users\\User 2\\Desktop\\myLogo.png");
res = photo.subsample(5,5);

btn = Button(root,text="My logo", image=res, compound="top", relief="solid");
btn.place(x=240,y=20);

mainloop();