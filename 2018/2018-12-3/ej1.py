def Catalan(n):

    suma = 0
    
    if n == 0:
        return 1
    if n >= 1:
        for i in range(n):
            suma += Catalan(i)*Catalan(n-(i+1))
        return suma

print(Catalan(int(input())))