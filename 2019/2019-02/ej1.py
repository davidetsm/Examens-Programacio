cadena = input()

lista = []

resultado = ""

for i in cadena:
    lista.append(i)

print(lista)

for i in range(len(cadena)-1, -1, -1):
    resultado = lista[i] + resultado
    print(resultado)