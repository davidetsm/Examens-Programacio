import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, x):
    return (1-(3*x)-(3*y))/(1 + x + y)

y0 = 0

x = np.linspace(0, 1, 100)

sol = odeint(f, y0, x)
print(sol)

plt.plot(x, sol)
plt.show()