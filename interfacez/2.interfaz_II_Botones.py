from tkinter import *

# EJercicio con botones y funciones en botones
win = Tk()

label_a = Label(win,text = "Nombre: ")
label_a.grid(row = 0, column = 0)

varNombre = StringVar() # variable que se va mandar al label

input_nombre = Entry(win, textvariable = varNombre)
'''							|
						comando para colocar variable en el label
'''
input_nombre.grid(row = 0, column = 1)

def funcion_enviar():
	varNombre.set("jack")
boton_enviar = Button(win, text = "enviar", command = funcion_enviar)

boton_enviar.grid(row = 1, column = 0)

win.mainloop()