# Creacion de archivos externos
# para manejar archivos se debe importar el modulo IO
from io import open

def crearNuevoArchivo():
	arch = open("arch.txt","w") # w Crea el archivo si no existe y tambien lo sobreescribe.
	contenido = "Este es un archivo creado desde un codigo python"
	arch.write(contenido)
	arch.close()
def leerArchivo():
	arch = open("arch.txt","r")# r lee el archivo si existe sino muestra error.
	contenido = arch.read()
	arch.close()
def agregarDatosArchivo():
	arch = open("arch.txt","a")# a agreaga datos al final del archivo
	contenido = "Esta es otra linea de codigo agregada desde el codigo"
	arch.write(contenido)
	arch.close()
def lectura_y_escritura_Archivo():
	arch = open("arch.txt","r+")# r+ permite que el archivo se pueda leer y escribir.
	arch.close()
