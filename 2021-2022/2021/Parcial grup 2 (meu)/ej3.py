'''
David Sánchez Mas, 74394689Q
'''

n = int(input())
m = int(input())

def crearMatriz(n, m):  #Crearemos una matriz donde todos sus elementos son nulos

    matriz = []
    for i in range(n):
        fila = []
        for i in range(m):
            fila.append(0)
        matriz.append(fila)
    return matriz

def anyadirValores(matriz, n, m):

    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i+j) % 2 == 0:
                matriz[i-1][j-1] = i + j
            else:
                matriz[i-1][j-1] = i - j
    return matriz

def productoColumnas(matriz, n, m):
    
    fila_productos = []
    for j in range(m):
        producto = 1
        for i in range(n):
            producto *= matriz[i][j]
        fila_productos.append(producto)
    matriz.append(fila_productos)
    return matriz

def imprimirMatriz(matriz, n, m):

    for i in range(n+1):
        fila_matriz = " ".join(str(elemento) for elemento in matriz[i])
        print(fila_matriz)
    return matriz

matriz = crearMatriz(n, m)
anyadirValores(matriz, n, m)
productoColumnas(matriz, n ,m)
imprimirMatriz(matriz, n, m)
