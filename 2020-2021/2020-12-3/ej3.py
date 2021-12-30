contador = 0

cadena = input()

while cadena != "salir":

    if contador % 2 == 0:
        cadena_inversa = ""
        for elemento in cadena:
            cadena_inversa = elemento + cadena_inversa
        print(cadena_inversa)

        contador += 1
        cadena = input()

    else:
        cadena_inversa = ""
        iterador = 0
        for elemento in cadena:
            if (iterador+1)%3 != 0:
                cadena_inversa += cadena[iterador]
                iterador += 1
            else:
                iterador += 1
        print(cadena_inversa)
        
        contador += 1
        cadena = input()