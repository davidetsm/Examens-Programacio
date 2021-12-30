def sumaSubMatrices(M):
    lista = []
    for i in range(max(len(m), len(m[0]))):
        suma = 0
        for j in range(i + 1):
            if j < len(M):
                for k in range(i+1):
                    if k < len(M[0]):
                        suma += M[j][k]
        lista.append(suma)
    return lista

def leerMatriz():
    M = []
    for i in range(int(input())):
        M.append([int(x) for x in input().split()])
    return M

def escribeLista(L):
    for i in range(len(L)):
        print("i = {}: {}".format(i, l[i]))

A = leerMatriz()
escribeLista(sumaSubMatrices(A))