def secCollatz(n):
    for i in range(1, n+1):
        num = i
        lista = []
        lista.append(i)
        while i != 1:
            if i % 2 == 0:
                i = i/2
                lista.append(int(i))
            else:
                i = i*3 + 1
                lista.append(int(i))
        print("{} {}". format(num, len(lista)))

secCollatz(5)