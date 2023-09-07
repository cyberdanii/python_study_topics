import pandas as pd
# manejo de archivos
filePath = "empleados.xls" # nombre del archivo
hoja = "Base de datos" # nombre de la hoja
dataFrame = pd.read_excel(filePath, sheet_name=hoja) # lee el archivo excel
#print(dataFrame.columns.values) # imprime el nombre de las columnas
#print(dataFrame) # imprime toda la hoja
#print(dataFrame.head()) # imprime las primeras filas
#print(dataFrame.dtypes) # imprime los tipos de datos en cada columna
print(type(pd.unique(dataFrame["Nombre"]))) # imprime una unica columna
#print(dataFrame["Salario"].describe()) # imprime una descripcion de la columna, usando diferentes operaciones matematicas
#print(dataFrame.groupby("Cargo").max()) # agrupa los datos por una columna en especifico
#print(dataFrame.groupby("Salario")["Nombre"].count())
#dataFrame.groupby("Salario")["Nombre"].count().plot(kind='bar')

# Imprimir hojas del Archivo.
    # xl = pd.ExcelFile(dirFile)
    # print(xl.sheet_names)
    

valores = [dataFrame["Salario"].max(),dataFrame["Salario"].min()]

indices = ["maximo salario","minimo salario"]
r = pd.DataFrame(data=valores, index=indices,columns=["valores"])
print(r)

archivoFinal = "resultados.xls"

writer = pd.ExcelWriter(archivoFinal)
r.to_excel(writer,sheet_name="resumen de salarios")
writer.save()

# https://github.com/DavidArmendariz/YouTube-Codes/blob/master/Python%20Excel%20Pandas.ipynb
