import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main
root=Tk()
eq=main.solve()
##for displaying equation on diff window
button1=ttk.Button(root,text="equation")
button1.pack()
def equ():
    messagebox.showinfo("equation",eq)
button1.config(command=equ)


##for displaying solution on diff window
button1=ttk.Button(root,text="solution")
button1.pack()
def sol():
    messagebox.showinfo("solution","x=20,y=30")
button1.config(command=sol)


#for ploting graph with button
button=ttk.Button(root,text="graph")
button.pack()
def callback():
    f= Figure(figsize=(5,5),dpi=100)
    a=f.add_subplot(111)
    a.plot([1,2,3,4,5,6,7,8],[3,4,5,6,7,8,9,10])

    canvas=FigureCanvasTkAgg(f,master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

button.config(command=callback)
root.mainloop()
