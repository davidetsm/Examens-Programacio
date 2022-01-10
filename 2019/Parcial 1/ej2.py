def insertaCad(lista, cad):
    lista_nueva = []
    for i in lista:
        if cad in lista_nueva:
            lista_nueva.append(i)
        else:
            if ord(i) > ord(cad):
                lista_nueva.append(cad)
                lista_nueva.append(i)
            else:
                lista_nueva.append(i)

    return lista_nueva

print(insertaCad(["a", "b", "d", "e"], "c"))