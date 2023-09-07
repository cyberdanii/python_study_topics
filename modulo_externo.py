# Modulo Externo para importar en otro modulo o archivo.

class persona():
	def __init__(self, nombre, apellido):
		self.nombre =  nombre
		self.apellido = apellido

	def datos_personales(self):
		print("Mis datos personales son: ",
			self.nombre, " ", self.apellido)