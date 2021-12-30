def recorta(M, i, j):
    M_reverse = M.reverse()
    matriz_solucion = []
    if i > len(M) or j > len(M[0]):
        return []

    elif i <= 1:
        for k in range(len(M_reverse)):
            matriz_solucion.append([])
        for k in range(len(matriz_solucion)):
            for p in range(p-1, len(M[0])):
                matriz_solucion[k].append(M_reverse[k][p])
        return matriz_solucion

    elif j <= 1:
        M_reverse = M.reverse()
        for k in range(i-1):
            M_reverse.pop(-1)
        matriz_solucion = M_reverse.reverse()
        return matriz_solucion
    
    matriz_solucion = []
    for k in range(i-1):
        M.reverse.pop(-1)
    M_reverse.reverse()
    for k in range(len(M_reverse)):
        matriz_solucion.append([])
    for k in range(len(matriz_solucion)):
        for p in range(p-1, len(M[0])):
            matriz_solucion[k].append(M_reverse[k][p])
    return matriz_solucion

M = [[1, 2, 3, 4], [5, 6, 7, 8]]

print(recorta(M, 2, 3))