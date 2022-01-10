import math
from ej5.py import *

def funcion(x):
    if x == 0:
        return 1
    return math.sin(x)/x

print(f(2,3))

n = 5
def integral(n):
    b = math.pi/2
    a = math.pi/4

    delta_x = (b-a)/n
    suma = 0
    for i in range(n):
        suma += (funcion(i) + funcion(i+1))/2
    return delta_x*suma

error = 0.001

while integral(n+5) - integral(n) >= error:
    n += 5

print(n)
print(integral(n))