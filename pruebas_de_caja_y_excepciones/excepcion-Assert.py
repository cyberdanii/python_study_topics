def primera_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        '''
            assert: valida excepciones.
                    si la condicion es falsa 
                    imprimira el valor o el contenido despues de la coma,
                    si es True seguira con el flujo del programa.
        '''
        assert type(palabra) == str, f'{palabra} no es string'
        assert len(palabra) > 0, 'No se permiten strigs vacios'

        primeras_letras.append(palabra)

    print(primeras_letras)
    return primeras_letras

l = ['hola','k','mundo']
primera_letra(l)