from tkinter import *

from tkinter import simpledialog

def Clickme():
    s = simpledialog.askinteger("Input string Box","Plese Enter your Name")
    print(type(s))


bob=Tk()


b=Button(bob,text="Message Box",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()