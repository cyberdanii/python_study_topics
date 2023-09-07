import unittest

def calculador_mayoria_edad(edad):

    if edad < 18:
        return False
    else:
        return True

class test_caja_cristal(unittest.TestCase):
    
    def es_mayor(self):
        edad = 25

        resultado = calculador_mayoria_edad(edad)
        self.assertEqual(resultado, True)

    def es_menor(self):
        edad = 15

        resultado = calculador_mayoria_edad(edad)
        self.assertEqual(resultado, False)

if __name__=='__main__':

    unittest.main()