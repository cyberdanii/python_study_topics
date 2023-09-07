import datetime
from datetime import date
ahora = datetime.datetime.now().strftime('%d')
print(ahora)
print(datetime.timedelta())

empleado = {'nombre':'Juan Bedoya',
'fecha_contratacion': date(2020,1,15),
'sueldo':1500320}
switch=True

f1 = empleado['fecha_contratacion']
f2 =date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)
diferencia=f2-f1
dias = diferencia.days


print('''
[ DATOS DELL EMPLEADO ]
Nombre: '''+empleado['nombre']+'''
Mes de contratacion: '''+str(empleado['fecha_contratacion'].strftime("%B"))+'''
Sueldo: '''+str(empleado['sueldo'])+'''
----------------------------------------------------
Opciones:
[1] - Salario actual del empleado
[2] - Sueldo actual con retencion de ley del 10%
[3] - Monto desembolsado al empleado hasta hoy
[s] - Salir del programa
''')

while switch==True:

    opcion = input("Opcion: ")
    if opcion == '1':
        print(f"El salario actual para el empleado es: {(empleado['sueldo']/30)*dias}")
    elif opcion == '2':
        print(f"La retencion por mes es de: {(empleado['sueldo']/100)*10}")
        print(f"El salario con la retencion de ley al mes es {(empleado['sueldo']/100)*90}")
    elif opcion=='3':
        
        if dias <30:
            salario_x_dia=empleado['sueldo']/30
            print(f"El monto desembolsado al trabajador hasta el dia de hoy es: {salario_x_dia*dias}")
        else:
            salario_x_dia=((empleado['sueldo']/100)*90)/30
            print(f"El monto desembolsado al trabajador hasta el dia de hoy es: {salario_x_dia*dias}")
        
        
    elif opcion == 's':
        switch = False
        print('¡Hasta pronto!')
    else:
        print('¡opcion incorrecta!')


