def funcion(x):
    return x**3 + 3*x**2 - 6*x -5

a = 1
b = 10
error = 10e-6

def metodoSecante(f, a, b, error):
    x1 = b
    x0 = a
    while abs(x1 - x0) >= error:
        x0, x1 = x1, x1 - ((x1 - x0)/(f(x1) - f(x0))*f(x1))
    return x1

print(metodoSecante(funcion, a, b, error))