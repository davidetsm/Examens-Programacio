error = 10e-12

def potencia(x, n):
    if n == 1:
        return x*x*x
    while n != 1:
        return x*x*potencia(x, 2*n-1)

def factorial(n):
    return ()

def CalculoSeno(x):
    return 