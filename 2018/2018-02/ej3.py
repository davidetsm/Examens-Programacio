from sys import argv
import matplotlib.pyplot as plt

entrada = open(argv[1], "r")

n = int(entrada.read(2))

x = []
y = []

for i in range(3, n+4):
    lista = (entrada.readline(i)).split()
    if i != 3:
        x.append(int(lista[0]))
        y.append(int(lista[1]))
    

entrada.close()

plt.plot(x, y)
plt.show()