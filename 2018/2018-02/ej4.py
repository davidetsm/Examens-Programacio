from scipy.integrate import quad
import numpy as np

valores_a = np.linspace(1, 10, 100)

for i in valores_a:
    def f(x):
        return(1/(np.sqrt(i**2-x**2)))
    lista = quad(f, 0, i)    #El método quad devuelve una tupla, el primer término es el valor de la integral y el segundo el error estimado.
    condicion = True
    if lista[0] - (np.pi/2) > lista[1]:
        condicion = False
    if condicion == False:
        break

print(condicion)