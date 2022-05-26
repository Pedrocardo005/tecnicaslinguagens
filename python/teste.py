from tkinter import *
from subprocess import call

root = Tk()
root.geometry('800x800')
frame = Frame(root)
frame.pack(pady=40, padx=40)


def Open():
    call(["python", "app.py"])


btn = Button(frame, text='ÓRBITAS', command=Open)
btn.pack()

root.mainloop()
