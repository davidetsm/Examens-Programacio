def crearamigo(premiado):
    divisores_premiado = []

    i = 1
    while i < premiado:  #Calculamos la lista de divisores del número
        if premiado % i == 0:
            divisores_premiado.append(i)
        i += 1
    
    suma_premiado = 0
    for i in range(len(divisores_premiado)):
        suma_premiado += divisores_premiado[i]
    
    return suma

premiado = 1184
amigo = amigos(premiado)
print(amigo)

def comprobarAmigo(amigo, premiado):
    divisores_amigo = []

    i = 1
    while i < amigo:
        if amigo % i == 0:
            divisores_amigo.append(i)
    
    suma_amigo = 0
    for i in range(len(divisores_amigo)):
        suma_amigo += divisores_amigo[i]

    if suma_amigo == premiado:
        return True
    return False

def capicua(amigo):

    lista = []
    for elemento in amigo:
        lista.append(elemento)

    digitos = len(str(amigo))
    if digitos == 1 or digitos == 2:
        return False
    if digitos == 3:
        if lista[4] == 0:
            if lista[3] == 0:
                return True
            return False
        return False

    if digitos == 4:
        if lista[4] == 0:
            if lista [1] == lista[3]:
                return True
        return False
    
    if digitos == 5:
        lista1 = []
        lista2 = []
        for i in range(2):
            lista1.append(i)
        for i in range(4, 2, -1):
            lista2.append(i)
        if lista1 == lista2:
            return True
        return False

def montaña(amigo):

    lista = []
    for i in amigo:
        lista.append(elemento)
    if digitos == 3:
        lista.insert(0, 0)
        lista.insert(0, 0)
    if digitos == 4:
        lista.insert(0, 0)

    if lista[0] < lista[1]:
        if lista[1] < lista[2]:
            if lista[2] > lista[3]:
                if lista[3] > lista[4]:
                    return True
                return False
            return False
        return False
    return False

if comprobarAmigo(amigo, premiado):
    if capicua(amigo):
        if montaña(amigo):
            print(True)
        print("No existe dicho número")
    print("No existe dicho número")
print("No existe dicho número")