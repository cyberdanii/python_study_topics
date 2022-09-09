#---------------------
# Polimorfismo:
#		el polimorfismo permite darle a un objeto una accion mas clara y directa.
#---------------------
from colorama import *
init()
class carro():
	def desplazamiento(self):
		print(Style.DIM+Back.BLUE+"Desaplazamiento en 4 ruedas"+Style.NORMAL+Fore.RESET)
class moto():
	def desplazamiento(self):
		print(Style.DIM+Back.RED+"Desplazamiento en 2 ruedas"+Style.NORMAL+Fore.RESET)
class camion():
	def desplazamiento(self):
		print(Style.DIM+Back.GREEN+"Desplazamiento en 6 ruedas"+Style.NORMAL+Fore.RESET)

def activar_desplazamiento(vehiculo): # 1. se define primero la funcion
	vehiculo.desplazamiento()

vehiculo_uno = carro()# 2. se define el objeto
vehiculo_tres = moto()
vehiculo_dos = camion()

activar_desplazamiento(vehiculo_uno) # 3. se imprime el objeto con la funcion
activar_desplazamiento(vehiculo_dos)
activar_desplazamiento(vehiculo_tres)