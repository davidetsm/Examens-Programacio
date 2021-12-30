def borraPares(lista):
    lista_nueva = []
    for i in lista:
        if i % 2 != 0:
            lista_nueva.append(i)
    lista = lista_nueva
    return lista

def eliminaPares(lista):
    lista_nueva = []
    for i in lista:
        if i % 2 != 0:
            lista_nueva.append(i)
    return lista_nueva

lista = [1, 0, 2, 16, 11, 15, -2]

print(lista)
input()
borraPares(lista)
print(lista)