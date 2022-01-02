from sys import argv

entrada = open(argv[1], "r")
salida = open(argv[2], "w")

for linea in entrada:
    cadena = ""
    linea = linea[:-1]
    lista = linea.split(" ")
    for i in range(len(lista) - 1, -1, -1):
        if i == 0:
            cadena += lista[i]
        else:
            cadena += lista[i]
    print(cadena)
entrada.close()
salida.close()