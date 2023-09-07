'''
METACHARACTERS
Metacharacters are characters with a special meaning:

[]	A set of characters	                                                        "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	                                "he..o"	
^	Starts with	                                                                "^hello"
$	Ends with	                                                                "world$"	
*	Zero or more occurrences	                                                "aix*"	
+	One or more occurrences	                                                    "aix+"	
{}	Exactly the specified number of occurrences	                                "al{2}"	
|	Either or	                                                                "falls|stays"	
()	Capture and group

--------------------------------------------------------


'''
import re as regexp

text = "This code 123-456/789"

var_search = regexp.search("^This", text)
print(var_search.string)

var_search1 = regexp.search("^This code ([0-9]/[-]/[0-9])+", text)
print(var_search1.string if var_search1 != None else 'None')

Analytics
Facturación
Reportes
Dimensionamiento y turnos
Desempeño
Implementación
Gestión de la capacidad

Oficina de proyectos
Diseño de producto
Transformación Digital
Innovación

	



Diseño de CX



Diseño de soluciones



Aseguramiento de CX



SGI y Auditoría