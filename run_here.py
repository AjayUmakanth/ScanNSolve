import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
from solve import solve

root=Tk()
root.title("Scan N Solve")
root.minsize(width=600,height=200)
def showimg(path):
    load=Image.open(path)
    render=ImageTk.PhotoImage(load)
    img=Label(root,image=render)
    img.image=render
    img.place(x=125,y=125)

##button for typing and selecting image for input
path=""
path2=StringVar()
path2.set("Result:")
label=Label(root,text="Path:")
label.grid(row=0)
button1=ttk.Button(root,text="Get")
button1.grid(row=0,column=2)

path1=StringVar()
Entry=Entry(root,textvariable=path1)
Entry.grid(row=0,column=1)
def kb():
    path=str(path1.get())
    if(path!=""):
        ans=solve(path)
        path2.set("Result:"+str(ans))
        print(ans)
button1.config(command=kb)

##button for browsing image for input
button=ttk.Button(root,text="Browse")
button.grid(row=1,column=1)
label=Label(root,textvariable=path2)
label.grid(row=2,column=1)
def browse():
    filename=filedialog.askopenfilename()
    path=str(filename)
    ans=solve(path)
    path2.set("Result:"+str(ans))
    print(ans)
button.config(command=browse)
root.mainloop()
