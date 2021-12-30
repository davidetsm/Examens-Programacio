contador = 1
numero = input("Introduce el número " + str(contador) + " (s para acabar): ")

suma = 0

while numero != "s":
    try: 
        suma += float(numero)**2
        contador += 1
        numero = input("Introduce el número " + str(contador) + " (s para acabar): ")
    except:
        print("Número incorrecto")
        numero = input("Introduce el número " + str(contador) + " (s para acabar): ")

if numero == "s":
    print(suma/(contador-1))