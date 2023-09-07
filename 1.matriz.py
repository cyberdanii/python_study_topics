# creando matriz de diferentes columnas y filas
from colorama import *
init()
matriz = []
col = int(input("No. columnas: "))
fil = int(input("No. filas: "))
for i in range(fil):
   matriz.append([0]*col)
    
for f in range(fil):
    for c in range(col):
        x= input("Elemento {} {}:".format(c,f))
        if x=='':
            x='0'
            matriz[c][f] = x
        else:
            matriz[c][f] = x

print(matriz)

def matriz_grid(m):
    cont=0
    for i in m:
        for x in i:
            if x == '1':
                print(Back.RED+x+Back.RESET,end=" ")
            if x == '2':
                print(Back.CYAN+x+Back.RESET,end=" ")
            if x == '3':
                print(Back.YELLOW+x+Back.RESET,end=" ")
            if x == '4':
                print(Back.GREEN+x+Back.RESET,end=" ")
            if x == '5':
                print(Back.BLUE+x+Back.RESET,end=" ")
            if x == '6':
                print(Back.MAGENTA+x+Back.RESET,end=" ")
            else:
                continue
        if cont== 3 or 6 or 9 or 12 or 15:
                print("\n")
        cont+=1
def matriz_end(m):
    for i in m:
        for x in i:
            if x == '1':
                print(Back.RED+x+Back.RESET,end=" ")
            if x == '2':
                print(Back.CYAN+x+Back.RESET,end=" ")
            if x == '3':
                print(Back.YELLOW+x+Back.RESET,end=" ")
            if x == '4':
                print(Back.GREEN+x+Back.RESET,end=" ")
            if x == '5':
                print(Back.BLUE+x+Back.RESET,end=" ")
            if x == '6':
                print(Back.MAGENTA+x+Back.RESET,end=" ")
            else:
                continue

matriz_grid(matriz)
matriz_end(matriz)

