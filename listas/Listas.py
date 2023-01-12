# LISTAS:
# Que son: estrutura de datos que nos permiten almacenar varios valores - es un equivalente a un array en otros lenguajes de programacion.
# Utilidad: nos permite guardar diferentes tipos de valores.
# Sintaxis: nombreLista=[item0,item1,item2,]
# Ejecucion:
# ejemplo uno:
thislist = ["apple","pineapple","banana","mango","cherry"]
print(thislist[1])

#ejemplo dos: cambiando valor de un item:

thislist[4]="berry"
print(thislist[4])

#ejemplo  tres: recorriendo valores de la lista con un bucle for:
for x in thislist:
    print("----")
    print(x)
    print("----")
#ejemplo cuatro: con sentencia if
if "apple" in thislist:
    print("this fruit is here")
    print("----")
    
#ejemplo cinco: contar la cantidad de elemtos en la lista:
print("la cantidad de elementos en la lista son: ")
print(len(thislist))
print("----")

#ejemplo seis: agregar un elemto al final de la lista:
thislist.append("orange")
print(thislist[5])
print("----")
#ejemplo siete: remover un elemento de la lista:
thislist.remove("orange")
print(thislist)
print("----")

#tambien se puede utilizar la siguiente sintaxis para eliminar cierto elemento de la lista o toda la lista:
# del thislist[0] - esto elimina el elemento en la posicion 0 de la lista
# del thislist - esto elimina toda la lista

#ejemplo ocho: insertar un elemento en un sitio especifico de la lista:
thislist.insert(2,"pear")#no agregar espacios entre los argumentos
print(thislist[2])
print(thislist)
print("----")

#ejemplo nueve: vaciar un elemento de la lista o vaciar toda la lista:
# thislist.clear() - esto vacia toda la lista, dejando solo los corchetes
# print(thislist)
# thislist.clear(thislist[0])
# print(thislist)

#ejemplo diez: copiar una lista:
newlist=thislist
print(newlist)
print("----")

#ejemplo once: imprimir todos los elemtos que estan entre un elemento y otro:
print(newlist[0:3])#se imprimiran todos los elemtos del elemto 0 hasta el elemto 3
print("----")

#ejemplo doce: imprimir desde cierto elemto en adelante:
print(newlist[3:])
print("----")

#ejemplo trece: saber en que posicion o indice esta cierto elemento:
print(newlist.index("banana"))
print("----")

#ejemplo 14: saber si un elemto se encuentra o no en la lista:
print("naranja" in newlist)# esto devolveria FALSE ya que no se encuentra
print("----")
print("berry" in newlist)# esto devolveria TRUE ya que si se encuentra
print("----")

#ejemplo 15: agregar otra lista o mas elemtos a una lista:
newlist.extend(["onion","lettuce","carrot"])
print(newlist)
print("----")