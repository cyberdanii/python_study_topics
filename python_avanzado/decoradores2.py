from datetime import datetime

def tiempo_ejecucion(func):
    def envoltura(
        *args, # son parametros simples, ejemplo: 'a', 4, True, {'uno':1}
        **kwargs # son parametros predefinidos, ejemplo: nombre='carlos', estado = False 
        ):

        inicio_tiempo = datetime.now()
        func(*args, **kwargs)
        final_tiempo = datetime.now()

        total_tiempo = final_tiempo - inicio_tiempo
        print('pasaron '+str(total_tiempo)+' segundos')

    return envoltura

@tiempo_ejecucion
def ramdom_time():
    for _ in range(1,10000):
        pass

@tiempo_ejecucion
def suma(a: int, b: int) -> int:
    return a + b

@tiempo_ejecucion
def saludar(nombre = 'Daniel'):
    print('Hola' + nombre)

suma(5, 1)
saludar()
ramdom_time()