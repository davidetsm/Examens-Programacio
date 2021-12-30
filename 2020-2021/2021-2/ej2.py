from sys import argv

def particiones(n, k):
    if k == 1 or n == k:
        return 1
    return particiones(n-1, k-1) + k*particiones(n-1, k)

n = int(argv[1])
nombre = "particiones_" + argv[1] + ".txt"

salida = open(nombre, "w")
for i in range(1, n+1):
    print(i, particiones(n, i), file = salida)

salida.close()