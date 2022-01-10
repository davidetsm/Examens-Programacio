from scipy.integrate import quad
import numpy as np 
import matplotlib.pyplot as plt

def Gamma():
        sol, err = quad(funcion, 0, np.Inf)
        return sol

x = np.linspace(1, 2, 100)
y = []
for i in x:
    def funcion(t):
        return t**(i-1)*np.e**(-t)
    sol = Gamma()
    y.append(sol)

plt.plot(x, y)
plt.show()