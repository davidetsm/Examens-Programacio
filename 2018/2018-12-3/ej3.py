def leerMatriz(n):
    matriz = []
    for i in range(n):
        fila = [float(x) for x in input().split()]
        matriz.append(fila)
    return matriz

def TriangularSuperior(matriz):

    for i in range(len(matriz)):
        if len(matriz) != len(matriz[i]):
            return None

    for i in range(1, len(matriz)):
        for j in range(i):
            if matriz[i][j] != 0:
                return False

    return True

n = int(input())
matriz = leerMatriz(n)
print(TriangularSuperior(matriz))