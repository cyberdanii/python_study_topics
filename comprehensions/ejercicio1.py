# Comprehensions ayudan a optimizar los programas.

# list
# [elemento for elemento in elementos if elemento_tiene_condicion]
# dictionary
# {key:elemento for elemento in elementos if elemento_tiene_condicion}

# set ot tuple
# {elemento for elemento in elementos if elemento_tiene_condicion}

# LISTAS
numeros = list(range(1,101))
# print(numeros)
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100

# DICCIONARIOS
students_id = (12,13,14,15)
students_names = ('Jesus','Mateo','Juan','Pedro')
students_obj = {std_id: std_name for std_id, std_name in zip(students_id, students_names) }
print(students_obj)
# {12: 'Jesus', 13: 'Mateo', 14: 'Juan', 15: 'Pedro'}

# SETs 
# Los Sets son conjuntos de datos que no se repiten.
# los Set son mutables como las listas
a = {1,2,34,5,33,33,1} # utomaticamente se quitaran los duplicados
#   {1, 2, 34, 33, 5}
print(type(a)), print(a)

import random
rand_numbers = list()

for i in range(11):
    rand_numbers.append(random.randint(1,3))
print(rand_numbers)
non_repeated = {number for number in rand_numbers}
print(non_repeated) # se imprime el set datos repetidos

# TUPLAS
tupla = (1,2,3,5,6,7,8,9,0)
tupla_pares = tuple([ n for n in tupla if n % 2 == 0])
print(tupla_pares)

'''

v3g3t42901@

'''