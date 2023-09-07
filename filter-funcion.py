''' 
Filter()
    La funcion filter() recive dos argumentos, filter(funcionFiltro,elementosParaFiltrar)
    La funcion filter devuelven una lista
    la funcion filter funciona como un filtro condicional
'''
# ejemplo basico

def pares(num):
    if num % 2==0:
        return True
numeros = [20,10,545,756,332,123,54,432,45]
print(list(filter(pares,numeros)))
#-------------------------------------------------------------
# ejemplo con objetos
class empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return '{} trabaja como {} y gana un sueldo de {}'.format(self.nombre,self.cargo,self.salario)

lista = [
    empleado('jack','director',1234511),
    empleado('jose','administrador',123459),
    empleado('maria','abogada',123457),
    empleado('pedro','chef',123454),
    empleado('david','conductor',123456),
]
# se almacena la lista en una variable.
filtro_nombres = filter(lambda empleado: empleado.nombre == 'pedro', lista)
# se itera la lista.
for x in filtro_nombres:
    print(x)