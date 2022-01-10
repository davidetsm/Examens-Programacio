tiempo = int(input("Introduce el número en segundos: "))

while tiempo < 0:
    tiempo = int(input("Error. Vuelve a introducir el dato: "))

if tiempo >= 60:
    minutos = tiempo // 60
    segundos = tiempo % 60
    if minutos >= 60:
        horas = minutos // 60
        minutos = minutos % 60
        if horas >= 24:
            dias = horas // 24
            horas = horas % 24
        else:
            dias = 0
    else:
        horas = 0
        dias = 0
else:
    segundos = tiempo
    minutos = 0
    horas = 0
    dias = 0

print("{} días, {} horas, {} minutos y {} segundos".format(dias, horas, minutos, segundos))