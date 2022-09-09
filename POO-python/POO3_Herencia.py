from colorama import *
init()
class vehiculo():
	def __init__(self):
			self.marca = "-"
			self.ruedas = 0
			self.color = "-"
			self.alto = 0.00
			self.largo = 0.00

			self.enciende = False
			self.acelera = False
			self.frena = False

	def encender(self):# importante colocar siempre self 
		self.enciende = True
		print(Style.DIM+Back.YELLOW+Fore.RED+self.marca,
		 Back.GREEN+Fore.WHITE+" Encendido"+Back.RESET+Fore.RESET+Style.NORMAL)
	def acelerar(self):# importante colocar siempre self
		self.acelera = True
		print(Style.DIM+Back.YELLOW+Fore.RED+self.marca,
			Back.GREEN+Fore.WHITE+" Acelerando"+Back.RESET+Fore.RESET+Style.NORMAL)
	def frenar(self):# importante colocar siempre self
		self.frena = True
		print(Style.DIM+Back.YELLOW+Fore.RED+self.marca,
			Back.GREEN+Fore.WHITE+" Frenando"+Back.RESET+Fore.RESET+Style.NORMAL)

class hyundai(vehiculo):
	def __init__(self):
		self.marca = " Hyundai" # cambiando el valor por defecto heredado de la otra clase

#objeto con clase padre unicamente
vehiculo_uno = vehiculo()

print(vehiculo_uno.encender())
print(vehiculo_uno.acelerar())
print(vehiculo_uno.frenar())

# Nuevo objeto con clase heredada
vehiculo_dos  = hyundai()

print(vehiculo_dos.marca)
print(vehiculo_dos.encender())
print(vehiculo_dos.acelerar())
print(vehiculo_dos.frenar())