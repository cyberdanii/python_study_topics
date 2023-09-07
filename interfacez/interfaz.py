import tkinter
def mostrar_texto():
	texto = textbox.get()
	etiqueta2["text"] = texto
ventana = tkinter.Tk()
ventana.title("Ejercicio con Interfaz python-Tkinter") # coloca el titulo a la ventana
#ventana.geometry("200x200") # establece tamaño de la ventana

# Label
etiqueta = tkinter.Label(ventana, text = "Hola Jack",fg="white",font=("Arial",20), bg = "black")
etiqueta.pack(fill = tkinter.BOTH,expand=False)

# TextBox
textbox = tkinter.Entry(ventana, bg= "grey",fg= "darkred") # entry - muestra un textbox para introducir datos
textbox.pack(fill = tkinter.BOTH,expand=False) # fill - llena toda el area del elemento con el color de fondo

# Label
etiqueta2 = tkinter.Label(ventana, bg= "black",fg= "white", font=("Helvetica", 30))
etiqueta2.pack(fill = tkinter.BOTH,expand=False)

# Boton 
boton = tkinter.Button(ventana, text = "Mostrar", fg = "white", bg= "black", command = mostrar_texto, width=10, height = 5)
boton.pack(fill = tkinter.BOTH,expand=False)

# Label
mensaje1 = tkinter.Label(ventana, text="Esto ", width = 10, height= 5, bg = "blue", fg = "yellow")
mensaje1.pack()

# Label
mensaje2 = tkinter.Label(ventana, text="Es ", width = 10, height= 5, bg = "darkred", fg = "white")
mensaje2.pack(side = tkinter.LEFT)

# Label
mensaje3 = tkinter.Label(ventana, text="Una ", width = 10, height= 5, bg = "green", fg = "grey")
mensaje3.pack( side = tkinter.RIGHT)

# Label
mensaje4 = tkinter.Label(ventana, text="Interfaz", width = 10, height= 5, bg = "cyan", fg = "blue")

ventana.mainloop() # ejecuta el programa