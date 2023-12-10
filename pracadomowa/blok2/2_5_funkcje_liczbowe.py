def suma_cyfr(n):
    suma = 0
    for cyfra in str(n):
        suma += int(cyfra)
    return suma
print(suma_cyfr(22))
