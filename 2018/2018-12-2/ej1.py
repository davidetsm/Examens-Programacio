entrada = open("/etc/passwd", "r")

nombre = []

for lineas in entrada:
    linea = lineas.split(":")
    nombre.append(linea[4])

print(nombre)
    

entrada.close()