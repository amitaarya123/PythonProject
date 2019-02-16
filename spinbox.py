
from tkinter import *


def Clickme():
    print(spin1.get())


bob=Tk()


frame= LabelFrame(bob,text="Label frame",pady=15)
spin1 = Spinbox(frame,from_=1, to =12)
spin1.pack()
b=Button(frame,text="Spin Box",command=Clickme)
b.pack()
frame.pack()
bob.geometry("300x200+300+200")
bob.mainloop()