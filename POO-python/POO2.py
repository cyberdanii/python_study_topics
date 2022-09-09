from colorama import *
init()
#------------------------------------
# Programacion Orientada a objetos.
	# Contructores: se usa: def __init__(self):
	# Encapsulamiento: se usa: __variable
#----------------------------------
class miPrimeraClase_Carro():
	# propiedades
	def __init__(self): # Este constructor permite establecer un valor por defecto a las variables pero que a la vez pueden ser modificados desde fuera.
		self.marca = "Hyundai"
		self.largo = 200
		self.alto = 120
		self.__puertas = 4 # __ permite que los valores de las variables no sean modificados desde fuera
		self.ruedas = 4
		self.encendido = False

	# Metodos, funciones o comportamiento
	def arrancar(self):# importante colocar siempre self
		self.encendido =  True
		print("Carro Encendido")
	def estado(self):# importante colocar siempre self
		if(self.encendido):
			return (Fore.GREEN+"el carro esta en marcha"+Fore.RESET)
		else:
			return ("el carro NO esta en marcha")

# Instanciar una clase
miCarro = miPrimeraClase_Carro()

print("Marca del Carro ",miCarro.marca)
print("Dimenciones: ",miCarro.largo,", ",miCarro.alto)
print("No. de ruedas: ",miCarro.ruedas)
miCarro.arrancar()
print(miCarro.estado())