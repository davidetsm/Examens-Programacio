def recorta(M, i, j):
    M_copia = M.copy()
    M_reverse = M_copia[::-1]

    if i > len(M) or j > len(M[0]):
        print([])
        return []
    
    if i <= 1:
        matriz_final = []
        for k in range(len(M)):
            matriz_final.append([])
        for k in range(len(M)):
            for p in range(j-1, len(M[0])):
                matriz_final[k].append(M[k][p])
        print(matriz_final)
        return
    
    if i <= 1:
        M_reverse = M.reverse()
        for k in range(i-1):
            M_reverse.pop(-1)
        matriz_final = M_reverse.reverse()
        print(matriz_final)
        return

    matriz_final = []

    for k in range(i-1):
        M_reverse.pop(-1)
    M_reverse.reverse()
    for k in range(len(M_reverse)):
        matriz_final.append([])
    for k in range(len(M_reverse)):
        for p in range(j-1, len(M[0])):
            matriz_final[k].append(M_reverse[k][p])
    print(matriz_final)
    return

M = [[1, 2, 3, 4], [5, 6, 7, 8]]
recorta(M, 2, 3)