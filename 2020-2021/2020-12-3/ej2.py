cadena = input()

lista_pre = []


for elemento in cadena:
    lista_pre.append(elemento)

lista = []

for i in range(len(lista_pre)):
    lista.append(lista_pre[i].lower())


if len(lista)%2 == 0: #Cadena de longitud par
    
    pivote = (len(lista)//2) - 1
    lista1 = []
    lista2 = []

    for i in range(pivote + 1):
        lista1.append(lista[i])

    for i in range(len(cadena) - 1, pivote, -1):
        lista2.append(lista[i])


    if lista1 == lista2:
        print(True)
    else:
        print(False)
    
else:

    pivote = len(lista)//2 
    lista1 = []
    lista2 = []

    for i in range(pivote):
        lista1.append(lista[i])

    for i in range(len(cadena)-1, pivote, -1):
        lista2.append(lista[i])

    if lista1 == lista2:
        print(True)
    else:
        print(False)