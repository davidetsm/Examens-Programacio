def prodEscalar(matriz, k):
    contador = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] *= k
    return matriz

n = int(input("n: "))

def crearMatriz(n):
    matriz = []
    for i in range(n):
        matriz.append([])
    return matriz

def llenarMatriz(n, matriz):
    for i in range(n):
        for j in range(n):
            matriz[i].append(n + (i+1) + (j+1))
    return matriz

matriz = crearMatriz(n)
matriz = llenarMatriz(n, matriz)
matriz = prodEscalar(matriz, n)
print(matriz)