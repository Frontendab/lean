from tkinter import *;
from tkinter.messagebox import *;

root = Tk();
root.title("Sign in");
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
# root.geometry(f"{width}x{height}");
root.geometry("800x550");
root.iconbitmap("C:\\Users\\User 2\\Downloads\\medium.ico");

#? ======== start color bg =========
colorBg = "#dfdfdf";
#? ======== end color bg =========
root.config(background=colorBg);

titlePage = Label(root, text="Login", font=("ariabl", 18),background=colorBg);
titlePage.place(x=350,y=15);

#? Creating input to login
#* Creating a function for login 
def LoginNow():
    username = inputUsername.get();
    password = inputPassword.get();
    if username and password:
        if username == "admin" and password == "pass123":
            showinfo(title="Login", message="Login is succesfully ✅");
            root.destroy();
            home = Tk();
            home.title("Home");
            # home.geometry(f"{width}x{height}");
            home.geometry("800x550");
            home.config(background=colorBg);
            lbl = Label(home, text=f"Welcome {username} in your an account ✅", font=("ariabl", 18));
            lbl.place(x=200, y=30);
            #? Creating a menu bar
            menuBar = Menu(home);
            
            main = Menu(menuBar, tearoff=0);
            menuBar.add_cascade(label="Main", menu=main);
            
            #? build a function to exit 
            def ExitNow(): 
                answer = askyesno(title="Exit", message="Are u sure u want to Exit?");
                if answer: home.quit();
            main.add_command(label="Exit", command=ExitNow);

            home.config(menu= menuBar);

        else: showerror(title="Login",message="Please Enter your correct a username and password to login successfull!");
    else: showerror(title="Login",message="Please Enter your username and password to login!");

labelInputUsername = Label(root,text="Username", background=colorBg, font=("ariabl", 17));
labelInputUsername.place(x=220,y=90);

inputUsername = Entry(root,background="#fff", font=("ariabl", 17), relief="solid",highlightbackground="#ccc");
inputUsername.place(width=200,x=350,y=90);
inputUsername.insert(0,"admin");

labelInputPassword = Label(root,text="Password", background=colorBg, font=("ariabl", 17));
labelInputPassword.place(x=230,y=150);

inputPassword = Entry(root,background="#fff", font=("ariabl", 17), relief="solid",highlightbackground="#ccc", show="*");
inputPassword.place(width=200,x=350,y=150);
inputPassword.insert(0,"pass123");

SubmitBtn = Button(root,text="Login",background="#fff", font=("ariabl", 13), relief="solid",highlightbackground="#ccc", command=LoginNow);
SubmitBtn.place(width=150,x=340,y=220);


mainloop();