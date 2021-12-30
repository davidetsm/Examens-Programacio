def manipula(cadena):

    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida

    cadena_solucion = ""
    for letra in cadena_invertida:
        if letra not in cadena_solucion:
            cadena_solucion += letra

    return cadena_solucion

cadena = ("En un lugar de la mancha de cuyo nombre no quiero acordarme")
print(manipula(cadena))