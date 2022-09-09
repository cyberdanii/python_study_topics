class perro:
	def sonido(self):
		print('guauuu!!!')
class gato:
	def sonido(self):
		print('miauuu!!!')
class vaca:
	def sonido(self):
		print('muuu!!!')

def todos_a_cantar(animales):
	for animal in animales:
		animal.sonido()

p = perro()
g = gato()
v = vaca()

animales = [p, g, v]

todos_a_cantar(animales)