def anyadirElementos(v, w, n):
    
    if n >= len(w):
        for i in range(len(w)):
            v.append(w[i])
        for i in range(len(w)):
            w.pop(0)
        print(v)
        print(w)
        return

    if n >= 0 and n < len(w):
        for i in range(n):
            v.append(w[i])
        for i in range(n):
            w.pop(0)
        print(v)
        print(w)
        return


v = [10, 20, 30]
w = [1, 2, 3]
anyadirElementos(v, w, 3)