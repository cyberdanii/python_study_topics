# importing tkinter module
from tkinter import *
  
# creating Tk() variable
# required by Tkinter classes
master = Tk()
  
# Tkinter variables
# initialization using constructor
intvar = IntVar(master, value = 25, name ="2")
strvar = StringVar(master, "Hello !")
boolvar = BooleanVar(master, True)
doublevar = DoubleVar(master, 10.25)