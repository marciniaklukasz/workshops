# W tej wersji:
# - usuwam wcięcia i puste linie
with open('pan_tadeusz.txt', mode='r', encoding='utf-8') as wejscie:
    linie = wejscie.readlines()

print('plik odczytany, liczba linii: ', len(linie))
print('sortuje...')
linie.sort()
print('zapisuje plik...')
with open('sorted.txt', mode='w', encoding='utf-8') as wyjscie:
    wyjscie.writelines(linie)
