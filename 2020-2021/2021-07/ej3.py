from sys import argv

if len(argv) == 2:
    try:
        entrada = open(argv[1], "r")
        datos = [int(x) for x in entrada.readline().split()]
        
        entrada.close()

        maxFrec = datos.count(datos[0])
        for i in range(1, len(datos)):
            frecuencia = datos.count(datos[i])
            if frec > maxFrec:
                maxFrec = frec

        print(maxFrec)

    except IOError:
        print("Error: no se puede abrir el archivo", argv[1])

else:
    print("Uso:", argv[0], "archivo_de_datos")