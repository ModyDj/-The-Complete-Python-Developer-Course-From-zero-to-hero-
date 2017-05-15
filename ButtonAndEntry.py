
from  tkinter import  *
from  tkinter import  ttk


root = Tk()
style= ttk.Style()
style.configure('TButton', background='#00FF0', font=('Arial', 18))
entry = ttk.Entry(root, width=100)
entry.pack()
button = ttk.Button(root, text="Click Me!")
button.pack()
logo = PhotoImage(file="contents_motif.gif")
button.config(image=logo, compound=RIGHT, width=75)
#Resize_logo = logo.subsample(100,100)
#button.config(image=Resize_logo)
def BuClick():
    print(entry.get())
    entry.delete(0,END)
    #entry.delete(0, 3)
    #entry.insert(0, "button clicked")


button.config(command = BuClick)
root.mainloop()