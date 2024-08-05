from tkinter import *;

root = Tk();
root.iconbitmap("C:\\Users\\User 2\\Downloads\\lock.ico");
root.title("LOGIN SYSTEM");
root.geometry("480x460+800+280");
root.resizable(False,False);
# * CHANGE BG ROOT
root.config(background="#717d7e");

mainBgDiv = "#d0d3d4";

#? BUILD A MAIN TITLE
title = Label(root, text="LOGIN SYSTEM",font=15, background="#212f3c",fg=mainBgDiv); 
title.pack(fill=X,ipady=5);

#? BUILD A FRAME
div = Frame(root, width=250, height=440, background=mainBgDiv);
div.pack(pady=35);

#? GET A PHOTO AND ADD IT

mainImg = PhotoImage(file= "C:\\Users\\User 2\\Downloads\\access-control.png");
logo = Label(div,image=mainImg, background=mainBgDiv);
logo.place(x=65,y=0);

#? ADD LABELS LOGIN
lblUsername = Label(div, text="USERNAME: ", font=18 , background=mainBgDiv);
lblUsername.place(x=10,y=140);
lblPassword = Label(div, text="PASSWORD: ", font=18 , background=mainBgDiv);
lblPassword.place(x=10,y=180);

#? ADD ENTRIES LOGIN

inputUsername = Entry(div, relief="solid");
inputUsername.place(x=115,y=142);
inputPassword = Entry(div, relief="solid", show="*");
inputPassword.place(x=115,y=182);

#? ADD LABEL FORGOT PASSWORD
lblForgotPassword = Checkbutton(div, text="Forgot password", font=18 , bg=mainBgDiv, activebackground=mainBgDiv);
lblForgotPassword.place(x=10,y=215);

#? CREATING BTN FOR SIGN IN AND SIGN UP

btnSignIn = Button(div,text="Sign In", pady=5, width=30, bg="#bdc3c7", activebackground="#bdc3c7", relief="solid");
btnSignIn.place(x=15,y=250);

btnSignUp = Button(div,text="Sign Up", pady=5, width=30, bg="#cacfd2", activebackground="#cacfd2", relief="solid");
btnSignUp.place(x=15,y=290);

#? CREATING LABEL FOR COPYRIGHT
copyRight = Label(div, text="© Developed by Ayoub Sadouri (2024): " , background=mainBgDiv);
copyRight.place(x=20,y=330);




mainloop();
