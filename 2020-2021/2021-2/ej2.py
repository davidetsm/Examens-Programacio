def particiones(n, k):
    while n != k and k != 1:
        return particiones(n-1, k-1) + k*particiones(n-1, k)
    if n == k or k == 1:
        return 1

from sys import argv
nombre_archivo = "particiones_" + argv[1] + ".txt"

salida = open(nombre_archivo, "w")

for i in range(int(argv[1])):
    contador = i + 1
    salida.write("{} {}".format(contador, particiones(int(argv[1]), contador)))
    salida.write("\n")

salida.close()