from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Ini Fernando").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=5)
root.mainloop()