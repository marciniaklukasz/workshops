'''
Napisz program, ktory wypisuje na wyjscie tabliczke mnozenia 10x10

1
'''

a = int(input("Podaj wymiar a: "))
b = int(input("Podaj wymiar b: "))
szerokosc = len(str(a*b))
for i in range(1,a+1):
    for x in range(1,b+1):
        print(f"{i * x : {szerokosc}}", end=' ')
    print()
