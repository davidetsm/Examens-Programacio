from sys import argv

entrada = open(argv[1], "r")
entrada_lista = entrada.readlines()
entrada.close()

lista = entrada_lista[0].split()

repetidos = []
contadores = []

for i in range(len(lista)):
    contador = 0
    if lista[i] not in repetidos:
        repetidos.append(lista[i])
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1
        
        contadores.append(contador)

print(max(contadores))