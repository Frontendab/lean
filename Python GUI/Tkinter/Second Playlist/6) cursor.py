from tkinter import *;

root = Tk();
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");
root.title("Cursors");
root.geometry("400x400");

#? Build a deffrenet btn with deffrenet cursor
btn1 = Button(root, text="circle", cursor="circle");
btn1.pack();

btn2 = Button(root, text="heart", cursor="heart");
btn2.pack();

btn3 = Button(root, text="spider", cursor="spider");
btn3.pack();

btn4 = Button(root, text="plus", cursor="plus");
btn4.pack();

btn5 = Button(root, text="target", cursor="target");
btn5.pack();

btn6 = Button(root, text="cross", cursor="cross");
btn6.pack();

btn7 = Button(root, text="clock", cursor="clock");
btn7.pack();

btn8 = Button(root, text="sizing", cursor="sizing");
btn8.pack();

btn9 = Button(root, text="trek", cursor="trek");
btn9.pack();

btn10 = Button(root, text="mouse", cursor="mouse");
btn10.pack();

btn11 = Button(root, text="clock", cursor="clock");
btn11.pack();

btn12 = Button(root, text="man", cursor="man");
btn12.pack();

btn13 = Button(root, text="hand1", cursor="hand1");
btn13.pack();

btn14 = Button(root, text="hand2", cursor="hand2");
btn14.pack();


mainloop();