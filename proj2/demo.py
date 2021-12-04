from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

master = tk.Tk()

tk.Label(master, text='From Roll No : ', font=20).grid(row=0,column=0,pady=10,padx=5)
tk.Label(master, text='to Roll No : ', font=20).grid(row=1,column=0,pady=10,padx=5)

e3 = tk.Entry(master)
e4 = tk.Entry(master)

e3.grid(row=0,column=1,pady=10,padx=5)
e4.grid(row=1,column=1,pady=10,padx=5)

def reset():
    var= StringVar(master)
    var.set('')
    e3.config(textvariable=var)

def reset1():
    var= StringVar(master)
    var.set('')
    e4.config(textvariable=var)

my_button = tk.Button(master, text='reset', command=reset, font=20)
my_button.grid(row=0,column=2,pady=10,padx=5)

my_button = tk.Button(master, text='reset', command=reset1, font=20)
my_button.grid(row=1,column=2,pady=10,padx=5)

def submit():
    
    var= StringVar(master)
    var.set('')
    e4.config(textvariable=var)

my_button = tk.Button(master, text='Generate  All', command=reset, font=20)
my_button.grid(row=2,column=0,pady=10,padx=5)

master.mainloop()