"""
Stosując wyrażenie listotwórcze (list comprehension) utwórz listę numerów telefonów (każdy
jako str) o postaci +4812300XYYY , gdzie X może być cyfrą od 1 do 5, a Y może być dowolną
cyfrą. Oblicz długość listy (powinno być 5000).
Następnie wypisz na ekran dziesięć losowo wybranych numerów z tej listy.

"""
import random
from random import randint

numery = ['+4812300' + str(x) + str(y1) + str(y2) + str(y3)
           for x in range (1,6)
           for y1 in range (0,10)
           for y2 in range (0,10)
           for y3 in range (0,10)]

print('Rozmiar listy:', len(numery))
print('Pierwsze 10 elementow:', numery[:10])
print('Ostatni element:', numery[-1])
with open('nowy_plik.txt', mode='w', encoding='utf-8') as plik2:
    print(numery)

'''#metoda 1
for _ in range (10):
    poz = random.randrange(5000)
    print(numery[poz])

#metoda 2 (sample)

print('\nLosowe elementy:')
for numer in random.sample(numery, 10):
    print(numer)'''

"""#metoda3
numery = [f'+4812300{x}{y1:03}'
           for x in range (1,6)
           for y1 in range (0,1000)]
for numer in random.sample(numery, 10):
    print(numer)
"""