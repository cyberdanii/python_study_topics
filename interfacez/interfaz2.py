import tkinter

ven = tkinter.Tk()
ven.title("prueba con grid")
def changeColor():
	color = ""
# NOTA: cuando se use .apck() no se puede usar .grid() ya que marcara error
mensaje = tkinter.Label(ven, text = "mensaje").grid(row = 0, column = 0)
boton = tkinter.Button(ven, text = "Boton 1", fg = "white",bg = "black").grid(row = 0,column = 1)

mensaje = tkinter.Label(ven, text = "mensaje").grid(row = 1, column = 1)
boton = tkinter.Button(ven, text = "Boton 2", bg = "green").grid(row = 1,column = 0)

mensaje = tkinter.Label(ven, text = "mensaje").grid(row = 2, column = 0)
boton = tkinter.Button(ven, text = "Boton 3", bg = "red").grid(row = 2,column = 1)

mensaje = tkinter.Label(ven, text = "mensaje").grid(row = 3, column = 1)
boton = tkinter.Button(ven, text = "Boton 4", bg = "magenta").grid(row = 3,column = 0)

ven.mainloop()