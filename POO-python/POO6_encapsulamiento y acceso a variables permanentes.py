import colorama
class productos():
    def __init__(self, codigo, nombre, valor):
        #variables encasuladas o privadas
        self.__codigo = int(codigo)
        self.__nombre = nombre
        self.__valor = float(valor)
    # metodos o funciones de acceso a variables privadas
#-----------------------------------------
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, var):
        self.__codigo = var

    @codigo.deleter
    def codigo(self):
        del self.__codigo
        # borra por completo la variable de la memoria

#-----------------------------------------
    @property # 'property' equivale al GETTER
    def nombre(self):
        return self.__nombre
    @nombre.setter # SETTER
    def nombre(self, nom):
        self.__nombre=nom
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        # borra por completo la variable de la memoria

#-----------------------------------------
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, val):
        self.__valor=val
    @valor.deleter
    def valor(self):
        del self.__valor
        # borra por completo la variable de la memoria
        # si se ejecuta de nuevo la script mostrara error por que ya no existe la variable en la clase
    def __str__(self):
        print("codigo: {} nombre: {} valor: {}".format(self.__codigo, self.__nombre, self.__valor))
    
    def total_por_unidad(self, unidad):
        float(unidad)
        print("valor total es: "+str(self.__valor*unidad))
        return ""

#-----------------------------------------

# se crean los objetos
po0 = productos(12,"camara",12.00)
po1 = productos(13,"play station",100.00)
po2 = productos(14,"celular",62.00)

print(po0.codigo, po0.nombre, po0.valor)
print(po1.codigo, po1.nombre, po1.valor)
print(po2.codigo, po2.nombre, po2.valor)

'''
NOTA: en el caso de las funciones de acceso se colocan sin parentesis en cualquier uso
        que se les de.
'''
#-----------------------------------------
# cambiando los valores con las funciones setters
po0.codigo = 1
po0.nombre = "helado"
po0.valor = 1.00
print(po0.codigo,po0.nombre,po0.valor)

#------ valor del producto por las unidades
print(po0.total_por_unidad(5))
print(po1.total_por_unidad(6))
print(po2.total_por_unidad(7))
