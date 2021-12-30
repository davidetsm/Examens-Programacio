def Repeticiones(c, cad):
    contador = 0
    for i in cad:
        if c == i:
            contador += 1
    if contador > 0:
        print("{}: {}".format(c, contador))
    return 

cadena1 = input()
cadena2 = input()

lista_caracteres = []

for i in cadena1:
    if i not in lista_caracteres:
        Repeticiones(i, cadena2)
    lista_caracteres.append(i)