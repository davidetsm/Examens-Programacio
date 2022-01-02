def nomultiplos(n, num1, num2):
    if n <= 0 or num1 <= 0 or num2 <= 0:
        return None
    lista = []
    for i in range(1, n):
        if i % num1 != 0 and i % num2 != 0:
            lista.append(i)
    return lista

def printLista(lista):
    if len(lista) == 0:
        print("No hay ningún número que cumpla las especificaciones")
        return
    for i in range(len(lista) - 1):
        print(lista[i], end = ", ")
    print(lista[-1], end = ".\n")
    return

n = int(input())
num1 = int(input())
num2 = int(input())

lista = nomultiplos(n, num1, num2)
if nomultiplos(n, num1, num2) == None:
    print("Error en los parámetros")
else:
    printLista(lista)