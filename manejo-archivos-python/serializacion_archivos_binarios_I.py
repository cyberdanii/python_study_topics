import pickle
'''
SERIALIZACION:
    consiste en convertir cualquier codigo u archivo 
    en un archivo con contenido binario.
    Esto sirve para guardar informacion de forma mas facil en 
    un dico duro, servidor, based de datos, etc.
'''
# Creacion de archivo Binario
def crear_binario(info):
    file = open("prueba_binario","wb")
    pickle.dump(info,file)
    file.close()
    del file
# leer archivo binario
def leer_binario():
    file = open("prueba_binario","wb")
    content = pickle.load(file)
    print(content)
    file.close()
    del file
