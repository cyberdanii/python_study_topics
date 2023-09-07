from colorama import *
init()

# Programacion Orientada a objetos.
class miPrimeraClase_Carro():
	# propiedades
	marca = "Hyundai"
	largo = 200
	alto = 120
	ruedas = 4
	encendido = False
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

miCarro.arrancar()
print(miCarro.estado())

# NOTA: las funciones no deben llevar el mismo nombre que las variables y viceversa
