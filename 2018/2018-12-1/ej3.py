from sys import argv

if len(argv) == 3:

    try:
        entrada = open(argv[1], "r")
        salida = open(argv[2], "w")

        contador = 1

        hora_del_dia = []
        temperatura = []
        velocidad_del_viento = []
        presion_atmosferica = []
        humedad_relativa = []

        for linea in entrada:
            if contador == 1:
                nombres = linea[:-1].split()
            if contador == 2:
                n = int(linea[:-1])
            if contador > 2:
                lista_linea = linea[:-1].split()
                for i in range(len(lista_linea)):
                    if i == 0:
                        hora_del_dia.append(lista_linea[i])
                    elif i == 1:
                        temperatura.append(lista_linea[i])
                    elif i == 2:
                        velocidad_del_viento.append(lista_linea[i])
                    elif i == 3:
                        presion_atmosferica.append(lista_linea[i])
                    elif i == 4:
                        humedad_relativa.append(lista_linea[i])
            contador += 1
        print(nombres)
        for i in range(len(nombres)):
            print(nombres[i], end = ": ")
            for k in nombres[i]:
                print(k, end = " ")
            print("")

        entrada.close()
        salida.close()
    except FileNotFoundError:
        print("El archivo de entrada {} no está disponible".format(argv[1]))
else:
    print("Falta por introducir al menos un archivo")