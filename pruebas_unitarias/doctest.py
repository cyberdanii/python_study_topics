
def area_triangulo(base, altura):
    """
    Calcula el area de un triangulo dado.

    >>> area_triangulo(3, 6)
    9.0

    """

    return (base * altura) / 2

# print(area_triangulo(2, 4))

import doctest
doctest.testmod()
