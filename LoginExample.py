from  tkinter import *
from  tkinter import  ttk
from tkinter import  messagebox

# Root Bar:

root= Tk()
root.title("Login page")
root.resizable(False,False)

# User Name:

l1 = ttk.Label(text="Username: ")
l1.grid(row=0, column=0)
etUserName= ttk.Entry(root,width=30)
etUserName.grid(row=0, column=1)


# Password:

l2 = ttk.Label(text="Password: ")
l2.grid(row=1, column=0)

etPassword= ttk.Entry(root,width=30)
etPassword.grid(row=1, column=1)
etPassword.config(show="*")

# Login:

Bulogin = ttk.Button(root, text="Login")
Bulogin.grid(row=2, column=1)

def BuClick():
    print("User name: {}, Password: {}".format(etUserName.get(), etPassword.get()))
    if(etUserName.get()=="admin" and etPassword.get()== "1234"):
      messagebox.showinfo(title="Login info", message="Hi Dude!, How are you man")
    else:
      messagebox.showinfo(title = "Login info", message = "User name or password")
Bulogin.config(command=BuClick)

# Run:
root.mainloop()

