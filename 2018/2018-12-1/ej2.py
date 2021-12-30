def combinaciones(n):
    valores = []

    for m in range(n+1):
        print(combinaciones(n-1))
    return c