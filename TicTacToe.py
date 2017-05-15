from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from random import randint
# Global variables
ActivePlayer=1
p1=[] # What player one selected
p2=[] # What Player two selected
root = Tk()
root.title("Tic Tac Toy: Player 1")
style=ttk.Style()
style.theme_use('classic')
# Add Buttons:

button1= ttk.Button(root, text=' ')
button1.grid(row=0, column=0, sticky='snew',ipadx=40,ipady=40)
button1.config(command=lambda :BuClick(1))

button2= ttk.Button(root, text=' ')
button2.grid(row=0, column=1, sticky='snew',ipadx=40,ipady=40)
button2.config(command=lambda :BuClick(2))

button3= ttk.Button(root, text=' ')
button3.grid(row=0, column=2, sticky='snew',ipadx=40,ipady=40)
button3.config(command=lambda :BuClick(3))

button4= ttk.Button(root, text=' ')
button4.grid(row=1, column=0, sticky='snew',ipadx=40,ipady=40)
button4.config(command=lambda :BuClick(4))

button5= ttk.Button(root, text=' ')
button5.grid(row=1, column=1, sticky='snew',ipadx=40,ipady=40)
button5.config(command=lambda :BuClick(5))

button6= ttk.Button(root, text=' ')
button6.grid(row=1, column=2, sticky='snew',ipadx=40,ipady=40)
button6.config(command=lambda :BuClick(6))

button7= ttk.Button(root, text=' ')
button7.grid(row=2, column=0, sticky='snew',ipadx=40,ipady=40)
button7.config(command=lambda :BuClick(7))

button8= ttk.Button(root, text=' ')
button8.grid(row=2, column=1, sticky='snew',ipadx=40,ipady=40)
button8.config(command=lambda :BuClick(8))

button9= ttk.Button(root, text=' ')
button9.grid(row=2, column=2, sticky='snew',ipadx=40,ipady=40)
button9.config(command=lambda :BuClick(9))




def BuClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        root.title("Tic Tac Toe: Player1")
        print("P1:{}".format(p1))
        ActivePlayer = 2
        AutoPlay()
    elif (ActivePlayer == 2):
        SetLayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toe: Player2")
        print("P2:{}".format(p2))
        ActivePlayer = 1

    CheckWinner()

def SetLayout(id,PlayerSymbol):
    if id==1:
        button1.config(text=PlayerSymbol)
        button1.state(['disabled'])

    elif id==2:
        button2.config(text=PlayerSymbol)
        button2.state(['disabled'])

    elif id==3:
        button3.config(text=PlayerSymbol)
        button3.state(['disabled'])

    elif id==4:
        button4.config(text=PlayerSymbol)
        button4.state(['disabled'])

    elif id==5:
        button5.config(text=PlayerSymbol)
        button5.state(['disabled'])

    elif id==6:
        button6.config(text=PlayerSymbol)
        button6.state(['disabled'])

    elif id==7:
        button7.config(text=PlayerSymbol)
        button7.state(['disabled'])

    elif id==8:
        button8.config(text=PlayerSymbol)
        button8.state(['disabled'])

    elif id==9:
        button9.config(text=PlayerSymbol)
        button9.state(['disabled'])

def CheckWinner():
    Winner = -1

    # Winner As a row:

    if ((1 in p1) and (2 in p1) and (3 in p1)):
        Winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winner=2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
       Winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
       Winner = 2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
       Winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
       Winner = 2

    # Winner As a column:

    if ((1 in p1) and (4 in p1) and (7 in p1)):
       Winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
       Winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
       Winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
       Winner = 2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
       Winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
       Winner = 2

    # Winner As a first Italic line :

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winner = 2

    # Winner As a Second Italic line :

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winner = 2




    if Winner==1:
        messagebox.showinfo(title="Congratulations",message="Player1 is the winner :)")
    elif Winner==2:
        messagebox.showinfo(title="Congratulations",message="Player2 is the winner :)")

def AutoPlay():
    EmptyCells=[]
    for cell in range(9):
        if (not((cell+1 in p1) or (cell+2 in p2))):
            EmptyCells.append(cell+1)
    RandIndex=randint(0,len(EmptyCells)-1)
    BuClick(EmptyCells[RandIndex])

root.mainloop()