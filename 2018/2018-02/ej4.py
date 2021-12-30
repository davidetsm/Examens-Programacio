from scipy.integrate import quad
import numpy as np

valores_a = np.linspace(1, 10, 100)

def f(i):
    return(1/(np.sqrt(i**2-x**2)))

for i in valores_a:
    lista = quad(f(i), 0, i)
    condicion = True
    if lista[0] - (np.pi/2) > lista[1]:
        condicion = False
    if condicion == False:
        break

print(condicion)