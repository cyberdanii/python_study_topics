# se importa la libreria
import pymysql
# coneccion a la base de datos
db = pymysql.connect("localhost","root","root","base_datos_python")

cursor = db.cursor()

# Forma de agregar un dato a la vez.
# cursor.execute("INSERT INTO usuarios VALUES(1,'Juan','Lopez','juan@mail.com','12345asdf')")

def crearTabla():
	# Forma de crear tablas en la base de datos.
	cursor.execute(''' 
		CREATE TABLE usuarios (
			id integer primary key auto_increment,
			nombre  varchar(50),
			apellido varchar(50),
			cedula integer unique
		)
		''')

# Forma de agregar datos en la BD usando lista y tuplas.
datosVariosUsuarios = [
("Mario","fernandez",12345),
("David","Martinez",123456),
("Carlos","Beltran",1234567)
]
#cursor.executemany("INSERT INTO usuarios VALUES(null,%s,%s,%s)", datosVariosUsuarios)


db.commit() # commit() confirma los datos para que sean ingresados en la BD
db.close()