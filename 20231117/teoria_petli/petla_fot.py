# for zmienna in kolekcja: instrukcje

# Z kolekcji pobierane są kolejne elementy, każdy z nich wpisywany jest na zmienną
# i wykonywane są instrukcje podane w treści pętli.

miasta = ['Toruń', 'Bydgoszcz', 'Grudziądz']
for miasto in miasta:
    print('Zapraszamy do miasta', miasto)
    print(' na wycieczkę :-)')
print('Miasta wypisane.\n')

# Źródłem danych może być dowolny "obiekt iterowalny" (iterable).
# Może być to kolekcja, napis, otwarty plik, generator.

# W przypadku napisów pętla for przegląda pojedyncze znaki.
# Ciekawostka dla programistów: pojedynczy znak też jest typu str (w Pythonie nie ma typu char)
napis = 'abecadło z pieca spadło'
for znak in napis:
    print(znak, end=', ')
print('\n========\n')

# Bardzo częstą sytuacją jest przeglądanie za pomocą pętli for liczb z określonego przedziału
# podanego za pomocą generatora range.

for liczba in range(1, 11):
    print('Kolejna liczba:', liczba)

# ogólna podstać: range(start, stop, step)
# generowane są liczby od start włącznie do stop wyłączając z krokiem step
# przy czym domyślnie step=1, a start=0

print('\nrange(10, 30, 3):')
for i in range(10, 30, 3):
    print(i, end=', ')
print()

print('\nrange(10, 20):')
for i in range(10, 20):
    print(i, end=', ')
print()

print('\nrange(20):')
for i in range(20):
    print(i, end=', ')
print()

print('\nrange(50, 40, -1):')
for i in range(50, 40, -1):
    print(i, end=', ')
print()
