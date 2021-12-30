def recorta(A, i):

    nueva_matriz = A.copy()
    nueva_matriz.pop(i)
    matriz_final = []
    for j in range(len(nueva_matriz)):
        matriz_final.append([])
    for j in range(len(nueva_matriz)):
        for k in range(len(nueva_matriz)):
            matriz_final[j].append(nueva_matriz[j][k+1])  
    return matriz_final

def determinante(A):

    suma = 0
    if len(A) == 1:
        return A[0][0]
    for j in range(len(A)):
        suma += A[j][0]*((-1)**j)*determinante(recorta(A, j))
    
    return suma

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(determinante(A))