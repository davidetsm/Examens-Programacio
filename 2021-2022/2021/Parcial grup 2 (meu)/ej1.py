'''
David Sánchez Mas, 74394689Q
'''
renta = float(input("Introduce tu renta: "))

suma = 0


if renta <= 12450:
    suma = round(renta*0.19,2)
elif renta <= 20200 and renta > 12450:
    suma = round(12450*0.19 + (renta - 12450)*0.24, 2)
elif renta <= 35200 and renta > 20200:
    suma = round(12450*0.19 + 7750*0.24 + (renta - 20200)*0.3, 2)
elif renta > 35200:
    suma = round(12450*0.19 + 7750*0.24 + 15000*0.3 + (renta-35200)*0.37, 2)

print(suma)
