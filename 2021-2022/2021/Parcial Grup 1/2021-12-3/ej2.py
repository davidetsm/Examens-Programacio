def divisores(n):

    lista_primos = []
    for i in range(2, n//2 +1):  #Generamos toda la lista de divisores primos de n
        if n % i == 0:
            esPrimo = True
            for j in range(2, round(i**0.5)+1):
                if i % j == 0:
                    esPrimo = False
                    break
            if esPrimo:
                lista_primos.append(i)

    #Creamos la lista de divisores y añadimos los elementos:
    lista_divisores = []

    iterador = 0
    while n % lista_primos[iterador] == 0:
        cociente = n / lista_primos[iterador]
        lista_divisores.append(lista_primos[iterador])
        n = cociente
        if n % lista_primos[iterador] != 0:
            iterador += 1
            if iterador == len(lista_primos):
                break
    return lista_divisores


def repeticiones(lista):

    lista_unicos = []
    for i in range(len(lista)):
        if lista[i] not in lista_unicos:
            lista_unicos.append(lista[i])
    lista_repeticiones = []
    for i in range(len(lista_unicos)):
        a = lista.count(lista_unicos[i])
        lista_repeticiones.append(a)

    return lista_unicos, lista_repeticiones

n = int(input())
divisores(n)
lista_unicos, lista_repeticiones = repeticiones(divisores(n))

for i in range(len(lista_unicos)):
    print("{}^{}".format(lista_unicos[i], lista_repeticiones[i]), end = " ")