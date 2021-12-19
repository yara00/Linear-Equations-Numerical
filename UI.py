import tkinter as tk
from tkinter.ttk import *
def iterations():
    tk.Label(window, text="Enter Number of iterations").grid(column=2, row=7)
    no = tk.Entry(window, width=10).grid(column=3, row=7)
    print(no.get())


def relError():
    tk.Label(window, text="Enter Absolute relative error").grid(column=2, row=7)
    er = tk.Entry(window, width=10).grid(column=3, row=7)


def call():
    method = dropdown.get()
    if (method == "Gauss Jordan"):
        print("tmam")
       # Gauss_Jordan()
    elif (method == "Jacobi"):
        tk.Label(window, text="Enter initial guess").grid(column=2, row=4)
        ini = tk.Entry(window, width=10)
        ini.grid(column=3, row=4)
        print(ini.get())
        rad1 = Radiobutton(window, text='Number of iterations', value=1, command=iterations)
        rad2 = Radiobutton(window, text='Relative error', value=2, command=relError)
        rad1.grid(column=3, row=5)
        rad2.grid(column=3, row=6)
# creating window
window = tk.Tk()
window.geometry('2400x700')
window.title("Linear equations methods")
lbl = tk.Label(window, text="Solving System of Linear Equations", font=("Times New Roman Bold", 35), fg="blue")
lbl.grid(column=0, row=0)
# lbl.pack()


tk.Label(window, text="Enter your equations", font=("Arial Bold", 20)).grid(column=0, row=2)
equations = tk.Entry(window, width=20)
equations.grid(column=1, row=2)

meth = tk.Label(window, text="Choose method to solve your equations", font=("Arial Bold", 20))
meth.grid(column=0, row=3)
dropdown = Combobox(window)
dropdown['values'] = ("Gauss Elimination", "Gauss Jordan", "Gauss Seidel", "LU decomposition", "Jacobi")
dropdown.grid(column=1, row=3)
btn = tk.Button(window, text="Submit", font=("Arial Bold", 15), bg="white", fg="red", width=12, command=call)
btn.grid(column=2, row=3)

window.mainloop()


