from tkinter import *  #this is a library used to create GUIs 
from tkinter.ttk import * # the ttk package is used to style the widget's property, its look and feel

from time import strftime 
# from datetime import *

root = Tk()
root.title("Date and Time")

def time():
    string_time = strftime('%H:%M:%S %p \n %A, %B %d, %Y')
    label1.config(text=string_time)
    label1.after(1000, time)


label1 = Label(root, font =("ds-digital", 50), background ="black", foreground ="cyan")
label1.pack(anchor = 'center')

time()
mainloop()

