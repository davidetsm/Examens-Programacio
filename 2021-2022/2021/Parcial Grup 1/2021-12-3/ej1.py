def ordenarLista(lista):
    for i in range(len(lista)):
        menor = lista[i]
        posicion = i
        for j in range(i, len(lista)):
            if lista[j] < menor:
                menor = lista[j]
                posicion = j
        variable = lista[posicion]
        lista[posicion] = lista[i]
        lista[i] = variable

    return lista

def kMinMax(lista, k):
    if k > len(lista):
        k = len(lista)
    lista_copia = lista.copy()
    ordenarLista(lista_copia)
    lista_solucion = []
    for i in range(k):
        lista_solucion.append(lista_copia[i])
    lista_reverse = lista_copia[::-1]
    for i in range(k):
        lista_solucion.append(lista_reverse[i])
    return lista_solucion

print(kMinMax([3, 4, 5], 5))