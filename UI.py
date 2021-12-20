import tkinter as tk
from tkinter.ttk import *
LISTS=[]
def Solve():
    #function yara &mariam
    
    number=int(t.index('end').split('.')[0])-1
    print(int(t.index('end').split('.')[0])-1)
    LISTS=t.get(0.0, 'end-1c').split("\n") #That's the line you need
    
    print(LISTS)
    print("3nd yara")
def iterations():
    
        tk.Label(window, text="Enter Number of iterations").grid(column=1,row=8)
        no=tk.Entry(window ,width=10).grid(column=2,row=8)
        print(no.get())
def relError():
    
        tk.Label(window, text="Enter Absolute relative error").grid(column=1,row=9)
        er=tk.Entry(window ,width=10).grid(column=2,row=9)
        
def call():
    method=dropdown.get()
    if(method=="Gauss Jordan"):
        Gauss_Jordan()
    elif(method=="Jacobi"):
        tk.Label(window, text="Enter initial guess").grid(column=1,row=5)
        ini=tk.Entry(window ,width=10)
        ini.grid(column=2,row=5)
        print(ini.get())
        rad1 = Radiobutton(window,text='Number of iterations', value=1, command=iterations)
        rad2 = Radiobutton(window,text='Relative error', value=2,command=relError)
        rad1.grid(column=2, row=6)
        rad2.grid(column=2, row=7) 
    elif(method=="Gauss Elimination"):
        gauss_pivot()
    elif(method=="Gauss Seidel"):
        tk.Label(window, text="Enter initial guess").grid(column=1,row=5)
        ini=tk.Entry(window ,width=10)
        ini.grid(column=2,row=5)
        print(ini.get())
        rad1 = Radiobutton(window,text='Number of iterations', value=1, command=iterations)
        rad2 = Radiobutton(window,text='Relative error', value=2,command=relError)
        rad1.grid(column=2, row=6) 
        rad2.grid(column=2, row=7) 
    elif(method=="LU decomposition"):
        tk.Label(window, text="Choose the form you want").grid(column=1,row=5)
        dropdownLU=Combobox(window)
        dropdownLU['values']=("Downlittle Form ", "Crout Form", "Cholesky Form ")
        dropdownLU.grid(column=2,row=5)
        form=dropdownLU.get()
#creating window 
window = tk.Tk()
window.geometry('2400x700')

window.title("Linear equations methods")
lbl = tk.Label(window, text="Solving System of Linear Equations",  font=("Times New Roman Bold", 35),fg="blue")
lbl.grid(column=0, row=0)
#lbl.pack()


tk.Label(window, text="Enter your equations" , font=("Arial Bold", 20)).grid(column=0,row=1)
t = tk.Text(window, width=30, height=10 ,yscrollcommand=set() ,bd=9 ,font=("Arial Bold", 18 ))
t.focus()
t.grid(column=1,row=1)
end=tk.Button(window,text="Solve",font=("Arial Bold", 15 ),bg="white",fg="blue", width=15 ,command=Solve)
end.grid(column=2,row=2,pady=(2,2))
choose = tk.Label(window, text="Choose the number of significant figures",  font=("Arial Bold", 20))
choose.grid(column=0,row=6)
significantDown=Combobox(window)
significantDown['values']=("1","2","3","4","5")
significantDown.grid(column=1,row=6)
meth = tk.Label(window, text="Choose method to solve your equations",  font=("Arial Bold", 20))
meth.grid(column=0,row=4)
dropdown=Combobox(window)
dropdown['values']=("Gauss Elimination", "Gauss Jordan", "Gauss Seidel", "LU decomposition", "Jacobi")
dropdown.grid(column=1,row=4)
btn = tk.Button(window, text="Submit", font=("Arial Bold", 15 ),bg="white" ,fg="red", width=12 ,command=call)
btn.grid(column=2, row=4)

window.mainloop()
