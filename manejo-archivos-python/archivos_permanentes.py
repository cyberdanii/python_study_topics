# Archivos BIANRIOS
import pickle
from colorama import *
import os
init()
class personas():
    def __init__(self,nombre,edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
    def __str__(self):
        return "{}\n{}\n{}\n".format(self.nombre,self.edad,self.pais)
class lista_personas(): #clase para leer archivo binario
    def __init__(self):
        self.persona= []
        arch_dir = "arch_binario"
        lista_depersonas = open(arch_dir,"rb+")
        try:
            self.persona = pickle.load(arch_dir)
            lista_depersonas.seek(0)
            print("total of {} ".format(len(self.persona)))
        except:
            print("The file is empty")
        finally:
            lista_depersonas.close()
            del(lista_depersonas)
        
    def cargarVariable(self,var):
        self.persona.append(var)
        print("var cargada")
    def crear_binario(self):
        arch_binari = open("arch_binario","wb")
        pickle.dump(self.persona,arch_binari)
        print(Back.GREEN+"El archivo ahora existe"+Back.RESET)
        arch_binari.close()
        del(arch_binari)

    def mostrarinfo(self):
        print("info de las personas: ")
        for a in self.persona:
            print(a)
        return "" # evita que se imprima 'None' al final de ejecutar la funcion

class modificador_binario():
    personas = list()
    def __init__(self,nombrearchivo):
        self.nombrearchivo = nombrearchivo
        
    def generar(self):
        file=open(self.nombrearchivo,"wb")
        pickle.dump(self.personas,file)    
        file.close()
        del(file)
        
    def leer(self):
        file = open(self.nombrearchivo,"rb")
        b = pickle.load(file)
        file.seek(0)
        print("info total {}".format(len(b)))
        print(b)
        file.close()
        del(file)
    def sobrescribir(self, personasp):
        self.personas.append(personasp)
        file=open(self.nombrearchivo,"wb+")
        try:
            pickle.dump(self.personas,file)
            print("- sobrescrito -")
        except:
            print("xxXxx")
        finally:
            file.close()
            del(file)

personas = ["carlos","juan","pedro"]
mb = modificador_binario("arch_binario")
mb.sobrescribir(personas)
mb.leer()

'''
NOTA: cada vez que se hace 'dump' en un archivo binario
        para sobreescribirlo se borra la informacion previa en el
'''
