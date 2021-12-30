num = int(input("Introduce un número entero positivo: "))


if num%2 == 0:
    for i in range(0, num//2):
        print(2*i, end = " ")
        print(num - (2*i + 1), end = " ")
    print(num)

if num%2 != 0:
    for i in range(0, num//2 + 1):
        print(2*i, end = " ")
        print(num - 2*i, end = " ")