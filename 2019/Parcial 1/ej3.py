def triangular(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)

    contador = 1
    for i in range(n):
        matriz[0][i] = contador
        contador += 1
    iterador = 1
    for i in range(1, n):
        iterador = i
        for j in range(iterador, n):
            matriz[i][j] = contador
            contador += 1
            iterador += 1
    return matriz

def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        fila = " ".join(str(x) for x in matriz[i])
        print(fila)
    return

n = int(input())
matriz = triangular(n)
imprimirMatriz(matriz)