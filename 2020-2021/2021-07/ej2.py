from sys import argv

def fibonacci(n):
    if n <= 2:
        return n - 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

suma = 0
for i in range(1, int(argv[1]) + 1):
    suma += fibonacci(i)

print(suma)