from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dydx(y, x):
    return y/x - y**2

x = np.linspace(1, 2, 100)

y1 = 1.
sol = odeint(dydx, y1, x)

plt.plot(x, sol)
plt.savefig("solucion.png")