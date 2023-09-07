''' Ejercicio con Funciones propias. '''
from colorama import Fore,Back, Style, init
init()
print(Style.BRIGHT)
# 1. funcion con Return.
def persona(nombre, apellido):
	full_nombre = Fore.YELLOW+nombre + " "+apellido+Fore.RESET
	return full_nombre
print(persona("jack","walker"))

# 2. funcion con parametros opcionales:
def datoPersona(nombre,nombre2="",apellido="",edad=20): # importante colocar valores por defeco a los parametros opcionales, de lo contrario no funcionara.
	if nombre and nombre2 and apellido and edad:
        full = nombre+" "+nombre2+" "+apellido+str(edad)
        return full
    elif nombre and nombre2 and apellido:
		full = nombre + " "+nombre2+" "+apellido
		return full
	elif nombre and apellido:
		full =  nombre +" "+apellido
		return full
	elif nombre and nombre2:
		full = nombre +" "+nombre2
		return full
	elif nombre:
		return nombre

	else:
		print("no has introducido algo.")

print(datoPersona(Fore.RED +"daniel",))
print(datoPersona(Fore.MAGENTA +"daniel","felipe"))
print(datoPersona(Fore.CYAN +"daniel","felipe","ibarra"))
print(datoPersona(Fore.GREEN +"daniel","felipe","ibarra",edad))

# 3. funcion con dos valores, pero que acepta un sin fin de otros valores.
def gente(nombre, apellido, **otros_datos):
# el tercer parametro en ** permite ingresar datos adicionales como se muestra al final.
	dic = {}
	dic["nombre"]=nombre
	dic["apellido"]=apellido
	for k, v in otros_datos.items():
		dic[k]=v
	return dic
datos = gente("carlos","mejia",ciudad="cartagena",edad="30")
print(datos)

def personas(*jovenes)
    # forma singular
    print("El joven es: "+jovenes[1])
    
    # forma multiple
    for n,joven in enumerate(jovenes):
        print(f'El joven {str(n)} es: {joven}')

personas('carlos','maria','jose')    


        
