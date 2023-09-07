from itertools import combinations_with_replacement
from colorama import init, Fore
from os import system
init()
fred, fgreen, fyellow, freset = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.RESET
alphabet = "q w e r t y u i o p a s d f g h j k l ñ z x c v b n m"
numbers = "1 2 3 4 5 6 7 8 9 0"
symbols = "! # $ % & / ( ) = ? ¡ ¿ * + ~ { } [ ] - _ ; , . : @ | ° < >"
others = ""
allchar = "q w e r t y u i o p a s d f g h j k l ñ z x c v b n m 1 2 3 4 5 6 7 8 9 0 ! # $ % & / ( ) = ? ¡ ¿ * + ~ { } [ ] - _ ; , . : @ | ° < >"

listAlphabet = alphabet.split()
listNumbers = numbers.split()
listSymbols = symbols.split()

iterNum = len(listAlphabet)+len(listNumbers)+len(listSymbols)

def escribirArchivo(texto):
	file = open("passwordList.txt","a")
	file.write(texto+"\n")
	print(fgreen,"Saved",freset)
	file.close()

for x in range(5,iterNum):
	for passw in combinations_with_replacement(allchar, x):

		password = ""
		union = password.join(passw)
		print(fyellow,union, end=" ")
		escribirArchivo(union)

	#for passw in combinations_with_replacement(listNumbers, x):

		#password = ""
		#union = password.join(passw)
		#print(union, end=" ")
		#escribirArchivo(union)

	#for passw in combinations_with_replacement(listSymbols, x):

		#password = ""
		#union = password.join(passw)
		#print(union, end=" ")
		#escribirArchivo(union)

