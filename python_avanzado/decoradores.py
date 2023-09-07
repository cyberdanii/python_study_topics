def mayusculas(func): # func, es el closure
    
    # nested function
    def envoltura(texto): 
        return func(texto.upper())
    return envoltura

@mayusculas
# mensaje = mayusculas(mensaje) # esto es lo que sucede detras del decorador
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('cesar'))