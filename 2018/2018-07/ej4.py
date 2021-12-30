from sys import argv

try:

    ex = argv[1][::-1]
    extension_reverse = ""
    for i in ex:
        if i == ".":
            break
        extension_reverse += i
    extension = extension_reverse[::-1]
        

    palabra = argv[2]

    nombre_mal = argv[1]
    nombre = ""
    for i in nombre_mal:
        if i == ".":
            break
        nombre += i
    nombre += "_" + palabra + "." + extension


    entrada = open(argv[1], "r")
    salida = open(nombre, "w")

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
                salida.write("{}: {}".format(i+1, lineas[i][:-1]))
                salida.write("\n")
                break

    entrada.close()
    salida.close()
except:
    print("Error")