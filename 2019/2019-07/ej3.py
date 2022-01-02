from sys import argv

entrada = open(argv[1], "r")
salida = open(argv[2], "w")

lista = entrada.readlines()
lista_2 = []
for i in range(len(lista) -1, -1, -1):
    lista_2.append(lista[i][::-1])

for i in range(len(lista_2)):
    salida.write(lista_2[i][1:])
    salida.write("\n")

salida.close()
entrada.close()