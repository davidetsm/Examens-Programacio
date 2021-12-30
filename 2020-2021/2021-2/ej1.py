def leeNotas():
    try:
        datos = open("C:/Users/david/OneDrive/Escritorio/Universitat/Primer/Primer Quatri/Fonaments de programació/Examens/2020-2021/2021-2/notas.dat", "r")

        notas = []
        for linea in datos:
            notas.append([int(x) for x in linea.split()])
        datos.close()
        return datos
    
    except IOError:
        return []

def abandono(notasAlu):
    if notasAlu[-1] != -1:
        return None
    for i in range(len(notasAlu)-1, -1, -1):
        if notasAlu[i] != -1:
            return i+1
    return 0

notas = leeNotas()
semanaAbandono = [0]*len(notas[0])

for alumno in notas:
    semana = abandono(alumno)
    if semana != None:
        semanaAbandono[abandono(alumno)] += 1
for i in len(semanaAbandono):
    if semanaAbandono[i] != 0:
        print("{}: {}".format(i, semanaAbandono[i]))