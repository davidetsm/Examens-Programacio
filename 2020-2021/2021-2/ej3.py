import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, x):
    return (y/x)-y**2

y1 = 1

x = np.linspace(1, 2, 100)

sol = odeint(f, y1, x)

plt.plot(x, sol)
plt.show()