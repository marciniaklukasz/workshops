def silnia(n):
    wynik = 1
    for i in range (1,n+1):
        wynik = wynik * i
    return(wynik)



#aby zakonczyc, wpisz liczbe ujemna
while True:
    x = int(input("Podaj argument: "))
    if x <0: break
    wynik = silnia(x)
    print(f'{x}! = {wynik}')
