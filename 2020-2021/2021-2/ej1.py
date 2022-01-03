def leeNotas():
    entrada = open("notas.dat", "r")
    lineas = entrada.readlines()
    entrada.close()

    matriz = []
    for i in range(len(lineas)):
        fila = lineas[i].split()
        matriz.append(fila)
    return matriz

matriz = leeNotas()

def abandono(notasAlu):
    for i in range(len(notasAlu)):
        if int(notasAlu[i]) == -1:
            contador = i
            return contador
    return None
matriz_semanas = []
for i in range(len(matriz[0])):
    matriz_semanas.append([])
for i in range(len(matriz)):
    if abandono(matriz[i]) != None:
        matriz_semanas[abandono(matriz[i])].append(1)
print(matriz_semanas)