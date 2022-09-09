
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
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
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
        return "codigo: {} nombre: {} valor: {}".format(str(self.__codigo), self.__nombre, str(self.__valor))

    def total_por_unidad(self, unidad):
        float(unidad)
        print("valor total es: "+str(self.__valor*unidad))
        return unidad
class pedido():
    def __init__(self,producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    def cantidad_total(self):
        total = 0
        for p,c in zip(self.producto, self.cantidad):
            total = total + p.total_por_unidad(c)
        return total
    def mostrar_productos(self):
        for p,c in zip(self.producto, self.cantidad):
            print("Producto: {} Cantidad: {}".format(p.nombre,str(c)))
    # Agregar producto
    def agregar_producto(self,producto,cantidad):
        if not isinstance(producto,productos):
            raise Exception("agregar producto: el producto debe ser de la clase producto")
        if not isinstance(cantidad,int):
            raise Exception("agregar producto: la cantidad debe ser un numero")
        if cantidad <= 0:
            raise Exception("la cantidad debe ser mayor a 0")
        if producto in self.producto:
            index = self.producto.index(producto)
            self.cantidad[index] = self.cantidad[index]+cantidad
        else:
            self.producto.append(producto)
            self.cantidad.append(cantidad)
    # Eliminar prducto
    def eliminar_pedido(self,producto):

        if producto in self.producto:
            index = self.producto.index(producto)
            del self.producto[index]
            print("producto eliminado")
        else:
            print("Producto a eliminar no existe")
TIPO_DESC_FIJO = "fijo"
TIPO_DESC_PORCEN = "porcentaje"
class descuento():
    def __init__(self,tipo, descuento):
        if tipo != TIPO_DESC_FIJO and tipo != TIPO_DESC_PORCEN:
            raise Exception("El descuento debe ser fijo o por porcentaje")
        if not isinstance(tipo,str):
            raise Exception("El tipo debe ser un string")
        if not isinstance(descuento,int):
            raise Exception("El descuento debe ser un numero")
        if tipo == TIPO_DESC_FIJO and descuento <= 0:
            raise Exception("El descuento debe ser mayor a 0")
        if tipo == TIPO_DESC_PORCEN and descuento <= 0 or descuento > 100:
            raise Exception("el descuento debe estar entre 0% y 100%")
        self.__tipo = tipo
        self.__descuento = descuento
    def aplicar_descuento(self, valor):
        if not isinstance(valor, float):
            raise Exception("el valor debe ser un numero")
        if valor <= self.__descuento:
            raise Exception("el valor debe ser mayor al descuento")
        elif self.__tipo == TIPO_DESC_FIJO:
            nvalor = valor - self.__descuento
            return nvalor
        else:
            nvalor = (self.__descuento*(valor / 100))
        return nvalor

po0 = productos(12,"camara",12.00)
po1 = productos(13,"play station",100.00)
po2 = productos(14,"celular",62.00)

print(po0)
print(po1)
print(po2)

# probando la clase de pedidos
l_productos = [po0,po1,po2]
l_cantidad = [12,34,54]

po0.total_por_unidad(5)
po1.total_por_unidad(5)
po2.total_por_unidad(5)

pedidos = pedido(l_productos,l_cantidad)
print(pedidos.cantidad_total())
print(pedidos.mostrar_productos())

# Agregando y eliminando un producto
try:
    pedidos.agregar_producto(po0,4)
    pedidos.agregar_producto(po1,5)
    pedidos.agregar_producto(po2,6)

    pedidos.eliminar_pedido(po1)

    print(pedidos.cantidad_total())
    print(pedidos.mostrar_productos())
except Exception as e:
    print(e)

# usando la clase descuento
desc1 = descuento(TIPO_DESC_FIJO,5)
desc2 = descuento(TIPO_DESC_PORCEN,50)

print(po0.valor)
print(desc1.aplicar_descuento(po0.valor))
print(desc2.aplicar_descuento(po1.valor))
