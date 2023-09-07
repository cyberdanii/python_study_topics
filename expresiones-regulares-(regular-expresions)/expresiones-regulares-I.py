''' para usar las expresiones regulares debe importarte la libreria 're'
'''
import re
import colorama
tex = 'esto es un texto de prueba que se va a usar para probar las expresiones regularesd e re'
tex_pbra = 'prueba'

# search()
print(re.search(tex_pbra,tex)) 

tex_encontrado = re.search(tex_pbra,tex)

# start(), devuelve la posicion inicial del primer caracter coincidente
print(tex_encontrado.start())
# end(), devuelve la posicion final del ultimo caracter coincidente
print(tex_encontrado.end())
# span(), devuelve una tubla con la posicion del primer y iltimo caracter
print(tex_encontrado.span())
# findall(), devuelve una lista con todas las coincidencias
print(re.findall(tex_pbra,tex))

personas = ["carlos perez",
			"sandra zapata",
			"maria gutierrez",
			"andres zamora",
			"pedro zamora"]

for x in personas:
#	if re.search("^mar", x):
#		print(x)
#		print("-------")
#	if  re.search("ata$", x):
#		print(x)
#		print("-------")
#	if re.search("[a-j]", x):
#		print(x)
#		print("-------")
	if re.search("[za]$", x):
		print(x)
		print("-------")

def example():
	"""
	