from tkinter import *


def sel():
   selection = "You selected option " + str(var.get())
   label.config(text = selection)

root = Tk(className=' EENG5780 - Radio Buttons Example')
root.geometry("400x300")
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value=1,command=sel,font=("Arial", 25))
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2,command=sel,font=("Arial", 25))
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Option 3", variable=var, value=3,command=sel,font=("Arial", 25))
R3.pack( anchor = W)

label = Label(root, font=("Arial", 25))
label.pack(anchor = S)
root.mainloop()

