'''
la abstracción consiste en crear código reutilizable de alto nivel
permitiendonos crear funciones con una complejidad propia pero sencillas de usar
ya que aunque no sabemos como funcionan sabemos lo que hacen
''' 

# ejemplo 1 sin abstraccion:
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])


# ejemplo 2 con abstraccion
num = input('How many numbers do you want? ')
print fibs(num)

