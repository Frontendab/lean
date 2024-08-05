from tkinter import *;

root = Tk();
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");
root.title("Bitmap");
root.geometry("400x400");

#? Build a deffrenet btn with deffrenet bitmap
btn1 = Button(root, text="error", bitmap="error", fg="red");
btn1.pack();

btn2 = Button(root, text="hourglass", bitmap="hourglass");
btn2.pack();

btn3 = Button(root, text="info", bitmap="info", fg="blue");
btn3.pack();

btn4 = Button(root, text="warning", bitmap="warning", fg="yellow");
btn4.pack();

btn5 = Button(root, text="question", bitmap="question");
btn5.pack();

btn6 = Button(root, text="gray12", bitmap="gray12");
btn6.pack();

btn7 = Button(root, text="gray25", bitmap="gray25");
btn7.pack();

btn8 = Button(root, text="gray50", bitmap="gray50");
btn8.pack();

mainloop();