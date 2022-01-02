from scipy.integrate import quad
import numpy as np 
import matplotlib.pyplot as plt

def funcion(t):
    return t^(t-1)*np.exp^(-t)

def Gamma(x):
    sol, err = quad(funcion(x), 0, np.Infinity)
    return sol

x_ = np.linspace(1, 2, 100)
y = []
for i in x_:
    y.append(Gamma(i))

plt.plot(x_, y)
plt.show()