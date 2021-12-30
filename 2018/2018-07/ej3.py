from sys import argv

try:

    entrada = open(argv[1], "r")

    cadena = argv[2]

    lineas = entrada.readlines()
    palabras = []

    for i in range(len(lineas)):
        palabras.append([])


    for i in range(len(lineas)):
        linea = lineas[i].split()
        for j in linea:
            palabras[i].append(j)

    for i in range(len(palabras)):
        for j in palabras[i]:
            if j == cadena:
                print("{}: {}".format(i+1, lineas[i][:-1]))
                break

    entrada.close()
except:
    print("ERROR")