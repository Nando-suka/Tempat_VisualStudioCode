from tkinter import *
from tkinter import ttk

tes = "Var1"
tes2 = "Var2"
tes3 = "Var3"
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Ini Fernando").grid(column=0, row=0)
ttk.Label(frm, text="Ini Fernando kedua").grid(column=10, row=0)
ttk.Entry(frm).grid(column=4, row=6)
ttk.Entry(frm).grid(columnspan=90, row=15)
ttk.
ttk.Button(frm, text="Submit").grid(column=4, row=7)
ttk.Checkbutton(frm).grid(column=4, row=30,)
ttk.Menubutton(frm, text="Ini Percobaan")
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=5)
root.mainloop()