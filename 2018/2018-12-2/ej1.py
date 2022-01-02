entrada = open("/etc/passwd", "r")

nombres = []

for lineas in entrada:
    linea = lineas.split(":")
    nombres.append(linea[4])

for i in nombres:
    print(i)
    
entrada.close()