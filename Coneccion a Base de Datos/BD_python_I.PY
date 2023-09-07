import pymysql
from colorama import init, Fore, Back
init()
db = pymysql.connect("localhost","root","root","db2python")
#-------------------------------------------------------------------

# prepare a cursor object using cursor() method
cursor = db.cursor()

# ejecuta el SQL query usando el metodo execute().
cursor.execute("select id, titulo from listaproductos_producto")
print(cursor)
# procesa una unica linea usando el metodo fetchone().
data = cursor.fetchall()
print(type(data))

print ("table Content : "+Fore.GREEN+"{0}".format(list(data)))

# desconecta del servidor
db.close()

'''
NOTA: importante instalar 'pymysql' desde la consola con 'pip install pymysql'
		para poder conectar a la base de datos con python

		
'''

