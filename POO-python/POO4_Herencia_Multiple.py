# Herencia Compleja
from colorama import *

init()

def backR():
	return Back.BLUE

class persona:
	def __init__(self, nombre, edad, ciudad):
		self.nombre = nombre
		self.edad = edad
		self.ciudad = ciudad

	def descripcion(self): # importante colocar siempre self
		
		print("\n"+Style.DIM+backR()+"Datos del Usuario "+Style.NORMAL+Back.RESET)
		
		print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nCiudad: {self.ciudad}" )

class casa:
	def __init__(self, ubicacion = 'calle 60 # 45A - 54', color = 'amarillo', estrato = 4, numero_habitaciones = 3 ):
		self.ubicacion = ubicacion
		self.color = color
		self.estrato = estrato
		self.numero_habitaciones = numero_habitaciones
	
	def descripcion_casa(self):
		
		return self.ubicacion

class empleado(persona, casa): # tambien se pueden agregar mas clases, ejemplo: empleado(persona, casa, auto)
	
	def __init__(self,nombre_emple, edad_emple, ciudad_emple, salario, empresa):

		persona.__init__(self, nombre_emple, edad_emple, ciudad_emple)# importante usar super(), vea la NOTA al final
		casa.__init__(self)

		self.salario = salario
		self.empresa = empresa

	def descripcion(self): # importante colocar siempre self
		persona.descripcion(self)
		print( f"Salario: { self.salario } \nEmpresa: { self.empresa } \nDireccion: { casa.descripcion_casa(self) } " )

# Empleado
empleado_uno = empleado("Gerardo","40","Madrid","12345667","NCR")
empleado_uno.descripcion()


# NOTA: La funcion super(). sirve para llamar funciones de la clase padre dentro de la clase hija 
#		y juntarlas con funciones de la clase hija.
#		porque de no usarse no funcioncionarian las uniones de funciones de dos clases diferentes.
#		Tambien sirve para llamar funciones de clases secundarias dentro de una herencia multiple.

#VALIDAD si un objeto es la instancia de una clase especifica
print('\nEs Instancia?')
print(isinstance(empleado_uno, persona))
print(isinstance(empleado_uno, empleado))
