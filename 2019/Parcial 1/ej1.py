segundos = int(input("Introduce el número en segundos: "))
while segundos < 0:
    print("Error. Vuelve a introducir el dato: ", end = "")
    segundos = int(input())

if segundos % 60 == 0: #Vemos si el resto de pasar a minutos es 0
    minutos = segundos / 60
    segundos = 0
else:
    minutos = segundos // 60
    segundos = segundos % 60

if minutos % 60 == 0:
    horas = minutos / 60
    minutos = 0
else:
    horas = minutos // 60
    minutos = minutos % 60

if horas % 24 == 0:
    dias = horas / 24
    horas = 0
else:
    dias = horas // 24
    horas = horas % 24

print("{} días, {} horas, {} minutos y {} segundos.".format(int(dias), int(horas), int(minutos), int(segundos)))