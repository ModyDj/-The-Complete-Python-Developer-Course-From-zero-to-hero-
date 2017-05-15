from  tkinter import *
from  tkinter import  ttk

#entry = ttk.Entry(root, width=80)

#entry.pack()


#def BuClick(id):
    #print("id:{}".format(id))
    #print(entry.get())
    #entry.delete(0,7)
    #entry.insert(9,"loool")

root = Tk()

def key_press(event):
    print("type:{}".format(event.type))
def button_press(event):
    print("Button is pressed")

x = ttk.Button(root,text="Click me")
x.pack()
#ttk.Button(root, text='Click It!', command=lambda:BuClick(10)).pack()
x.bind('<ButtonPress>', button_press)
root.bind("<Control-c>", key_press)

root.mainloop()