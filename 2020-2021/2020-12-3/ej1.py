def mcd(a, b):
    
    if b == 0:
        return a

    return mcd(a, a%b)