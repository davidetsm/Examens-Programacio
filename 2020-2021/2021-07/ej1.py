from sys import argv
import time


cadena1 = argv[1]
cadena2 = argv[2]

longitud1 = len(cadena1)
longitud2 = len(cadena2)

iterador = 0
contador = 0


while (longitud1) > longitud2:
    i = cadena1.find(cadena2)
    iterador =  i + longitud2
    cadena1 = cadena1[iterador:]
    if i >= 0:
        contador += 1
    longitud1 = len(cadena1)



print(contador)