from tkinter import *;

root = Tk();
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico")
root.title("ScrollBar");
root.geometry("450x400");
root.minsize(width=400,height=350);
root.maxsize(width=500,height=450);

scrollbar = Scrollbar(root);
scrollbar.pack(side=RIGHT, fill=Y);

scrollbar2 = Scrollbar(root, orient=HORIZONTAL);
scrollbar2.pack(side=BOTTOM, fill=X);

mainloop();