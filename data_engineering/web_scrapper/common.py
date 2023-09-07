import yaml
from yaml import SafeLoader
import os

__config = None

def config() -> dict:
    '''
    Funcion para leer el contenido del archivo YAML
    '''

    global __config

    if not __config:

        with open( os.path.join(os.path.dirname(__file__),"config.yaml"),"r") as f:
            __config =  yaml.load(f, Loader=SafeLoader)

    # retorna un diccionario de lo que hay en el archivo YAML            
    return __config
