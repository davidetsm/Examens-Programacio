def triangular(M):
    matriz = []
    for i in range(M):
        matriz.append([])
    contador = 1
    for i in range(M):
        for j in range(M):
            if j >= i:
                matriz[i].append(contador)
                contador += 1
            else:
                matriz[i].append(0)
    return matriz

print(triangular(4))