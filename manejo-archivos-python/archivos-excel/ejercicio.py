
# MANEJO DE ARCHIVOS CON PYTHON
# pip install pandas
# pip install xlwt # modulo importante
import pandas as pd

filePath = "empleados.xls"
hoja = "Base de datos"
dataFrame = pd.read_excel(filePath, sheet_name=hoja)
print(dataFrame)
print("-----------------------------------")
#print(dataFrame.head())
#print(pd.unique(dataFrame["Nombre"]))
#print(dataFrame["Nombre"])
#print(dataFrame["Salario"].describe())
#print(dataFrame["Salario"].max())
#print(dataFrame["Salario"].min())
#print(dataFrame.groupby("Cargo")["Salario"].max())

valores = [dataFrame["Salario"].max(), dataFrame["Salario"].min()]
filas = ["Salario maximo","Salario minimo"]
nuevaHoja = pd.DataFrame(data = valores, index = filas, columns = ["Valores"])
#print(nuevaHoja)

archivoNombre = "archivoFinal.xls"

archivo = pd.ExcelWriter(archivoNombre)
nuevaHoja.to_excel(archivo, sheet_name="resumen")
archivo.save()

#https://openanalytics.es/las-40-mejores-preguntas-y-respuestas-de-la-entrevista-de-python/
#https://datacarpentry.org/python-ecology-lesson-es/02-starting-with-data/