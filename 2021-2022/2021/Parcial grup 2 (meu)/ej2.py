'''
David Sánchez Mas, 74394689Q
'''
import math

a = 0
b = 10
error = 0.001


n = 10 #Número inicial de trapecios

def funcion(i):
    return math.sin(i)/i

def integral(a, b, n):
    deltax = (b-a)/n
    suma = 0
    for i in range(n):
        if i == 0 :
            suma += (1 + funcion(1)) / 2
        else:
            suma += (funcion(i) + funcion(i+1)) / 2
    return deltax*suma

while (integral(a, b, n+5) - integral(a, b, n))  > error:
    n += 5


print(n+5)
print(integral(a, b, n+5))
