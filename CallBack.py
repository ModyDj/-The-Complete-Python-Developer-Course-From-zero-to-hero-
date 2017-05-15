from  tkinter import *
from  tkinter import ttk

def BuClick(id):
    #print("Button is clicked")
    print("Id: {}".format(id))


root = Tk()

#bu = ttk.Button(root, text="Click me 1", command = BuClick(10)).pack()
ttk.Button(root, text="Click me 1", command = lambda :BuClick(10)).pack()
#bu.pack()

root.mainloop()