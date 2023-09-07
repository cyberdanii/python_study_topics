from colorama import *
import datetime
init()

date = datetime.datetime.today()
day = date.day

# mes
month = date.month
# año
year = date.year
# hora
hour = date.year
#minutos
minut = date.minute
# segundos
sec = date.second   
#-----------------------------------
print(Fore.RED+str(date)+Fore.RESET)
print(Fore.BLUE+str(day)+Fore.RESET)
print(Fore.GREEN+str(month)+Fore.RESET)
print(Fore.WHITE+str(year)+Fore.RESET)
print(Fore.CYAN+str(hour)+Fore.RESET)
print(Fore.MAGENTA+str(minut)+Fore.RESET)
print(Fore.YELLOW+str(sec)+Fore.RESET)

fecha_simple = datetime.datetime.strftime(date,'%d %B %Y')

print(Back.YELLOW+Fore.BLACK+str(fecha_simple)+Fore.RESET+Back.RESET)