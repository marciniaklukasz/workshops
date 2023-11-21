import random

# po zaimportowaniu modułu w taki sposób (bez słowa from) mogę używać wszystkich funkcji z modułu,
# ale poprzedzając nazwą modułu, np. random.randint()

# Gdybyśmy zainicjalizowali generator liczb pseudolosowych na tę samą wartość, to na róznych komputerach będziemy uzyskiwać te same ciągi liczb
# random.seed(0)

# Jeśli tego nie zrobimy, to Python weźmie pod uwagę stan zegara.

# zwraca liczbę typ float z zakresu od 0 do 1
print(random.random())

# randint(a, b) zwraca liczbę całkowitą z zakresu od a do b włącznie
print(random.randint(10, 20))

# randrange - sposób użycia odpowiada generatorowi range, o którym później
# randrange(b) - od 0 włącznie do b wyłączając
print(random.randrange(10)) # od 0 do 9

# randrange(a, b) - od a włącznie do b wyłączając
print(random.randrange(50, 60)) # od 50 do 59

# randrange(a, b, c) - od a włącznie do b wyłączając, ale idąc krokiem c
print(random.randrange(50, 60, 2)) # od 50 do 58, ale tylko liczby parzyste

# wybór wartości z listy
kolory = ['czerwony', 'zielony', 'niebieski', 'żółty', 'purpurowy']

# wybór jednej z wartości z równym prawdop.
print(random.choice(kolory))

# wybór wielu wartości:
# z możliwością powtórzenia (wielokrotne losowanie z pełnego zbioru)
print(random.choices(kolory, k=3))
# z wagami dla podanych pozycji; żółty nie ma prawa się pojawić
print(random.choices(kolory, weights=[5, 2, 2, 0, 1], k=3))

# wybór bez możliwości powtórzenia (wybór podzbioru)
print(random.sample(kolory, k=3))
