def productoIndicesImpar(matriz):
    producto = 1

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i+j) % 2 != 0:
                producto *= matriz[i][j]
    return producto

matriz = [[1, 2, 3], [0, 12, 6], [0, 0, -3]]

print(productoIndicesImpar(matriz))