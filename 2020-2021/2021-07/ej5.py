import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(u):
    return u/(np.e**(-u))

x = np.linspace(0, 5, 100)
y = []


for i in x:
    sol, err = quad(f, 0, i)
    y.append(sol)

print(y)

plt.plot(x, y)
plt.show()