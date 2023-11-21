"""
Użytkownik podaje liczbę "limit"

Napisz program ktory przegląda wszystkie liczby od 1 do podanego limitu wlacznie:
- jezeli liczba jest podzielna przez 3 -> to wypisuje "Fizz {liczba}"
- jezeli liczba jest podzielna przez 5 -> to wypisuje "Buzz {liczba}"
- jezeli liczba jest jednoczenie podzielna przez 3 oraz 5 -> to wypisuje FizzBuzz {liczba}
"""


liczba = int(input("Wypisz liczbe od 1 do 100"))
print(f"Twoja liczba to {liczba}")
print(f"...")

fizbuz = []
fiz = []
buz = []
for i in range (1, liczba+1):
    if i%15 == 0:
        fizbuz.append(i)
    elif i%3 == 0:
        fiz.append(i)
    elif i%5 == 0:
        buz.append(i)

print(f"Liczby z kategori fiz: {fiz}",len(fiz))
print(f"Liczby z kategori buz: {buz}",len(buz))
print(f"Liczby z kategori fizbuz: {fizbuz}",len(fizbuz))

"""for i in range (1, liczba+1):
    if i%15 == 0:
        print(f"{i} - Fizbuzz")
    elif i%3 == 0:
        print(f"{i} - Fizz")
    elif i%5 == 0:
        print(f"{i} - Buzz")"""
