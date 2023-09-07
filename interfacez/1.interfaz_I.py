from tkinter import *

ventana = Tk()
ventana.iconbitmap("interfacez/alien.ico") # estable el icono
ventana.title("Nueva Ventana") 
ventana.resizable(True,True) # establece si la ventana sera redimencinable o no
ventana.geometry("600x600")
ventana.config(bg = "darkred")

# Frame 1
miframe = Frame()
	# pack() empaqueta el objeto dentro del Frame o la ventana principal segun se establezca
miframe.pack(expand = True)
	# config() permite poner todas las configuraciones necesarias a un objeto
miframe.config(width = "100", height = "100")
miframe.config(bg = "blue")
miframe.config(relief = "flat", borderwidth = 200) 
	# relief -> establece el tipo de borde

# Frame 2, con campos de datos
miframe_dos= Frame()
miframe_dos.pack(side = "left", anchor = "w")
miframe_dos.config(width = "300", height = "100", bg = "white", padx = 20, pady = 20)
'''
NOTA: es importante tener claro que el width y el height no definen 
el tamaño de un frame si estos estan vacios por dentro.

En realidad los frames son espacios o marcos para separar elementos de otros.

para que se note un frame con color o borde debe colocarse un padding con 'padx o pady' 
como se muestra en la linea anterior a este comentario.
'''
#Label
milabel = Label(miframe_dos, text = "Datos")
milabel.grid(row = 0, column  = 1)

label_nombre = Label(miframe_dos, text = "Nombre: ")
label_nombre.grid(row = 1, column = 0)
cuadro_texto = Entry(miframe_dos)
cuadro_texto.grid(row = 1, column = 1)

label_pass = Label(miframe_dos, text = "Pass: ")
label_pass.grid(row = 2, column = 0, sticky = "w") 
cuadro_texto_pass = Entry(miframe_dos)
cuadro_texto_pass.grid(row = 2, column = 1)

label_comentario = Label(miframe_dos, text = "Comentario: ")
label_comentario.grid(row = 3, column = 0)

text_comentario = Text(miframe_dos, width = 18, height = 10) # Text() permite crear cuadros de textogrande
text_comentario.grid(row = 3, column = 1)

barra_vertical = Scrollbar(miframe_dos, command = text_comentario.yview)
barra_vertical.grid(row = 3, column = 2, sticky = "ns")# n y s alargan el scrollbar al tamaño del textbox

# frame 3
sframe = Frame()
sframe.pack(fill='both')
sframe.config(bg= "red", width = "250", height = "250")

ventana.mainloop()