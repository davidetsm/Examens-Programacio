contador = 1
suma = 0

while True:
    try:
        entrada = input("Introduce el número {} (s para acabar): ".format(contador))
        num = float(entrada)
        suma += num**2
        contador += 1
    except:
        if entrada == "s":
            break
        entrada = input("Introduce el número {} (s para acabar): ".format(contador))

print(suma/(contador-1))